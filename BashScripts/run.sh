#!/bin/bash
#./initialize.sh
cd ..

echo "Running config_tcga"
#python BLRunner.py --config config-files/config_tcga.yaml

# echo "Running config_dream4_10\n"
# python BLRunner.py --config config-files/config_dream4_10.yaml

# echo "Running config_dream4_100\n"
#python BLRunner.py --config config-files/config_dream4_100.yaml
# python BLEvaluator.py --config config-files/config_dream4_10.yaml -n -z -y -t -e -x -j -a -u 
# python BLEvaluator.py --config config-files/config_dream4_100.yaml -n -z -y -t -e -x -j -a -u 
#python BLEvaluator.py --config config-files/config_dream4_100.yaml -a -u #-j -n -z -y -t -e -x

# echo "Running config_sergio_bulk_100\n"
# python BLRunner.py --config config-files/config_sergio_bulk_100.yaml


# echo "Running config_sergio_400\n"
# python BLRunner.py --config config-files/config_sergio_400.yaml
python BLEvaluator.py --config config-files/config_dream4_100.yaml -a -u -j -n -z -y -t -e -x

# echo "Running config_sergio_bulk_400\n"
python BLRunner.py --config config-files/config_sergio_bulk_400.yaml

#echo "Running config_sergio_1200\n"
# python BLRunner.py --config config-files/config_sergio_1200.yaml

# echo "Running config_sergio_bulk_1200\n"
python BLRunner.py --config config-files/config_sergio_bulk_1200.yaml

# echo "Running config_sergio_100\n"
# python BLRunner.py --config config-files/config_sergio_100.yaml
