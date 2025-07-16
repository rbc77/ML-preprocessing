import os

# Set dataset paths
labels_dir = r"D:\coco\Datasets\barricade\train\labels"  # Change this path
valid_class_ids = set(range(48))  # Class IDs from 0 to 47

# Get all label files
label_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]

# Store corrupt labels
corrupt_labels = []

print("\n🔍 Scanning Label Files for Errors...\n")

for label_file in label_files:
    label_path = os.path.join(labels_dir, label_file)

    with open(label_path, "r") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        parts = line.strip().split()

        # Case 1: Complex labels (polygon data)
        if len(parts) != 5:
            corrupt_labels.append(f"❌ {label_file} (Line {line_number}): Complex label detected.")
            continue

            # Extract values
        try:
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])

            # Case 2: Invalid class ID
            if class_id not in valid_class_ids:
                corrupt_labels.append(f"❌ {label_file} (Line {line_number}): Invalid class ID {class_id}.")
                continue

            # Case 3: Bounding box values out of range
            if not (0 <= x_center <= 1 and 0 <= y_center <= 1 and 0 <= width <= 1 and 0 <= height <= 1):
                corrupt_labels.append(
                    f"❌ {label_file} (Line {line_number}): Invalid bounding box values [{x_center}, {y_center}, {width}, {height}].")

        except ValueError:
            corrupt_labels.append(f"❌ {label_file} (Line {line_number}): Non-numeric value detected.")

# Print final report
if corrupt_labels:
    print("\n🔴 Corrupt Labels Found:\n")
    for error in corrupt_labels:
        print(error)
    print(f"\n❗ Total Corrupt Labels: {len(corrupt_labels)}")
else:
    print("\n✅ No corrupt labels found. Dataset is clean.")
