import os
import json
from PIL import Image

# Paths
coco_annotations_file = r"D:\coco\Datasets\COCO Dataset.v34-yolov11x-1280.coco\test\_annotations.coco.json"  # Path to COCO JSON file
coco_images_dir = r"D:\coco\Datasets\COCO Dataset.v34-yolov11x-1280.coco\test"  # Path to COCO images directory
output_images_dir = r"D:\coco\Datasets\COCO Dataset.v34-yolov11x-1280.coco\labels\images"  # Output directory for YOLO images
output_labels_dir = r"D:\coco\Datasets\COCO Dataset.v34-yolov11x-1280.coco\labels\labels"  # Output directory for YOLO labels

# Ensure output directories exist
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# Load COCO annotations
with open(coco_annotations_file, 'r') as f:
    coco_data = json.load(f)

# Define a function to convert COCO bounding box to YOLO format
def coco_to_yolo_bbox(bbox, img_width, img_height):
    x, y, width, height = bbox
    x_center = (x + width / 2) / img_width
    y_center = (y + height / 2) / img_height
    width /= img_width
    height /= img_height
    return x_center, y_center, width, height

# Process each image in the COCO dataset
for image_info in coco_data['images']:
    image_id = image_info['id']
    file_name = image_info['file_name']
    img_width = image_info['width']
    img_height = image_info['height']

    # Construct source and destination image paths
    src_image_path = os.path.join(coco_images_dir, file_name)
    dest_image_path = os.path.join(output_images_dir, file_name)

    # Check if the source image exists
    if not os.path.exists(src_image_path):
        print(f"File not found: {src_image_path}, skipping...")
        continue

    try:
        # Copy the image to the output directory
        Image.open(src_image_path).save(dest_image_path)
    except Exception as e:
        print(f"Error processing image {src_image_path}: {e}")
        continue

    # Open a label file for YOLO format annotations
    label_file_path = os.path.join(output_labels_dir, f"{os.path.splitext(file_name)[0]}.txt")
    with open(label_file_path, 'w') as label_file:
        # Get annotations for the current image
        annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] == image_id]

        for ann in annotations:
            class_id = ann['category_id'] - 1  # Convert COCO 1-based class index to 0-based YOLO index
            bbox = ann['bbox']

            # Skip if the class ID is out of range
            if class_id < 0:
                print(f"Invalid class ID {class_id} for image {file_name}, skipping annotation...")
                continue

            # Convert bounding box to YOLO format
            yolo_bbox = coco_to_yolo_bbox(bbox, img_width, img_height)

            # Write to the label file in YOLO format
            label_file.write(f"{class_id} " + " ".join(map(str, yolo_bbox)) + "\n")

print("Conversion completed!")
