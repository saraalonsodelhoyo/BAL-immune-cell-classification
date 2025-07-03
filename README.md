# Immune Cell Classification from BAL Images Using YOLOv12

This project focuses on the **automatic classification of immune cells** in **bronchoalveolar lavage (BAL)** cytology images using the **YOLOv12** architecture. The goal is to perform **fast and accurate object detection and classification** of immune cells to assist in clinical diagnostics and research.

---

## Project Structure

```python
immune-cell-classification/
│
├── tools/ # Python scripts for training, evaluation, inference
│ ├── train.py
│ ├── eval.py
│ └── infer.py
│
├── experiments/ # YAML config files for different training runs
│ ├── exp1.yaml
│ ├── exp2.yaml
│ └── ...
│
├── scripts/ # Shell scripts for cluster or local execution
│ ├── run_train.sh
│ └── run_infer.sh
│
├── models/ # (Optional) Trained weights and architecture code
│
├── data/ # (Optional) Data loading or augmentation utilities
│
├── README.md # Project documentation (this file)
├── requirements.txt # Python dependencies
```

---

## Installation

> Requires Python 3.8+, PyTorch, and OpenCV

```bash
# Clone this repository
git clone https://github.com/your-username/my-yolo-bal-project.git
cd my-yolo-bal-project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Download pretrained models

Download weights:

### YOLOv12 models

| Model   | Download Link                                                                                     |
|---------|-------------------------------------------------------------------------------------------------|
| [Nano](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12n.pt)      | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12n.pt`      |
| [Small](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12s.pt)     | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo12s.pt`      |
| [Medium](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12m.pt)   | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12m.pt`     |
| [Large](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12l.pt)    | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12l.pt`     |
| [X-Large](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12x.pt)  | `wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov12x.pt`     |


