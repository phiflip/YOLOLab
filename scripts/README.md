## Most important command line interface (CLI) commands

## LabelImage
### Run labelImg in the correct folder
   ```bash
   labelimg C:\Users\UserName\yolov8\labeling C:\Users\UserName\yolov8\labeling\predefined_classes.txt 
   ```
## YOLOv8


### Predict on an image
```bash
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

### Run a pretrained yolo object detector on your webcam
   ```bash
   yolo predict model=yolov8n.pt source=0 show=True
   ```

# Add the following (to do)

- images from videos
- CLI commands (webcam, train,val)
- GPU installation
