import json
import os
import shutil
from pathlib import Path
from tqdm import tqdm

# Path to COCO dataset and where to store YOLO annotations
COCO_DIR = r'D:\coco\coc dataset'  # Update to your COCO dataset directory
OUTPUT_DIR = r'D:\coco\Datasets\coco_final\valid\labels'  # Update to your desired output directory

# COCO-to-YOLO class name mapping
COCO_TO_YOLO_CLASSES = {
    'person': 0, 'bicycle': 1, 'car': 2, 'motorcycle': 3, 'airplane': 4,
    'bus': 5, 'train': 6, 'truck': 7, 'boat': 8, 'traffic light': 9,
    'fire hydrant': 10, 'stop sign': 11, 'parking meter': 12,
    'bench': 13, 'bird': 14, 'cat': 15, 'dog': 16, 'horse': 17,
    'sheep': 18, 'cow': 19, 'elephant': 20, 'bear': 21, 'zebra': 22,
    'giraffe': 23, 'backpack': 24, 'umbrella': 25, 'handbag': 26, 'tie': 27,
    'suitcase': 28, 'frisbee': 29, 'skis': 30, 'snowboard': 31, 'sports ball': 32,
    'kite': 33, 'baseball bat': 34, 'baseball glove': 35, 'skateboard': 36, 'surfboard': 37,
    'tennis racket': 38, 'bottle': 39, 'wine glass': 40, 'cup': 41, 'fork': 42, 'knife': 43,
    'spoon': 44, 'bowl': 45, 'banana': 46, 'apple': 47, 'sandwich': 48, 'orange': 49,
    'broccoli': 50, 'carrot': 51, 'hot dog': 52, 'pizza': 53, 'donut': 54, 'cake': 55,
    'chair': 56, 'couch': 57, 'potted plant': 58, 'bed': 59, 'dining table': 60,
    'toilet': 61, 'tv': 62, 'laptop': 63, 'mouse': 64, 'remote': 65, 'keyboard': 66,
    'cell phone': 67, 'microwave': 68, 'oven': 69, 'toaster': 70, 'sink': 71,
    'refrigerator': 72, 'book': 73, 'clock': 74, 'vase': 75, 'scissors': 76, 'teddy bear': 77,
    'hair drier': 78, 'toothbrush': 79

}

# Create output directories
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Load COCO annotations
with open(os.path.join(COCO_DIR, 'annotations/instances_val2017.json')) as f:
    coco_data = json.load(f)

# Map categories to YOLO IDs
category_id_map = {category['id']: category['name'] for category in coco_data['categories']}


# Function to convert COCO annotations to YOLO format
def convert_coco_to_yolo(coco_data, output_dir):
    for image_info in tqdm(coco_data['images'], desc="Processing Images"):
        image_id = image_info['id']
        image_name = image_info['file_name']
        image_width = image_info['width']
        image_height = image_info['height']

        # Initialize the annotation list for this image
        yolo_annotations = []

        # Loop through annotations and convert to YOLO format
        for annotation in coco_data['annotations']:
            if annotation['image_id'] == image_id:
                # Extract class name and map to YOLO ID
                class_name = category_id_map[annotation['category_id']]
                if class_name in COCO_TO_YOLO_CLASSES:
                    yolo_class_id = COCO_TO_YOLO_CLASSES[class_name]
                else:
                    continue  # Skip classes not in COCO_TO_YOLO_CLASSES

                # Get bounding box [x, y, width, height] from COCO
                x, y, width, height = annotation['bbox']

                # Normalize bounding box coordinates
                center_x = (x + width / 2) / image_width
                center_y = (y + height / 2) / image_height
                norm_width = width / image_width
                norm_height = height / image_height

                # Append YOLO annotation
                yolo_annotations.append(f"{yolo_class_id} {center_x} {center_y} {norm_width} {norm_height}")

        # Save annotations to a text file
        if yolo_annotations:
            with open(os.path.join(output_dir, f"{image_name.split('.')[0]}.txt"), 'w') as label_file:
                label_file.write("\n".join(yolo_annotations))


# Convert the COCO dataset
convert_coco_to_yolo(coco_data, OUTPUT_DIR)

print("Conversion Complete!")
