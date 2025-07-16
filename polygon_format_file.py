import os

# Define paths
labels_folder = r"D:\coco\Datasets\bull_final\train\labels"  # Replace with your actual labels directory
output_file = "complex_labels_train_bull.txt"  # File to store polygon labels

# Open the output file to store polygon format labels
with open(output_file, "w") as out_file:
    for label_file in os.listdir(labels_folder):
        if label_file.endswith(".txt"):  # Process only text files
            label_path = os.path.join(labels_folder, label_file)

            with open(label_path, "r") as f:
                lines = f.readlines()

            complex_labels = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 5:  # More than one bounding box (i.e., a polygon)
                    complex_labels.append(line.strip())

            # If the file contains complex labels, save them to the new file
            if complex_labels:
                out_file.write(f"File: {label_file}\n")
                out_file.write("\n".join(complex_labels) + "\n\n")

print("Complex labels identified and saved to 'complex_labels.txt'.")
