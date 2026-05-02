from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
from pathlib import Path


class ImageHandler:
    def __init__(self):
        self.filename = None
        self.pil_image = None
        self.watermark_filename = None
        self.watermark_pil_image = None
        self.watermark_size = 2
        self.watermark_opacity = 0.5


    def get_img_path(self):
        # ask for and save filepath
        user_input = filedialog.askopenfilename()
        self.filename = user_input

    def get_watermark_path(self):
        # ask for and save filepath
        user_input = filedialog.askopenfilename()
        self.watermark_filename = user_input


    def import_image(self):
        #ensure a watermark image was imported first
        if self.watermark_filename is not None:
            # find the image path
            self.get_img_path()
            # open it as a pillow image
            self.pil_image = Image.open(self.filename)
            self.watermark_image()

        else:
            messagebox.showinfo("Error", "No watermark image was uploaded, upload one before you import your main image!")

    def watermark_image(self):
        # ensures a watermark has been uploaded and an image is available for watermarking
        if self.pil_image is not None and self.watermark_filename is not None:
            # determine the watermark size
            if self.watermark_size == 1:
                resize_factor = 50
            elif self.watermark_size == 2:
                resize_factor = 100
            elif self.watermark_size == 3:
                resize_factor = 200
            else:
                resize_factor = 400
            # convert watermark into a pillow image and format the size
            self.watermark_pil_image = Image.open(self.watermark_filename).convert('RGBA')
            aspect_ratio = self.watermark_pil_image.size[0] / self.watermark_pil_image.size[1]
            self.watermark_pil_image = self.watermark_pil_image.resize((resize_factor, int(resize_factor * aspect_ratio)), Image.Resampling.LANCZOS)

            # lower the watermark's opacity
            r, g, b, a = self.watermark_pil_image.split()
            a = a.point(lambda p: int(p * self.watermark_opacity))
            self.watermark_pil_image = Image.merge('RGBA', (r, g, b, a))

            watermark_pos = (25,25)

            # add the watermark to the image
            self.pil_image.convert('RGBA')
            self.pil_image.paste(self.watermark_pil_image, watermark_pos, self.watermark_pil_image)
            self.pil_image.convert('RGB')


    def export_image(self):
        # ensures an image is available to export
        if self.pil_image is not None:
            # downloads the image to the users downloads folder
            download_path = Path.home() / 'Downloads' / 'watermarked_image.png'
            self.pil_image.save(download_path)
            # notifies the user
            messagebox.showinfo("Success", "Image saved to your downloads folder successfully")

        else:
            messagebox.showinfo("Error", "No image was uploaded, so no image could be exported")

    # restarts the image to allow the watermark size to change properly
    def restart_image(self):
        self.pil_image = Image.open(self.filename)
        self.watermark_image()
