import os

# Define paths
labels_folder = r"D:\coco\Datasets\coco_final\valid\labels"  # Replace with your actual labels directory

# Initialize total count
total_polygons = 0
found_polygons = False  # Flag to check if any polygons exist

# Loop through label files
for label_file in os.listdir(labels_folder):
    if label_file.endswith(".txt"):  # Process only text files
        label_path = os.path.join(labels_folder, label_file)

        with open(label_path, "r") as f:
            lines = f.readlines()

        polygon_count = 0
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 5:  # More than 5 values means it's a polygon format
                polygon_count += 1

        # If polygons are found in the file, display count
        if polygon_count > 0:
            found_polygons = True
            total_polygons += polygon_count
            print(f"File: {label_file} ➝ {polygon_count} polygon(s) found.")

# Display total polygons
if found_polygons:
    print(f"\n✅ Total polygon annotations found: {total_polygons}")
else:
    print("\n⚠️ No polygon format found in any label file.")
