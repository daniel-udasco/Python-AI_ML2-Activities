import os
from PIL import Image

bad_images = []
DATASET_DIR = 'dataset'


for root, _, files in os.walk(DATASET_DIR):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(root, file)
            try:
                img = Image.open(path)
                img.verify()
            except Exception as e:
                bad_images.append(path)

print("Bad images found:", len(bad_images))
for b in bad_images:
    print(b)