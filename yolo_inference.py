from ultralytics import YOLO

# inference for object
model = YOLO('yolov8l')
results = model.predict('input_videos/08fd33_4.mp4',save=True)
print(results[0])
print('=================================')
for box in results[0].boxes:
    print(box)
