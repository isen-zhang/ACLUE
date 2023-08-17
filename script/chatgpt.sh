#!/bin/bash
#SBATCH --job-name=chatgpt
#SBATCH --output=./stdout/slurm-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=100G
#SBATCH --time=12:00:00
#SBATCH --cpus-per-task=4

#SBATCH --gres=gpu:1
#SBATCH -p gpu
#SBATCH --qos=gpu-8

cd ../src
for i in 0 5
do
python chatgpt.py \
    --save_dir ../results/ChatGPT \
    --num_few_shot $i
done

