import os
import cv2
import numpy as np
from collections import defaultdict
import hashlib

# Paths to images and labels
image_folder = r"D:\coco\Datasets\bull_final\train\images"  # Change path accordingly
label_folder = r"D:\coco\Datasets\bull_final\train\labels"

# Track deleted images and labels
corrupt_count = 0
duplicate_count = 0

# Store image hashes to detect duplicates
hashes = defaultdict(list)

def dhash(image, size=8):
    """Generate a difference hash (dHash) for an image."""
    resized = cv2.resize(image, (size + 1, size))
    diff = resized[:, 1:] > resized[:, :-1]
    return hashlib.sha256(diff.tobytes()).hexdigest()

# **Step 1: Detect and remove corrupted images**
for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    label_path = os.path.join(label_folder, filename.replace(".jpg", ".txt"))

    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Corrupted Image")

        # Compute hash and store it for duplicate detection
        img_hash = dhash(img)
        hashes[img_hash].append(image_path)

    except Exception as e:
        print(f"❌ Corrupted Image Found: {image_path} (Deleting)")
        os.remove(image_path)
        if os.path.exists(label_path):
            os.remove(label_path)  # Remove corresponding label
        corrupt_count += 1

# **Step 2: Detect and remove duplicate images**
for img_hash, paths in hashes.items():
    if len(paths) > 1:
        # Keep first image, delete the rest
        for duplicate in paths[1:]:
            label_path = os.path.join(label_folder, os.path.basename(duplicate).replace(".jpg", ".txt"))
            print(f"🗑️ Duplicate Image Found: {duplicate} (Deleting)")
            os.remove(duplicate)
            if os.path.exists(label_path):
                os.remove(label_path)
            duplicate_count += 1

# **Final Report**
if corrupt_count == 0 and duplicate_count == 0:
    print("✅ No duplicate or corrupted images found.")
else:
    print(f"✅ Cleanup complete: {corrupt_count} corrupted and {duplicate_count} duplicate images (and labels) removed.")
