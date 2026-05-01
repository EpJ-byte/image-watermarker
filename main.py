from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from image_handler import ImageHandler

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ih = ImageHandler()


#image preview
def preview_image():
    # checks if there is an image to preview
    if ih.pil_image is not None:

        # create a pillow image and resize it
        display_image = ih.pil_image
        aspect_ratio = display_image.size[0] / display_image.size[1]
        resized_image = display_image.resize((400, int(400 * aspect_ratio)), Image.Resampling.LANCZOS)

        tk_image = ImageTk.PhotoImage(resized_image)

        # display the watermarked image
        image_display.config(image=tk_image)
        image_display.image = tk_image

# image display
image_display = ttk.Label(frm, image='')
image_display.grid(column=0, row=0, columnspan=2)


# import image button
import_button = ttk.Button(frm, text="Import Image", command=ih.import_image)
import_button.grid(column=0, row=1)

# export image button
export_button = ttk.Button(frm, text="Export Image", command=ih.export_image)
export_button.grid(column=1, row=1)

# preview button
image_preview = ttk.Button(frm, text='Preview Image', command=preview_image)
image_preview.grid(column=1, row=2)

# quit button
quit_button = ttk.Button(frm, text='Quit', command=root.destroy)
quit_button.grid(column=0, row=2)

# import watermark image botton
watermark_button = ttk.Button(frm, text='Import watermark image', command=ih.get_watermark_path)
watermark_button.grid(column=0, row=3, columnspan=2)

root.mainloop()

#NOTES FOR NEXT TIME: ensure all of your widgets have the same parent, or they won't render properly