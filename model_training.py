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
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Train the model with optimizations
    model.train(
        data=r"D:\coco\Datasets\Final_Dataset\data.yaml",  # Replace with your dataset YAML
        epochs=100,  # Train for 100 epochs
        batch=16,  # Start with 16, increase to 32 if VRAM allows
        imgsz=640,  # Image size
        device="cuda:0, cuda:1",  # Use GPU (RTX 3070)
        optimizer="SGD",  # AdamW is better for convergence
        lr0=0.01,  # Initial learning rate
        lrf=0.0001,  # Final learning rate
        weight_decay=0.0005,  # Helps regularize
        momentum=0.937,  # Stabilizes training
        amp=True,  # Mixed precision for faster training
        workers=12,  # Utilize all 12 cores for data loading
        dropout=0.1,  # Prevents overfitting
        val=True,  # Enable validation during training
        save=True,  # Save best models
        patience=20, #for early stopping
        project="runs/train",  # Where to store results
        name="yolo_V8_trained",  # Custom name for the run
    )
    # GPU Utilization Check
    print("\n📌 Checking GPU utilization...")
    print("Run `nvidia-smi` in the terminal to monitor GPU usage.")
