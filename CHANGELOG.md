# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-12-23

### Added
- 🎨 **Modern Dark GUI** - CustomTkinter interface with responsive two-column layout
- 🖼️ **Multi-Format Support** - PNG, JPEG, WEBP, BMP, ICO, GIF, TIFF conversion
- 📏 **Image Resizing** - Smart downscaling with LANCZOS filtering and aspect ratio preservation
- 🎚️ **Quality Control** - Compression slider (1-100) for JPEG/WebP optimization
- 📂 **Custom Output Folder** - Optional destination selection for converted images
- ⚡ **Batch Processing** - Convert 50+ images at once with worker thread support
- 📊 **Progress Bar** - Real-time visualization during batch conversions
- 🌙 **Dark Theme** - Professional dark appearance with color-coded sections
- ⌨️ **CLI Interface** - Programmatic API for developers and automation
- 🔄 **Transparency Handling** - Automatic RGBA/Palette → RGB conversion for JPEG
- ✅ **Cross-Platform** - Works on Windows, macOS, and Linux

### Project Setup
- Created comprehensive README.md with usage examples
- Added requirements.txt for easy dependency installation
- Generated .gitignore for version control
- Added MIT License for open-source distribution
- Created AI coding instructions for future development
- Professional file naming (cli.py, gui.py)

### Bug Fixes
- Fixed missing "_converted" suffix in CLI output
- Corrected incomplete transparency handling for JPEG conversion
- Resolved window sizing and layout issues
- Improved responsive layout for various screen sizes

---

## [0.9.0] - 2025-12-22

### Added (Pre-release)
- Basic image conversion functionality
- GUI with dropdown format selection
- CLI module with core conversion functions
- Batch processing support
- Resize and quality features

### Known Issues
- Layout spacing needs improvement
- Window margins missing in some sections
- File naming inconsistencies between CLI and GUI

---

## Upcoming Features

### [1.1.0] - Planned
- [ ] Drag-and-drop support for files
- [ ] Recent files history
- [ ] Custom presets for conversion settings
- [ ] Image preview before conversion
- [ ] Format-specific optimization settings
- [ ] Undo/Redo functionality
- [ ] Settings persistence

### [1.2.0] - Future Considerations
- [ ] Watermarking support
- [ ] Batch image renaming
- [ ] Advanced filters (contrast, brightness, saturation)
- [ ] Animated GIF support with optimization
- [ ] Cloud integration (AWS S3, Google Cloud Storage)
- [ ] Dark/Light theme toggle
- [ ] Multi-language support

---

## Release Notes

### How to Install
```bash
# Clone the repository
git clone https://github.com/aa-humaaan/PixelForge.git
cd PixelForge

# Install dependencies
pip install -r requirements.txt

# Run GUI
python gui.py

# Run CLI
python cli.py
```

### What's New in v1.0.0
The initial release includes a fully-featured, production-ready image converter with both GUI and CLI interfaces. The GUI features a modern dark theme with responsive design, real-time progress tracking, and comprehensive image optimization options.

---

## Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 1.0.0 | 2025-12-23 | ✅ Stable | Initial release |
| 0.9.0 | 2025-12-22 | 🔧 Pre-release | Development preview |

---

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/aa-humaaan/PixelForge).

---

**Made with ❤️ by aa_humaaan (human)**
