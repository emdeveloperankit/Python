
# pip install pillow rembg

from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    # Open the input image
    with Image.open(input_path) as img:
        # Remove background
        output = remove(img)
        
        # Save the result to the output path
        output.save(output_path)
        print(f"Background removed successfully. Saved to {output_path}")

# File paths
input_image_path = "input_image.jpg"  # Replace with your image file
output_image_path = "output_image.png"

# Run the background remover
remove_background(input_image_path, output_image_path)
