from PIL import Image
import os

images = []
for img in sorted(os.listdir(), key=lambda x: (int(x.split('.')[0]) if x.split('.')[0].isdigit() else float('inf'))):
    if img.lower().endswith(('.jpeg', '.jpg', '.png')):
        print(f"Adding {img}")
        images.append(Image.open(img))

if images:
    images[0].save('output.pdf', save_all=True, append_images=images[1:], resolution=100.0)
    print("PDF generated successfully.")
else:
    print("No images found.")
