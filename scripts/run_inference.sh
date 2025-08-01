#!/bin/bash
#SBATCH -p gpi.compute 
#SBATCH --mem=30G 
#SBATCH -c 6
#SBATCH --gres=gpu:1,gpumem:10G
#SBATCH --time=24:00:00

# Activate the virtual environment
source ./venv/bin/activate

# Run the Python script
python inference.py
