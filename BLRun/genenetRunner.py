import os
import pandas as pd
from pathlib import Path


ALGORITHM_UPPER = "GENENET"
ALGORITHM_LOWER = "genenet"
USER = "18881888"

def generateInputs(RunnerObj):
    '''
    Function to generate desired inputs for ALGORITHM.
    If the folder/files under RunnerObj.datadir exist, 
    this function will not do anything.
    '''
    if not RunnerObj.inputDir.joinpath(ALGORITHM_UPPER).exists():
        print("Input folder for ALGORITHM does not exist, creating input folder...")
        RunnerObj.inputDir.joinpath(ALGORITHM_UPPER).mkdir(exist_ok = False)
        
    if not RunnerObj.inputDir.joinpath(ALGORITHM_UPPER + "/ExpressionData.csv").exists():
          # input data
        ExpressionData = pd.read_csv(RunnerObj.inputDir.joinpath(RunnerObj.exprData),
                                     sep = '\t', header = 0, index_col = 0)

        # Write .csv file
        ExpressionData.to_csv(RunnerObj.inputDir.joinpath(ALGORITHM_UPPER + "/ExpressionData.csv"),
                             sep = '\t', header = True, index = False)
    
def run(RunnerObj):
    '''
    Function to run ALGORITHM algorithm
    '''
    inputPath = "data" + str(RunnerObj.inputDir).split(str(Path.cwd()))[1] + \
                    "/" + ALGORITHM_UPPER + "/ExpressionData.csv"
    
    # Make output dirs if they do not exist:
    outDir = "outputs/"+str(RunnerObj.inputDir).split("inputs/")[1]+ "/" + ALGORITHM_UPPER + "/"
    os.makedirs(outDir, exist_ok = True)
    
    # Parameters
    num_edges = RunnerObj.params['num_edges']
    directed = RunnerObj.params['directed']
    verbose = RunnerObj.params['verbose']
    
    outPath = "data/" +  str(outDir) + 'outFile.txt'
    cmdToRun = ' '.join(['docker run --rm -v', str(Path.cwd())+':/data/ '+ USER + '/' + ALGORITHM_LOWER + ':base /bin/sh -c \"time -v -o', "data/" + str(outDir) + 'time.txt', 'Rscript run' + ALGORITHM_UPPER + '.R',
                         inputPath, outPath, str(num_edges), str(directed), str(verbose), '\"'])
    print(cmdToRun)
    os.system(cmdToRun)



def parseOutput(RunnerObj):
    '''
    Function to parse outputs from ALGORITHM.
    '''
    # Quit if output directory does not exist
    outDir = "outputs/"+str(RunnerObj.inputDir).split("inputs/")[1]+"/" + ALGORITHM_UPPER + "/"

    if not Path(outDir+'outFile.txt').exists():
        print(outDir+'outFile.txt'+'does not exist, skipping...')
        return
        
    # Read output
    OutDF = pd.read_csv(outDir+'outFile.txt', sep = '\t')

    # Make edgeweights positive
    OutDF["EdgeWeight"] = OutDF["EdgeWeight"].abs()

    # Store as it is in the right format already
    OutDF.to_csv(outDir + 'rankedEdges.csv', sep = '\t', index=False)
