### HELPER FUNCTION 2###
### CONVERT PDF TO IMAGES ###
import os
from pdf2image import convert_from_path
from PIL import Image

# ============= PATH CONFIGURATION =============
# Get the current working directory instead of script directory
script_dir = os.getcwd()

# Define input and output directories
PDF_INPUT_DIR = os.path.join(script_dir, 'process_pdfs')
IMAGE_OUTPUT_DIR = os.path.join(script_dir, 'output_images')

# Create directories if they don't exist
os.makedirs(PDF_INPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)

# ============= PDF TO IMAGE CONVERSION =============
def pdf_to_images(pdf_path, output_base_folder):
    # Extract the base name of the PDF file (without extension)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create a directory named after the PDF file
    output_folder = os.path.join(output_base_folder, pdf_name)
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Save each page as an image in the output folder
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
        print(f"Saved: {image_path}")
    
    # Combine images into one
    combine_images(image_paths, os.path.join(output_base_folder, f"{pdf_name}_combined.png"))

def combine_images(image_paths, output_path):
    """Combine multiple images vertically into a single image."""
    images = [Image.open(img_path) for img_path in image_paths]
    
    # Calculate the total height and max width
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)
    
    # Create a new blank image with the calculated dimensions
    combined_image = Image.new('RGB', (max_width, total_height))
    
    # Paste each image into the combined image
    y_offset = 0
    for img in images:
        combined_image.paste(img, (0, y_offset))
        y_offset += img.height
    
    # Save the combined image
    combined_image.save(output_path)
    print(f"Combined image saved: {output_path}")

# ============= MAIN EXECUTION =============
def main():
    print(f"Processing PDFs from: {PDF_INPUT_DIR}")
    print(f"Saving images to: {IMAGE_OUTPUT_DIR}")
    
    # Process each PDF in the directory
    pdf_files = [f for f in os.listdir(PDF_INPUT_DIR) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the input directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_file in pdf_files:
        print(f"\nProcessing: {pdf_file}")
        pdf_path = os.path.join(PDF_INPUT_DIR, pdf_file)
        pdf_to_images(pdf_path, IMAGE_OUTPUT_DIR)

if __name__ == "__main__":
    main()
