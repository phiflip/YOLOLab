# YOLOv8Lab
<img src="https://github.com/phiflip/YOLOv8Lab/blob/main/icons/YOLOv8Lab_final_icon_nobackgorund_highRes.png" width="200" alt="ModVegePy main logo type">
</div>
Welcome to the YOLOv8Lab repository, a dedicated platform for setting up and using YOLOv8 for object detection tasks in educational settings.
<br />
<br />
This repository and code is based on the YOLOv8 project by: Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0)
[Computer software]. https://github.com/ultralytics/ultralytics

## Installation

This project assumes that Anaconda and Spyder are installed on your Windows system. Follow the steps below to set up your environment.

### Prerequisites

- Anaconda: Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual).
  See installation guides for different operating systems:
   - [Installing on Windows](https://docs.anaconda.com/free/anaconda/install/windows/),
   - [Installing on Linux](https://docs.anaconda.com/free/anaconda/install/linux/),
   - [Installing on macOS](https://docs.anaconda.com/free/anaconda/install/mac-os/).
- Python >= 3.9 (comes with Anaconda)

### Directory structure

1. **Create the yolov8 project folder**
```bash
C:/
├─ Users
│   ├─ UserName
│   │   ├─ yolov8                  
│   │   │   ├─ labeling/        
│   │   │   ├─ train/
│   │   │   ├─ test/     
│   │   │   └─ valid/
│   │   └─ ...             
│   └─ ...
└──...
```
### Environment Setup (via Anaconda Prompt)

2. **Create a new conda environment (in the windows search bar type "Anaconda Prompt"):**
   ```bash
   conda create --name yolov8 python=3.9 spyder=5
   ```

3. **Activate the environment:**
   ```bash
   conda activate yolov8
   ```

5. **Install Required Packages:**
   ```bash
   pip install ultralytics
   ```

6. **Launch Spyder within the new environment:**
   ```bash
   spyder
   ```
7. **… and check your installation by opening and running the yolov8_test.py in Spyder:**
   
   [Download yolov8_test.py](https://github.com/phiflip/YOLOv8Lab/blob/main/scripts/yolov8_test.py)

### Additional Tools

1. **Install labelImg for image annotation using the same activated yolov8 environment:**
   ```bash
   conda install -c conda-forge labelimg
   ```
2. **Start the labeling software:**
   ```bash
   labelImg
   ```
