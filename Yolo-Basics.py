from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model(r"C:\Users\Dr Poonam Pandey\Desktop\Project 4 - Poker Hand Detector\Chapter 5 - Running Yolo\Images\3.png", show=True)
cv2.waitKey(0)