from flask import current_app, url_for
import os

def rename_waste_image(waste, new_name):
    old_image_filename = f"{waste}.png"
    new_image_filename = f"{new_name}.png"
    old_image_path = os.path.join(current_app.static_folder, "uploads", "Wastes", old_image_filename)
    new_image_path = os.path.join(current_app.static_folder, "uploads", "Wastes", new_image_filename)
    os.rename(old_image_path, new_image_path)
