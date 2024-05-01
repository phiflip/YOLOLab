from ultralytics import YOLO
import cv2


# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# results = model("//bfhfilerbe01.bfh.ch/ahp1/Desktop/ahp1.jfif")  # predict on an image


# Plot the results
res_plotted = results[0].plot()
cv2.imshow("result", res_plotted)