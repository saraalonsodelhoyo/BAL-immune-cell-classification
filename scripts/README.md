# SLURM Job Scripts

This folder contains SLURM batch scripts used to launch training and inference jobs for the YOLO-based BAL cell classification project on a high-performance computing (HPC) cluster.

---

## Training Script

### `run_training.sh`

Use this script to submit a training job via SLURM.

```python
sbatch scripts/run_training.sh dataset_name
```

- `dataset_name`: You can pass a dataset identifier or name to the script. Make sure your `training.py` file handles this argument correctly (e.g., using it to select dataset paths or configuration files).

- The script is expected to launch `training.py` with the appropriate arguments.

Before running, check that:

- `training.py` points to the correct dataset path
- The model weights (if starting from pretrained) are accessible
- Any wandb configuration (if used) is set correctly

## Inference Script

### `run_inference.sh`

Use this script to run inference with a trained YOLO model.

```python
sbatch scripts/run_inference.sh
```

Make sure to edit this file and set:

- The correct path to your trained weights (e.g., `models/best_yolo12n.pt`)
- The path to the validation or test images (e.g., `dataset/images/val`)

## SLURM Requirements

These scripts assume:

- You're running on a SLURM-managed cluster (e.g., with `sbatch`)
- Necessary modules (e.g., CUDA, Python) are loaded or a virtual environment is activated inside the script
- GPU resources are requested as needed (see the `--gres=gpu` line in the script)

Example SLURM directives to include in your script:

```python
#SBATCH -p gpi.compute 
#SBATCH --mem=30G 
#SBATCH -c 6
#SBATCH --gres=gpu:1,gpumem:10G
#SBATCH --time=24:00:00
```

## File Overview

| File               | Description                          |
| ------------------ | ------------------------------------ |
| `run_train.sh`     | SLURM script to train the YOLO model |
| `run_inference.sh` | SLURM script to run inference        |

Logs from job executions can optionally be saved in a logs/ folder.