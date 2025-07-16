import torch
from ultralytics import YOLO

torch.backends.cudnn.benchmark = True

# Check if CUDA is available and select the GPU
if torch.cuda.is_available():
    device = "cuda"  # Use GPU
    print("\n✅ Running on GPU:", torch.cuda.get_device_name(0))
else:
    raise RuntimeError("\n⚠️ No GPU detected! Please check your CUDA installation.")

if __name__ == '__main__':
    # Load the trained YOLOv8 model
    model = YOLO(r'D:\coco\Datasets\yolo_V8_trained3\weights\best.pt')  # Path to your trained model file

    # Test the model with test data
    results = model.predict(
        source=r"D:\coco\Datasets\Final_Dataset\test\images\52431.jpg",  # Specify the test data directory
        imgsz=512,  # Resize image to 512x512 for prediction
        conf=0.1  # Set a confidence threshold for detection
    )

    # Show the results (detections and bounding boxes on images)
    for r in results:
        r.show()  # Display each image with bounding boxes

    # Save the results (images with bounding boxes) to a folder
    for i, r in enumerate(results):
        r.save(filename=f"D:\coco\output\result_{i}.jpg")  # Save output images to a specific folder

    # Get the predictions in pandas DataFrame format
    print("\n📊 Prediction Details:")
    for i, r in enumerate(results):
        df = r.pandas().xywh  # Get predictions for each image
        print(f"\n🔹 Image {i+1} Predictions:")
        print(df.head())  # Display first few predictions for each image

    # Evaluate the model (Optional)
    print("\n📌 Running model evaluation...")
    metrics = model.val()  # Evaluate on validation set

    print("\n📊 Evaluation Metrics:")
    print(f"Precision: {metrics.box.pr:.4f}")
    print(f"Recall: {metrics.box.re:.4f}")
    print(f"mAP50: {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")

    # GPU Utilization Check
    print("\n📌 Checking GPU utilization...")
    print("Run `nvidia-smi` in the terminal to monitor GPU usage.")
