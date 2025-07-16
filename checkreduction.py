import json

# Paths to the original and filtered JSON files
original_json_path = r"D:/coco/annotations_trainval2017/annotations/instances_train2017.json"
filtered_json_path = r"D:/coco/filtered_instances_train2017.json"

# List of category IDs to keep
keep_ids = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            27, 28, 31, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 49, 52, 62, 63, 64, 65, 67, 70,
            72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 89]

# Load original COCO JSON
with open(original_json_path, "r") as f:
    original_data = json.load(f)

# Load filtered COCO JSON
with open(filtered_json_path, "r") as f:
    filtered_data = json.load(f)

# Step 1: Check the number of images in the filtered JSON
print(f"Number of images in the filtered JSON: {len(filtered_data['images'])}")

# Step 2: Check that all annotations in the filtered JSON reference valid image IDs
filtered_image_ids = {image['id'] for image in filtered_data['images']}
annotations_valid = all(ann['image_id'] in filtered_image_ids for ann in filtered_data['annotations'])
print(f"All annotations reference valid images: {annotations_valid}")

# Step 3: Check that the filtered annotations only use valid category IDs
filtered_category_ids = {category["id"] for category in filtered_data["categories"]}
annotations_valid_categories = all(ann["category_id"] in filtered_category_ids for ann in filtered_data["annotations"])
print(f"All annotations use valid category IDs: {annotations_valid_categories}")

# Step 4: Verify that the number of images matches the original dataset for the kept categories
# Find the image IDs in the original dataset that correspond to the desired categories
original_image_ids_for_kept_categories = {
    ann["image_id"] for ann in original_data["annotations"] if ann["category_id"] in keep_ids
}
print(f"Number of images in the original dataset matching filtered categories: {len(original_image_ids_for_kept_categories)}")

# Check if the number of filtered images matches the number of relevant images in the original dataset
filtered_image_count_matches = len(filtered_image_ids) == len(original_image_ids_for_kept_categories)
print(f"Filtered image count matches relevant images in the original dataset: {filtered_image_count_matches}")

# Step 5: Check if all filtered images belong to kept categories
filtered_annotation_category_ids = {ann["category_id"] for ann in filtered_data["annotations"]}
category_ids_match = filtered_annotation_category_ids.issubset(set(keep_ids))
print(f"All filtered annotations belong to kept categories: {category_ids_match}")

# Step 6: Manual Verification Prompt
print("\nManual verification is recommended. Randomly inspect some images in the filtered_train2017 folder to ensure they match the desired classes.")
