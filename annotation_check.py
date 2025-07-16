import os

# Path to the merged dataset output folder
merged_dataset_dir = 'D:/coco/merged_dataset_output2'  # Update with your path

# Subfolders to check in the merged dataset
subfolders = ['test', 'train', 'valid']

# File extension for annotation files (assuming JSON, update if needed)
annotation_extension = '.json'

# Initialize count for annotations
merged_counts = {folder: 0 for folder in subfolders}

# Count annotation files in each subfolder
for folder in subfolders:
    subfolder_path = os.path.join(merged_dataset_dir, folder)

    if os.path.exists(subfolder_path):
        annotation_files = [f for f in os.listdir(subfolder_path) if f.endswith(annotation_extension)]
        merged_counts[folder] += len(annotation_files)

# Print combined counts
print("Counts from Merged Dataset Output:")
for folder in subfolders:
    print(f"{folder.capitalize()}: Annotations: {merged_counts[folder]} files")

# Print overall total
total_annotations = sum(merged_counts.values())
print(f"\nTotal Annotations Across All Subfolders: {total_annotations} files")

# Compare with original dataset counts
original_counts = {'test': 17, 'train': 18, 'valid': 18}  # Expected counts from your original dataset
if merged_counts == original_counts:
    print("\n✅ The merged annotations match the original dataset counts!")
else:
    print("\n❌ The merged annotations do NOT match the original dataset counts.")
    print("Differences:")
    for folder in subfolders:
        if merged_counts[folder] != original_counts[folder]:
            print(f"  {folder.capitalize()}: Expected {original_counts[folder]}, Found {merged_counts[folder]}")
