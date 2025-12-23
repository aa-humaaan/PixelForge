import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os
from pathlib import Path
import threading

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ImageConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("Image Converter")
        self.geometry("1000x700")
        self.resizable(True, True)
        self.minsize(800, 600)  # Minimum size for responsive layout
        
        # Store selected output folder
        self.output_folder = None
        
        # Configure main grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Main container with padding
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(1, weight=1)  # Middle content area
        self.main_frame.grid_rowconfigure(2, weight=0)  # Progress and status
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # ===== TOP SECTION: Title =====
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(20, 30))
        
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🎨 Image Converter",
            font=("Segoe UI", 32, "bold"),
            text_color="#00B4FF"
        )
        self.title_label.pack(pady=(0, 8))
        
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="Modern & Fast Image Format Conversion",
            font=("Segoe UI", 13),
            text_color="#A0A0A0"
        )
        self.subtitle_label.pack(pady=(0, 0))
        
        # ===== MIDDLE SECTION: Two-Column Layout =====
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_frame.grid(row=1, column=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        
        # LEFT COLUMN
        self.left_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 15))
        self.left_frame.grid_columnconfigure(0, weight=1)
        
        # Format Section (Left)
        self.format_label = ctk.CTkLabel(
            self.left_frame,
            text="📋 Output Format",
            font=("Segoe UI", 15, "bold"),
            text_color="#00B4FF"
        )
        self.format_label.grid(row=0, column=0, pady=(0, 10), sticky="w")
        
        self.formats = ["PNG", "JPEG", "WEBP", "BMP", "ICO", "GIF", "TIFF"]
        self.format_var = ctk.StringVar(value=self.formats[0])
        self.format_dropdown = ctk.CTkOptionMenu(
            self.left_frame,
            variable=self.format_var,
            values=self.formats,
            font=("Segoe UI", 13),
            button_color="#0078D4",
            button_hover_color="#0066B2",
            dropdown_font=("Segoe UI", 12)
        )
        self.format_dropdown.grid(row=1, column=0, sticky="ew", pady=(0, 25))
        
        # Resize Section (Left)
        self.resize_label = ctk.CTkLabel(
            self.left_frame,
            text="📏 Resize (Optional)",
            font=("Segoe UI", 15, "bold"),
            text_color="#FFB800"
        )
        self.resize_label.grid(row=2, column=0, pady=(0, 10), sticky="w")
        
        self.max_widths = ["No Resize", "640px", "800px", "1080px", "1920px"]
        self.resize_var = ctk.StringVar(value=self.max_widths[0])
        self.resize_dropdown = ctk.CTkOptionMenu(
            self.left_frame,
            variable=self.resize_var,
            values=self.max_widths,
            font=("Segoe UI", 13),
            button_color="#FF9500",
            button_hover_color="#E68400",
            dropdown_font=("Segoe UI", 12)
        )
        self.resize_dropdown.grid(row=3, column=0, sticky="ew", pady=(0, 25))
        
        # Quality Section (Left)
        self.quality_label = ctk.CTkLabel(
            self.left_frame,
            text="⚙️ Quality (JPEG/WebP)",
            font=("Segoe UI", 15, "bold"),
            text_color="#FF9500"
        )
        self.quality_label.grid(row=4, column=0, pady=(0, 10), sticky="w")
        
        # Quality slider with value
        self.quality_slider_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.quality_slider_frame.grid(row=5, column=0, sticky="ew", pady=(0, 10))
        self.quality_slider_frame.grid_columnconfigure(0, weight=1)
        
        self.quality_slider = ctk.CTkSlider(
            self.quality_slider_frame,
            from_=1,
            to=100,
            number_of_steps=99,
            command=self._update_quality_label,
            bg_color="#1E1E1E",
            fg_color="#FF9500",
            progress_color="#E68400"
        )
        self.quality_slider.set(85)
        self.quality_slider.grid(row=0, column=0, sticky="ew")
        
        self.quality_value_label = ctk.CTkLabel(
            self.quality_slider_frame,
            text="85",
            font=("Segoe UI", 12),
            text_color="#FFB800"
        )
        self.quality_value_label.grid(row=0, column=1, padx=(10, 0))
        
        # RIGHT COLUMN
        self.right_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(15, 20))
        self.right_frame.grid_columnconfigure(0, weight=1)
        
        # Output Folder Section (Right)
        self.output_label = ctk.CTkLabel(
            self.right_frame,
            text="📂 Output Folder",
            font=("Segoe UI", 15, "bold"),
            text_color="#9C27B0"
        )
        self.output_label.grid(row=0, column=0, pady=(0, 10), sticky="w")
        
        self.output_folder_btn = ctk.CTkButton(
            self.right_frame,
            text="Select Output Folder",
            command=self.select_output_folder,
            font=("Segoe UI", 12, "bold"),
            height=40,
            corner_radius=8,
            fg_color="#9C27B0",
            hover_color="#7B1FA2",
            text_color="#FFFFFF"
        )
        self.output_folder_btn.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        
        self.output_folder_display = ctk.CTkLabel(
            self.right_frame,
            text="Default: Same folder",
            font=("Segoe UI", 11),
            text_color="#888888"
        )
        self.output_folder_display.grid(row=2, column=0, sticky="w", pady=(0, 25))
        
        # Conversion Buttons (Right)
        self.buttons_label = ctk.CTkLabel(
            self.right_frame,
            text="🚀 Convert",
            font=("Segoe UI", 15, "bold"),
            text_color="#00CC88"
        )
        self.buttons_label.grid(row=3, column=0, pady=(0, 10), sticky="w")
        
        self.single_btn = ctk.CTkButton(
            self.right_frame,
            text="Convert Single Image",
            command=self.convert_file,
            font=("Segoe UI", 12, "bold"),
            height=40,
            corner_radius=8,
            fg_color="#00CC88",
            hover_color="#00AA66",
            text_color="#000000"
        )
        self.single_btn.grid(row=4, column=0, sticky="ew", pady=(0, 12))
        
        self.batch_btn = ctk.CTkButton(
            self.right_frame,
            text="Batch Convert Folder",
            command=self.batch_convert_folder,
            font=("Segoe UI", 12, "bold"),
            height=40,
            corner_radius=8,
            fg_color="#0078D4",
            hover_color="#0066B2",
            text_color="#FFFFFF"
        )
        self.batch_btn.grid(row=5, column=0, sticky="ew", pady=(0, 25))
        
        # ===== BOTTOM SECTION: Progress & Status =====
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=0, sticky="ew", pady=(20, 20))
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        
        # Progress Bar
        self.progress_label = ctk.CTkLabel(
            self.bottom_frame,
            text="Progress",
            font=("Segoe UI", 11, "bold"),
            text_color="#A0A0A0"
        )
        self.progress_label.grid(row=0, column=0, pady=(0, 8), padx=(20, 20), sticky="w")
        
        self.progress_bar = ctk.CTkProgressBar(
            self.bottom_frame,
            fg_color="#333333",
            progress_color="#00B4FF"
        )
        self.progress_bar.set(0)
        self.progress_bar.grid(row=1, column=0, sticky="ew", padx=(20, 20), pady=(0, 15))
        
        # Status Frame
        self.status_frame = ctk.CTkFrame(self.bottom_frame, fg_color="#1E1E1E", corner_radius=10)
        self.status_frame.grid(row=2, column=0, sticky="ew", padx=(20, 20))
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Ready to convert images",
            font=("Segoe UI", 11),
            text_color="#A0A0A0"
        )
        self.status_label.pack(padx=15, pady=12)

    def convert_file(self):
        """Convert a single image file."""
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.webp *.bmp *.ico *.gif *.tiff")]
        )
        
        if not file_path:
            return

        target_format = self.format_var.get()
        max_width = self._parse_max_width(self.resize_var.get())
        quality = int(self.quality_slider.get())

        try:
            self.progress_bar.set(0.5)
            with Image.open(file_path) as img:
                # Resize if needed
                if max_width:
                    img = self._resize_image(img, max_width)
                
                # Handle transparency
                if target_format.lower() in ['jpeg', 'jpg'] and img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Determine output path
                file_root, _ = os.path.splitext(file_path)
                if self.output_folder:
                    output_path = os.path.join(self.output_folder, os.path.basename(file_root) + f"_converted.{target_format.lower()}")
                else:
                    output_path = f"{file_root}_converted.{target_format.lower()}"
                
                # Save with quality for JPEG/WebP
                save_kwargs = {}
                if target_format.lower() in ['jpg', 'jpeg', 'webp']:
                    save_kwargs['quality'] = min(100, max(1, int(quality)))  # Clamp quality to 1-100
                
                img.save(output_path, target_format.upper(), **save_kwargs)
                self.progress_bar.set(1.0)
                self.status_label.configure(text=f"✓ Converted: {os.path.basename(output_path)}")
                messagebox.showinfo("Success", f"Image saved at:\n{output_path}")
                self.progress_bar.set(0)
            
        except Exception as e:
            self.progress_bar.set(0)
            self.status_label.configure(text=f"✗ Error: {str(e)[:50]}")
            messagebox.showerror("Error", f"Failed to convert:\n{e}")

    def batch_convert_folder(self):
        """Convert multiple images in a folder."""
        folder_path = filedialog.askdirectory(title="Select Folder with Images")
        
        if not folder_path:
            return
        
        target_format = self.format_var.get()
        max_width = self._parse_max_width(self.resize_var.get())
        quality = int(self.quality_slider.get())
        
        folder = Path(folder_path)
        image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.ico', '.gif', '.tiff'}
        image_files = [f for f in folder.glob("*") if f.suffix.lower() in image_extensions]
        
        if not image_files:
            messagebox.showwarning("No Images", f"No image files found in:\n{folder_path}")
            return
        
        self.status_label.configure(text=f"⏳ Converting {len(image_files)} images...")
        self.batch_btn.configure(state="disabled")
        self.single_btn.configure(state="disabled")
        self.progress_bar.set(0)
        
        batch_thread = threading.Thread(
            target=self._batch_convert_worker,
            args=(image_files, target_format, folder_path, max_width, quality)
        )
        batch_thread.daemon = True
        batch_thread.start()

    def _batch_convert_worker(self, image_files, target_format, folder_path, max_width=None, quality=85):
        """Worker function for batch conversion (runs in separate thread)."""
        success_count = 0
        failed_count = 0
        total = len(image_files)
        
        for idx, image_path in enumerate(image_files, 1):
            try:
                with Image.open(image_path) as img:
                    # Resize if needed
                    if max_width:
                        img = self._resize_image(img, max_width)
                    
                    # Handle transparency
                    if target_format.lower() in ['jpeg', 'jpg'] and img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # Determine output path
                    file_root, _ = os.path.splitext(str(image_path))
                    if self.output_folder:
                        output_path = os.path.join(self.output_folder, os.path.basename(file_root) + f"_converted.{target_format.lower()}")
                    else:
                        output_path = f"{file_root}_converted.{target_format.lower()}"
                    
                    # Save with quality
                    save_kwargs = {}
                    if target_format.lower() in ['jpg', 'jpeg', 'webp']:
                        save_kwargs['quality'] = min(100, max(1, int(quality)))  # Clamp quality to 1-100
                    
                    img.save(output_path, target_format.upper(), **save_kwargs)
                    success_count += 1
                    
            except Exception:
                failed_count += 1
            
            # Update progress bar
            progress = idx / total
            self.progress_bar.set(progress)
        
        message = f"Batch Conversion Complete!\n\n"
        message += f"✓ Successful: {success_count}/{total}\n"
        message += f"✗ Failed: {failed_count}/{total}\n"
        message += f"\nFiles saved to:\n{self.output_folder if self.output_folder else folder_path}"
        
        self.status_label.configure(
            text=f"✓ Batch complete: {success_count} successful, {failed_count} failed"
        )
        self.batch_btn.configure(state="normal")
        self.single_btn.configure(state="normal")
        messagebox.showinfo("Batch Conversion", message)

    def _parse_max_width(self, width_str):
        """Parse max width from dropdown string (e.g., '1920px' -> 1920)."""
        if width_str == "No Resize" or not width_str:
            return None
        return int(width_str.replace("px", ""))

    def _resize_image(self, img, max_width):
        """Resize image maintaining aspect ratio."""
        if img.width <= max_width:
            return img  # No resize needed if smaller than max_width
        
        # Calculate new height maintaining aspect ratio
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        
        return img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    def _update_quality_label(self, value):
        """Update quality value display when slider changes."""
        self.quality_value_label.configure(text=str(int(float(value))))
    
    def select_output_folder(self):
        """Select output folder for converted images."""
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder = folder
            folder_name = os.path.basename(folder) or folder
            self.output_folder_display.configure(text=f"📂 {folder_name}", text_color="#00CC88")
        else:
            self.output_folder = None
            self.output_folder_display.configure(text="Default: Same folder as original", text_color="#888888")


if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()