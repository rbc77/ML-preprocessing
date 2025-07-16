import json

# Path to the merged JSON file
merged_dataset_path = r"D:\coco\final_merged_dataset\val\merged_coco.json" #dont forget to change the path to the coco.json file you want to check. by RBC

# Load the merged dataset
with open(merged_dataset_path, 'r') as f:
    merged_coco = json.load(f)

# Check the number of entries
num_images = len(merged_coco["images"])
num_annotations = len(merged_coco["annotations"])
num_categories = len(merged_coco["categories"])

print(f"Number of Images: {num_images}")
print(f"Number of Annotations: {num_annotations}")
print(f"Number of Categories: {num_categories}")