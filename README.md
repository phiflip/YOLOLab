# YOLOv8Lab
<img src="https://github.com/phiflip/YOLOv8Lab/blob/main/icons/YOLOv8Lab_final_icon_nobackgorund_highRes.png" width="200" alt="ModVegePy main logo type">
</div>
Welcome to the YOLOv8Lab repository, a dedicated resource center for setting up and using YOLOv8 for object detection tasks in educational settings. This repository serves as a hub for individuals interested in configuring and deploying YOLOv8 for custom object detection.

## Installation

This project assumes that Anaconda and Spyder are installed on your Windows system. Follow the steps below to set up your environment.

### Prerequisites

- Anaconda: Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual).
- Python 3.9

### Environment Setup

1. **Create a Conda Environment:**
   ```bash
   conda create --name yolov8 python=3.9 spyder=5
   ```

2. **Activate the Environment:**
   ```bash
   conda activate yolov8
   ```

3. **Install Required Packages:**
   ```bash
   pip install ultralytics
   ```

4. **Launch Spyder within the new environment:**
   ```bash
   spyder
   ```
5. **…and check by opening and running the yolov8_test.py if it doesn’t
create any further error messages.**

[Download yolov8_test.py](https://github.com/phiflip/YOLOv8Lab/blob/main/scripts/yolov8_test.py)


## Usage

In this repository, you will find various CLI snippets that help perform basic tasks such as loading and running test datasets.

### Sample Snippet

```bash
python yolov8_test.py
```

## Most important command line interface (CLI) commands
### run an pretrained yolo object detector on your webcam
```bash
yolo predict model=yolov8n.pt source=0 show=True
```
## Test Dataset

A test dataset is included in the `data/test` directory. This can be used to verify the functionality of YOLOv8 after the installation is complete.
