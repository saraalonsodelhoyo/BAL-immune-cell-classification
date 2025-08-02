# Immune Cell Classification from BAL Images Using YOLOv12

This project focuses on the **automatic classification of immune cells** in **bronchoalveolar lavage (BAL)** cytology images using the **YOLOv12** architecture. The goal is to perform **fast and accurate object detection and classification** of immune cells to assist in clinical diagnostics and research.

---

## Project Structure

```python
BAL-immune-cell-classification/
│
├── train.py                   # Main training script using YOLOv12
├── inference.py              # Inference script using trained weights
├── requirements.txt          # Python dependencies
├── README.md                 # Main project README
│
├── models/                   # Trained model weights (downloaded separately)
│   ├── best_yolo12n.pt       # Example trained weight file
│   └── best_yolo12x.pt       # Other trained models
│
├── dataset/                  # Dataset structure (images and YOLO labels)
│   ├── images/
│   │   ├── train/            # Training images
│   │   └── val/              # Validation images
│   ├── labels/
│   │   ├── train/            # YOLO-format label .txt files
│   │   └── val/              # Validation labels
│   └── cell_detection.yaml   # Dataset configuration (auto-generated)
│
├── data_transformation/      # Scripts for preprocessing and label format conversion
│   ├── create_yolo_annotations.ipynb  # Converts segmentation masks to YOLO labels
│   ├── geojson_2_yolo.py     # Converts GeoJSON to YOLO format
│   ├── yolo_2_geojson.py     # Converts YOLO annotations to GeoJSON
│   └── README.md             # Info about transformation tools
│
├── scripts/                  # SLURM job submission scripts
│   ├── run_training.sh       # Submits training job via sbatch
│   ├── run_inference.sh      # Submits inference job via sbatch
│   └── README.md             # Explanation of SLURM usage
```

---

## Project Overview

- **Goal:** Automatically detect and classify 4 types of cells in BAL images.
- **Model:** Trained YOLOv12 models (e.g., `yolo12n`, `yolo12x`)
- **Classes:**  
  `['macrophages', 'lymphocytes', 'polymorphonuclear cells', 'eosinophils']`
- **Tools:** Ultralytics YOLOv12, Weights & Biases (`wandb`), SLURM for job scheduling.

---

## Installation

Requires Python 3.8+, PyTorch, and OpenCV

```python
# Clone the repository
git clone https://github.com/saraalonsodelhoyo/BAL-immune-cell-classification
cd BAL-immune-cell-classification

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Training

Train a model using SLURM:

```python
sbatch scripts/run_training.sh dataset_name
```

The script executes `training.py`, which uses your dataset and saves results in a project-specific folder.
W&B logging is supported and enabled by default.

## WANDB Setup

Install and initialize Weights & Biases:

```python
pip install -U ultralytics wandb
yolo settings wandb=True

# Login (choose one method)
wandb login YOUR_API_KEY         # CLI
# or
import wandb; wandb.login(key="YOUR_API_KEY")  # Python
```

## Inference

Run inference on a trained model:

```python 
sbatch scripts/run_inference.sh
``` 

This runs inference.py using the weights specified in the SLURM script.

## Model Weights

Download the trained YOLOv12 models from Google Drive:

**[Model weights – Google Drive](https://drive.google.com/drive/folders/1--A-mW5Y3dX8wpkTLbM-bX8rf6rylmxl?usp=drive_link)**

Place the downloaded `.pt` files into the `models/` folder of this project.

> These trained weights were obtained by fine-tuning the official **YOLOv12 pretrained models** (from Ultralytics) on our custom BAL dataset.  
> Each model variant (e.g., `yolo12n`, `yolo12x`, etc.) was trained using the structure and data provided in the `dataset/` folder.

### YOLOv12 Base Models (Ultralytics)

These were used as the starting point for training:

| Model Variant | Download Command |
|---------------|------------------|
| [Nano](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12n.pt)          | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12n.pt` |
| [Small](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12s.pt)         | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12s.pt` |
| [Medium](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12m.pt)        | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12m.pt` |
| [Large](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12l.pt)         | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12l.pt` |
| [X-Large](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12x.pt)       | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12x.pt` |

---

## Dataset

The dataset is **not included** in the repository due to size restrictions.

Download the full dataset from:  
**[Data – Google Drive](https://drive.google.com/drive/folders/1jzIaSdwMp5ZQKIjxjruXzNyv1CUVvtb-?usp=drive_link)**

Once downloaded, extract and place the files inside the `dataset/` folder using the following structure:

```python
dataset/
├── images/
│   ├── train/         # Training images
│   └── val/           # Validation images
├── labels/
│   ├── train/         # YOLO-format .txt files for training
│   └── val/           # YOLO-format .txt files for validation
```

During training, a configuration file named `cell_detection.yaml` will be automatically generated inside the `dataset/` folder. This file contains:

- Paths to training/validation image directories
- Number of classes (`nc)
- List of class names:
`['macrophages', 'lymphocytes', 'polymorphonuclear cells', 'eosinophils']`

## Data Transformation

The project initially used segmentation masks, which were converted to YOLO bounding box format.

Folder data_transformation/ includes:

- Notebook to convert segmentation masks → YOLO bounding boxes

- Scripts to convert labels formats between YOLO and GeoJSON

Run transformation:

```python
python data_transformation/create_yolo_annotations.ipynb
```

Refer to `data_transformation/README.md` for more.

## License

This project is for academic research purposes. License terms may depend on data usage permissions.

## Maintainer

**Sara Alonso del Hoyo**
This repository was developed as part of a TFG project. Future contributors can build on top of this work.

## Acknowledgments

- Ultralytics YOLOv12

- Weights & Biases

- HPC Cluster at UPC
