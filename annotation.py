import cv2
import os
import torch
from ultralytics import YOLO

# Specify paths
dataset_path = r"D:\coco\Datasets\mongoose.v1i.multiclass\train"  # Folder containing images
output_labels_path = r"D:\coco\Datasets\mongoose.v1i.multiclass\output_labels"          # Folder for YOLO-format annotations
model_path = "yolov8n.pt"                     # Pre-trained YOLOv8 model

# Create output folder if it doesn't exist
os.makedirs(output_labels_path, exist_ok=True)

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the YOLO model on the specified device
model = YOLO(model_path)
model.to(device)

# Function to normalize bounding box coordinates
def normalize_bbox(x_min, y_min, x_max, y_max, img_width, img_height):
    x_center = (x_min + x_max) / 2 / img_width
    y_center = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height
    return x_center, y_center, width, height

# Process each image
for image_name in os.listdir(dataset_path):
    if image_name.endswith((".jpg", ".png")):
        # Load the image
        image_path = os.path.join(dataset_path, image_name)
        img = cv2.imread(image_path)
        img_height, img_width = img.shape[:2]

        # Perform object detection on the specified device
        results = model(image_path, device=device)

        # Open a .txt file to save annotations
        txt_file_name = os.path.splitext(image_name)[0] + ".txt"
        txt_file_path = os.path.join(output_labels_path, txt_file_name)

        with open(txt_file_path, "w") as f:
            for result in results[0].boxes:
                # Get bounding box coordinates and class ID
                x_min, y_min, x_max, y_max = result.xyxy[0].cpu().numpy()
                class_id = int(result.cls.cpu().numpy())

                # Normalize the bounding box
                x_center, y_center, width, height = normalize_bbox(x_min, y_min, x_max, y_max, img_width, img_height)

                # Write to YOLO format
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

        print(f"Annotated: {image_name}")

print("Annotation completed. YOLO format labels saved to:", output_labels_path)
