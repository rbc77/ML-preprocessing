# Correct class ID to name mapping
class_id_to_name = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    4: "chair",
    5: "bus",
    6: "train",
    7: "truck",
    8: "couch",
    9: "potted plant",
    10: "bed",
    11: "toilet",
    12: "tv",
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
    24: "microwave",
    25: "sink",
    26: "refrigerator",
    27: "vase",
    28: "suitcase",
    29: "barricade",
    30: "boulder",
    31: "buffalo",
    32: "bull",
    33: "crocodile",
    34: "baseball bat",
    35: "deer",
    36: "fox",
    37: "goat",
    38: "leopard",
    39: "lion",
    40: "monkey",
    41: "peacock",
    42: "tiger",
    43: "treelog",
    44: "mongoose",
    45: "rabbit",
    46: "snake",
    47: "pig"
}

# Path to save the file
file_path = r"D:\coco\Datasets\Final_Merged_Dataset\class_id_to_name.txt"

# Writing class ID and name to the file
with open(file_path, 'w') as f:
    for class_id, class_name in sorted(class_id_to_name.items()):
        f.write(f"{class_id}: {class_name}\n")

print(f"File has been created at: {file_path}")
