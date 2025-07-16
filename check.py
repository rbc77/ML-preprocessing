import json

# Path to the filtered JSON file
filtered_json_path = r"D:\coco\filtered_instances_train2017.json"

# Load the filtered dataset
with open(filtered_json_path, "r") as f:
    coco_data = json.load(f)

# Get unique category IDs in annotations
remaining_category_ids = set(annotation["category_id"] for annotation in coco_data["annotations"])

# Get the names of the remaining categories
remaining_categories = [category for category in coco_data["categories"] if category["id"] in remaining_category_ids]

print("Remaining Category IDs:", remaining_category_ids)
print("Remaining Categories:")
for category in remaining_categories:
    print(f"ID: {category['id']}, Name: {category['name']}")
