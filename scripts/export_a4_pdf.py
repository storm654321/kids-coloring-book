import os
import sys
from PIL import Image, ImageOps

def create_a4_coloring_pdf(image_path: str, output_pdf_path: str, orientation: str = "landscape"):
    """
    Fit a coloring image neatly onto a standard A4 page (300 DPI) and save as PDF.
    A4 at 300 DPI:
      - Portrait: 2480 x 3508 pixels
      - Landscape: 3508 x 2480 pixels
    """
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return False

    img = Image.open(image_path).convert("RGB")

    if orientation == "landscape":
        a4_w, a4_h = 3508, 2480
    else:
        a4_w, a4_h = 2480, 3508

    # Margin: 120 pixels (~1cm at 300 DPI)
    margin = 120
    max_w = a4_w - 2 * margin
    max_h = a4_h - 2 * margin

    # Resize keeping aspect ratio
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)

    # Create pure white A4 canvas
    canvas = Image.new("RGB", (a4_w, a4_h), (255, 255, 255))

    # Center image
    offset_x = (a4_w - img.width) // 2
    offset_y = (a4_h - img.height) // 2
    canvas.paste(img, (offset_x, offset_y))

    # Save as high-resolution PDF
    canvas.save(output_pdf_path, "PDF", resolution=300.0)
    print(f"Successfully created printable A4 PDF: {output_pdf_path}")
    return True

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(os.path.dirname(current_dir), "assets")
    
    # Default example test
    test_img = os.path.join(assets_dir, "example_coloring.jpg")
    output_pdf = os.path.join(assets_dir, "kirby_coloring_page_A4.pdf")
    
    input_file = sys.argv[1] if len(sys.argv) > 1 else test_img
    output_file = sys.argv[2] if len(sys.argv) > 2 else output_pdf
    
    create_a4_coloring_pdf(input_file, output_file, orientation="landscape")
