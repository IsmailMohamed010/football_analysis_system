from ultralytics import YOLO

model = YOLO("models/best.pt")  # Load a custom model

results = model.predict(source="input/08fd33_4.mp4", save=True, save_txt=True)
print(results[0])