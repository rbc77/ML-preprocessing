import json
import os
import shutil

# Paths
coco_json_path = r"D:/coco/annotations_trainval2017/annotations/instances_train2017.json"
images_folder_path = r"D:\coco\train2017\train2017"
filtered_images_folder = r"D:/coco/filtered_train2017"
filtered_json_path = r"D:/coco/filtered_instances_train2017.json"

# List of category IDs to keep
keep_ids = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 31, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 49, 52, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 89]

# Load COCO JSON
with open(coco_json_path, "r") as f:
    coco_data = json.load(f)

# Filter annotations and categories
filtered_annotations = [annotation for annotation in coco_data["annotations"] if annotation["category_id"] in keep_ids]
filtered_categories = [category for category in coco_data["categories"] if category["id"] in keep_ids]

# Filter images based on annotations
filtered_image_ids = {annotation["image_id"] for annotation in filtered_annotations}
filtered_images = [image for image in coco_data["images"] if image["id"] in filtered_image_ids]

# Debugging: Print the number of filtered images and annotations
print(f"Number of filtered annotations: {len(filtered_annotations)}")
print(f"Number of filtered images: {len(filtered_images)}")

# Save filtered JSON
coco_data["annotations"] = filtered_annotations
coco_data["categories"] = filtered_categories
coco_data["images"] = filtered_images

with open(filtered_json_path, "w") as f:
    json.dump(coco_data, f, indent=4)

print(f"Filtered annotations saved to {filtered_json_path}")

# Create folder for filtered images
os.makedirs(filtered_images_folder, exist_ok=True)

# Copy filtered images
for image_info in filtered_images:
    image_filename = image_info["file_name"]
    src_path = os.path.join(images_folder_path, image_filename)
    dest_path = os.path.join(filtered_images_folder, image_filename)

    # Debugging: Print image paths
    print(f"Processing image: {image_filename}")
    print(f"Source path: {src_path}")
    print(f"Destination path: {dest_path}")

    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied: {image_filename}")
    else:
        print(f"Image not found: {src_path}")

print(f"Filtered images copied to {filtered_images_folder}")
