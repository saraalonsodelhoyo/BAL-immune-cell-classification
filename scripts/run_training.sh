#!/bin/bash
#SBATCH -p gpi.compute 
#SBATCH --mem=30G 
#SBATCH -c 6
#SBATCH --gres=gpu:1,gpumem:10G
#SBATCH --time=24:00:00

# Usage: ./run_training.sh <dataset_name> 
# Example: ./run_training.sh bin_dataset

# Check for required argument
if [ -z "$1" ]; then
    echo "❌ Error: Missing dataset name."
    echo "Usage: ./run_training.sh <dataset_name>"
    exit 1
fi

DATASET_NAME="$1"

# Activate virtual environment
source ./venv/bin/activate

# Run the training script
python training.py "$DATASET_NAME"