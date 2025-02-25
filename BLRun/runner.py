import BLRun.pidcRunner as PIDC
import BLRun.genie3Runner as GENIE3
import BLRun.genie3_rRunner as GENIE3_R
import BLRun.grnboost2Runner as GRNBOOST2
import BLRun.ppcorRunner as PPCOR
import BLRun.order_mcmcRunner as ORDER_MCMC
import BLRun.partition_mcmcRunner as PARTITION_MCMC
import BLRun.pcRunner as PC
import BLRun.genenetRunner as GENENET
import BLRun.glassoRunner as GLASSO
import BLRun.aracneRunner as ARACNE
import BLRun.corrRunner as CORR

from pathlib import Path


InputMapper = {  
                'PIDC':PIDC.generateInputs,
                'GENIE3':GENIE3.generateInputs,
                'GENIE3_R':GENIE3_R.generateInputs,
                'GRNBOOST2':GRNBOOST2.generateInputs,
                'PPCOR':PPCOR.generateInputs,
                'ORDER_MCMC':ORDER_MCMC.generateInputs,
                'PARTITION_MCMC':PARTITION_MCMC.generateInputs,
                'PC':PC.generateInputs,
                'GENENET':GENENET.generateInputs,
                'GLASSO':GLASSO.generateInputs,
                'ARACNE':ARACNE.generateInputs,
                'CORR':CORR.generateInputs
            }

AlgorithmMapper = {  
                'PIDC':PIDC.run,
                'GENIE3':GENIE3.run,
                'GENIE3_R':GENIE3_R.run,
                'GRNBOOST2':GRNBOOST2.run,
                'PPCOR':PPCOR.run,
                'ORDER_MCMC':ORDER_MCMC.run,
                'PARTITION_MCMC':PARTITION_MCMC.run,
                'PC':PC.run,
                'GENENET':GENENET.run,
                'GLASSO':GLASSO.run,
                'ARACNE':ARACNE.run,
                'CORR':CORR.run
            }

OutputParser = {  
                'PIDC':PIDC.parseOutput,
                'GENIE3':GENIE3.parseOutput,
                'GENIE3_R':GENIE3_R.parseOutput,
                'GRNBOOST2':GRNBOOST2.parseOutput,
                'PPCOR':PPCOR.parseOutput,
                'ORDER_MCMC':ORDER_MCMC.parseOutput,
                'PARTITION_MCMC':PARTITION_MCMC.parseOutput,
                'PC':PC.parseOutput,
                'GENENET':GENENET.parseOutput,
                'GLASSO':GLASSO.parseOutput,
                'ARACNE':ARACNE.parseOutput,
                'CORR':CORR.parseOutput
            }


class Runner(object):
    '''
    A runnable analysis to be incorporated into the pipeline
    '''
    def __init__(self,
                params):
        self.name = params['name']
        self.inputDir = params['inputDir']
        self.params = params['params']
        self.exprData = params['exprData']
        self.cellData = params['cellData']
        
    def generateInputs(self):
        InputMapper[self.name](self)
        
    def run(self):
        AlgorithmMapper[self.name](self)

    def parseOutput(self):
        OutputParser[self.name](self)
