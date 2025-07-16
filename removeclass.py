import json

# Load the original COCO JSON file
coco_json_path = r"D:/coco/annotations_trainval2017/annotations/instances_train2017.json"  # Update with the path to your JSON file
with open(coco_json_path, "r") as f:
    coco_data = json.load(f)

# List of category IDs to keep (update this list with the categories you need)
keep_ids = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 31, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 49, 52, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 89]    # Example: IDs for 'person', 'bicycle', and 'car' (you can replace these)

# Filter annotations to keep only those with desired category IDs
filtered_annotations = [
    annotation for annotation in coco_data["annotations"] if annotation["category_id"] in keep_ids
]

# Filter categories to keep only the ones matching the desired IDs
filtered_categories = [
    category for category in coco_data["categories"] if category["id"] in keep_ids
]

# Update the COCO data structure
coco_data["annotations"] = filtered_annotations
coco_data["categories"] = filtered_categories

# Save the filtered dataset to a new JSON file
filtered_json_path = r"filtered_instances_train2017.json"  # Output file path
with open(filtered_json_path, "w") as f:
    json.dump(coco_data, f, indent=4)

print(f"Filtered dataset saved to {filtered_json_path}")
