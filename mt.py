import torch
from ultralytics import YOLO
import shutil

torch.backends.cudnn.benchmark = True

# Check if CUDA is available
if torch.cuda.is_available():
    device = "cuda"
    print("\n✅ Running on GPU:", torch.cuda.get_device_name(0))
else:
    raise RuntimeError("\n⚠️ No GPU detected! Please check your CUDA installation.")

if __name__ == '__main__':
    # Load the existing trained model
    model_path = r"D:\coco\Datasets\yolo_V8_trained3\weights\best.pt"  # Existing best.pt
    model = YOLO(model_path)  # Load best.pt for fine-tuning

    # Fine-tune on the new bull dataset without affecting other classes
    model.train(
        data=r"D:\coco\bull_data.yaml",  # New dataset
        epochs=50,  # Fine-tune for 50 epochs
        batch=8,  # Adjust batch size based on VRAM
        imgsz=640,  # Image size
        device="cuda",  # Use GPU
        optimizer="SGD",  # Same optimizer as before
        lr0=0.0005,  # Lower learning rate to avoid forgetting
        lrf=0.00001,  # Final learning rate
        weight_decay=0.0001,  # Reduce regularization
        momentum=0.9,  # Stabilizes training
        amp=True,  # Mixed precision
        workers=0,  # Reduce workers for small dataset
        dropout=0.05,  # Lower dropout since dataset is small
        val=True,  # Enable validation
        save=True,  # Save model after fine-tuning
        patience=7,  # Early stopping
        freeze=[0],  # **Freeze backbone, train only detection layers**
        project=r"D:\coco\Datasets\yolo_V8_trained3",  # **Use the same folder as before**
        name="weights",  # **Save directly in the existing folder**
        resume=True,  # **Continue training from the old best.pt**
    )

    print("\n✅ The existing best.pt has been updated with new training on the bull dataset.")
