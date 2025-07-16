import json

# Path to your JSON annotation file
json_path = r"D:/coco/annotations_trainval2017/annotations/instances_train2017.json"

# Load the JSON file
with open(json_path, "r") as f:
    coco_data = json.load(f)

# Extract categories
categories = coco_data["categories"]

# Save the IDs and names to a text file
output_file = "categories_output.txt"
with open(output_file, "w") as file:
    for category in categories:
        file.write(f"ID: {category['id']}, Name: {category['name']}\n")

print(f"Category data saved to {output_file}")
