# ⚒️ PixelForge

> **A powerful, modern dual-interface image format converter with CLI and GUI**

---

## ✨ Features

- 🖼️ **Multiple Format Support** - PNG, JPEG, WEBP, BMP, ICO, GIF, TIFF
- 📏 **Smart Resizing** - Scale down images with aspect ratio preservation (LANCZOS filtering)
- 🎚️ **Quality Control** - Compression slider (1-100) for JPEG/WebP optimization
- 📂 **Custom Output** - Choose where to save converted images
- ⚡ **Batch Processing** - Convert 50+ images at once with progress tracking
- 🎯 **Transparency Handling** - Automatic RGBA/Palette → RGB conversion for JPEG
- 🌙 **Modern Dark UI** - Beautiful CustomTkinter interface with responsive two-column layout
- ⌨️ **CLI & GUI** - Choose between command-line or graphical interface

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Required packages:
  ```bash
  pip install pillow customtkinter
  ```

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📖 Usage

### 🖥️ GUI Mode (Recommended for Users)

Launch the beautiful graphical interface:

```bash
python gui.py
```

**Features:**
- Intuitive two-column layout
- Format dropdown selector
- Resize presets (640px, 800px, 1080px, 1920px)
- Real-time quality slider
- Output folder picker
- Single image or batch conversion
- Live progress bar with status updates

### ⌨️ CLI Mode (For Developers & Automation)

Convert images programmatically:

```python
from cli import convert_image, batch_convert_images

# Single image conversion
convert_image("photo.png", "webp")

# With resizing (max width 1920px)
convert_image("photo.png", "webp", max_width=1920)

# With quality control (JPEG/WebP)
convert_image("photo.jpg", "webp", quality=80)

# All options
convert_image("photo.jpg", "webp", max_width=1920, quality=85, output_folder="./output")

# Batch processing
success, failed = batch_convert_images("./images", "jpg")

# Batch with options
success, failed = batch_convert_images(
    "./images", 
    "png", 
    "*.webp",  # Pattern filter
    max_width=1080,
    quality=90,
    output_folder="./output"
)
```

---

## 📋 Supported Formats

| Format | Input | Output | Notes |
|--------|-------|--------|-------|
| PNG | ✅ | ✅ | Lossless, supports transparency |
| JPEG | ✅ | ✅ | Quality slider available |
| WEBP | ✅ | ✅ | Quality slider available |
| BMP | ✅ | ✅ | Basic bitmap format |
| ICO | ✅ | ✅ | Windows icon format |
| GIF | ✅ | ✅ | Animated support |
| TIFF | ✅ | ✅ | High-quality format |

---

## ⚙️ Configuration

### Quality Settings
- **Default:** 85 (recommended balance)
- **High Quality:** 90-100 (larger files, best appearance)
- **Compressed:** 70-80 (smaller files, acceptable quality)
- **Note:** Only applies to JPEG and WebP formats

### Resize Behavior
- Images smaller than max_width are **not upscaled**
- Aspect ratio is **always preserved**
- Uses LANCZOS resampling for high-quality results

### Output Path
- **With output folder:** All files saved to selected folder
- **Without output folder:** Files saved next to originals with `_converted` suffix

---

## 🎯 Use Cases

✅ **Batch convert PNG screenshots to WEBP** for better compression  
✅ **Resize bulk product images** for e-commerce  
✅ **Convert JPEG to PNG** while preserving quality  
✅ **Optimize images for web** with quality/size control  
✅ **Automate image processing** in CI/CD pipelines (CLI mode)  

---

## 📦 Project Structure

```
.
├── gui.py                          # Modern GUI application
├── cli.py                          # Command-line interface
├── README.md                       # This file
├── requirements.txt                # Python dependencies

```

---

## 🔧 File Details

### `gui.py`
- **Type:** Standalone GUI Application
- **Framework:** CustomTkinter (modern dark theme)
- **Interface:** Responsive two-column layout
- **Features:** File dialog, progress bar, status display
- **Run:** `python gui.py`

### `cli.py`
- **Type:** Python Module (importable)
- **Framework:** PIL/Pillow
- **Interface:** Function-based API
- **Features:** Batch processing, flexible parameters
- **Run:** `python cli.py` or `from cli import convert_image`

---

## 💡 Examples

### Example 1: Convert Single PNG to WEBP
```python
from cli import convert_image
convert_image("screenshot.png", "webp")
# Output: screenshot_converted.webp
```

### Example 2: Batch Resize & Compress JPEGs
```python
from cli import batch_convert_images
success, failed = batch_convert_images(
    "./photos",
    "jpg",
    max_width=1080,
    quality=85
)
print(f"✓ Success: {success}, ✗ Failed: {failed}")
```

### Example 3: Convert PNG to JPEG (Auto RGB)
```python
from cli import convert_image
# Automatically converts RGBA→RGB (JPEG incompatibility)
convert_image("transparent.png", "jpeg", quality=90)
# Output: transparent_converted.jpeg
```

---

## 🐛 Troubleshooting

**Issue:** GUI doesn't start
- **Solution:** Ensure CustomTkinter is installed: `pip install customtkinter`

**Issue:** "No module named 'PIL'"
- **Solution:** Install Pillow: `pip install pillow`

**Issue:** JPEG conversion fails with transparent images
- **Solution:** Automatic RGBA→RGB conversion is applied. If still failing, check file permissions.

**Issue:** Quality slider has no effect
- **Solution:** Quality only applies to JPEG and WebP formats. PNG/BMP/ICO are lossless.

**Issue:** Images are upscaled incorrectly
- **Solution:** Images smaller than max_width are not upscaled by design. Only downscaling occurs.

---

## 📝 Requirements

```
pillow>=9.0.0
customtkinter>=5.0.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🎓 Development

This project is designed with extensibility in mind:

**To add a new format:**
1. Add format name to `formats` list in `gui.py`
2. Ensure PIL/Pillow supports it

**To add a new feature:**
1. Implement in `cli.py` first (core logic)
2. Integrate UI in `gui.py` (if needed)
3. Test both CLI and GUI interfaces
4. Update documentation

---

## 📄 License

Open source and free to use. Feel free to modify and distribute!

---

## 👨‍💻 Author

**aa_humaaan** (human)

*Built with ❤️ for developers and content creators*

---

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to create an issue or submit a pull request!

---

## ⭐ If you find this useful, please give it a star!

Made with passion for the open-source community. Happy converting! 🎨✨


