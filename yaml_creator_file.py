import yaml

# Correct class ID to name mapping
class_id_to_name = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    5: "bus",
    6: "train",
    7: "truck",
    13: "bench",
    14: "bird",
    15: "cat",
    16: "dog",
    17: "horse",
    18: "sheep",
    19: "cow",
    20: "elephant",
    21: "bear",
    22: "zebra",
    23: "giraffe",
    28: "suitcase",
    34: "baseball bat",
    56: "chair",
    57: "couch",
    58: "potted plant",
    59: "bed",
    61: "toilet",
    62: "tv",
    68: "microwave",
    71: "sink",
    72: "refrigerator",
    75: "vase",
    91: "barricade",
    92: "boulder",
    93: "buffalo",
    94: "bull",
    95: "crocodile",
    96: "deer",
    97: "fox",
    98: "goat",
    99: "leopard",
    100: "lion",
    101: "monkey",
    102: "peacock",
    103: "tiger",
    104: "treelog",
    105: "mongoose",
    106: "rabbit",
    107: "snake",
    108: "pig"
}

# Path for the YAML file
yaml_file_path = r"D:\coco\Datasets\Final_Merged_Dataset\data.yaml"

# Correct YAML content structure
yaml_content = {
    "train": r"D:\coco\Datasets\Final_Merged_Dataset\train\images",  # Update with your actual train image path
    "val": r"D:\coco\Datasets\Final_Merged_Dataset\valid\images",    # Update with your actual validation image path
    "test": r"D:\coco\Datasets\Final_Merged_Dataset\test\images",    # Optional: Update with your actual test image path
    "nc": len(class_id_to_name),  # Number of classes
    "names": [class_id_to_name[i] for i in sorted(class_id_to_name.keys())]  # Sorted class names by ID
}

# Write the YAML content to a file
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(yaml_content, yaml_file, default_flow_style=False)

print(f"'data.yaml' file has been created at: {yaml_file_path}")
