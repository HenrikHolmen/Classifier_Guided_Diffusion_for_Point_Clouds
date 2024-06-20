#!/bin/sh
### General options
### -- specify queue --
###BSUB -q hpc
###BSUB -q gpua100
#BSUB -q gpuv100
### -- Select the resources: 1 gpu in exclusive process mode --
#BSUB -gpu "num=1:mode=exclusive_process"
### –- specify queue --
### -- set the job Name --
#BSUB -J test_baseline_generator_num_200V2_
### -- ask for number of cores (default: 1) --
#BSUB -n 4
### -- specify that the cores must be on the same host --
#BSUB -R "span[hosts=1]"
### -- specify that we need xGB of memory per core/slot --
#BSUB -R "rusage[mem=6GB]"
###BSUB -R "select[gpu80gb]"
#BSUB -R "select[gpu32gb]"
#### -- specify that we want the job to get killed if it exceeds 5 GB per core/slot --
###BSUB -M 128GB
### -- set walltime limit: hh:mm --
#BSUB -W 08:00
### -- set the email address --
#BSUB -u s210659@dtu.dk
### -- send notification at start --
#BSUB -B
### -- send notification at completion --
#BSUB -N
### -- set the job output file --
### -- Specify the output and error file. %J is the job-id --
### -- -o and -e mean append, -oo and -eo mean overwrite --
#BSUB -o test_baseline_generator__num_200V2_%J.out
#BSUB -e test_baseline_generator__num_200V2_%J.err
# all  BSUB option comments should be above this line!

# execute our command
source ~/.bashrc
conda activate dpm-pc-gen
module load cuda/10.1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/zhome/0f/e/160664/miniconda3/lib/
python /zhome/0f/e/160664/projects/probabilistic_diffusion_model/code/Code_Baseline/test_gen.py
