from PIL import Image
import os
from pathlib import Path

def convert_image(input_path, output_format, max_width=None, quality=85, output_folder=None):
    """Convert a single image to the specified format.
    
    Args:
        input_path: Path to the image file
        output_format: Target format (png, jpg, jpeg, webp, bmp, ico)
        max_width: Maximum width for resizing (optional, in pixels)
        quality: Quality for JPEG/WebP (1-100, default 85)
        output_folder: Output folder path (optional, defaults to same as input)
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize if needed
            if max_width and isinstance(max_width, int):
                img = _resize_image(img, max_width)
            
            # Determine output path
            file_name, _ = os.path.splitext(input_path)
            base_name = os.path.basename(file_name)
            
            if output_folder:
                output_path = os.path.join(output_folder, f"{base_name}_converted.{output_format.lower()}")
            else:
                output_path = f"{file_name}_converted.{output_format.lower()}"
            
            # Convert specifically for RGB modes if saving to JPEG (which doesn't support transparency)
            if output_format.lower() in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Save with quality for JPEG/WebP
            save_kwargs = {}
            if output_format.lower() in ['jpg', 'jpeg', 'webp']:
                save_kwargs['quality'] = min(100, max(1, quality))  # Clamp quality to 1-100
            
            img.save(output_path, output_format.upper(), **save_kwargs)
            size_info = f" ({img.width}x{img.height})" if max_width else ""
            quality_info = f" [Q:{quality}]" if output_format.lower() in ['jpg', 'jpeg', 'webp'] else ""
            print(f"✓ Converted: {os.path.basename(input_path)} → {os.path.basename(output_path)}{size_info}{quality_info}")
            return True
            
    except Exception as e:
        print(f"✗ Error converting {input_path}: {e}")
        return False


def batch_convert_images(folder_path, output_format, file_pattern="*", max_width=None, quality=85, output_folder=None):
    """Convert multiple images in a folder to the specified format.
    
    Args:
        folder_path: Path to folder containing images
        output_format: Target format (png, jpg, jpeg, webp, bmp, ico)
        file_pattern: Wildcard pattern (default: "*" for all files)
        max_width: Maximum width for resizing (optional, in pixels)
        quality: Quality for JPEG/WebP (1-100, default 85)
        output_folder: Output folder path (optional, defaults to same folder)
    
    Returns:
        Tuple of (successful_count, failed_count)
    """
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory")
        return (0, 0)
    
    # Find all image files matching the pattern
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.ico', '.gif', '.tiff'}
    image_files = [f for f in folder.glob(file_pattern) if f.suffix.lower() in image_extensions]
    
    if not image_files:
        print(f"No image files found in {folder_path}")
        return (0, 0)
    
    resize_info = f" (max width: {max_width}px)" if max_width else ""
    quality_info = f" [Q:{quality}]" if output_folder or max_width else ""
    output_info = f" → {output_folder}" if output_folder else ""
    print(f"\nStarting batch conversion of {len(image_files)} image(s) to {output_format.upper()}{resize_info}{quality_info}{output_info}...")
    print("-" * 60)
    
    success_count = 0
    failed_count = 0
    
    for idx, image_path in enumerate(image_files, 1):
        print(f"[{idx}/{len(image_files)}] ", end="")
        if convert_image(str(image_path), output_format, max_width, quality, output_folder):
            success_count += 1
        else:
            failed_count += 1
    
    print("-" * 60)
    print(f"\nBatch conversion complete!")
    print(f"✓ Successful: {success_count}")
    print(f"✗ Failed: {failed_count}")
    return (success_count, failed_count)


def _resize_image(img, max_width):
    """Resize image maintaining aspect ratio."""
    if img.width <= max_width:
        return img  # No resize needed if smaller than max_width
    
    # Calculate new height maintaining aspect ratio
    ratio = max_width / img.width
    new_height = int(img.height * ratio)
    
    return img.resize((max_width, new_height), Image.Resampling.LANCZOS)


# Example Usage:
# Single image conversion
# convert_image("my_photo.jpg", "png")

# Single image with resizing and quality
# convert_image("my_photo.jpg", "webp", max_width=1920, quality=80)

# Single image with custom output folder
# convert_image("my_photo.jpg", "jpg", output_folder="./output")

# Batch conversion - all images in a folder
# batch_convert_images("./images", "webp")

# Batch conversion with all options
# batch_convert_images("./images", "jpg", "*.png", max_width=1080, quality=90, output_folder="./output")