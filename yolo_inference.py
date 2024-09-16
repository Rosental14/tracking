from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('input_videos/liverpool_psg.mp4',
                        save=True, save_dir='output_videos')
print(results[0])
print()
for box in results[0].boxes:
    print(box)
