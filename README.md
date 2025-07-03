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

