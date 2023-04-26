import time
from app.openai.openai_waste import WasteOpenAI
from flask import current_app, url_for
import os


def rename_waste_image(waste, new_name):
    """Renomme l'image associée à un déchet avec un nouveau nom.

    Args:
        waste (str): le nom du déchet dont l'image doit être renommée.
        new_name (str): le nouveau nom de l'image.

    Returns:
        None
    """
    if os.path.exists(os.path.join(current_app.root_path,
                      'static/uploads/wastes', f"{waste}.png")):
        old_image_filename = f"{waste}.png"
        new_image_filename = f"{new_name}.png"
        old_image_path = os.path.join(
            current_app.static_folder, "uploads", "Wastes", old_image_filename)
        new_image_path = os.path.join(
            current_app.static_folder, "uploads", "Wastes", new_image_filename)
        os.rename(old_image_path, new_image_path)


def get_waste_info(name):
    """Obtient des informations sur un déchet à partir de l'API OpenAI Waste.

    Args:
        name (str): le nom du déchet.

    Returns:
        Tuple[str, str]: une paire contenant la description du déchet et une liste de manières de le recycler.
    """
    # Instancier l'objet WasteOpenAI avec le nom du déchet
    waste = WasteOpenAI(name)

    # Récupérer la description et la liste des manières pour le recycler
    recycling_instructions = waste.getRecyclingInstructions()
    time.sleep(1.1)
    description = waste.getDescription()
    time.sleep(1.1)
    # Télécharger l'image correspondante
    images = waste.getPictures()
    if len(images) > 0:
        filename = name.lower() + '.png'
        path = os.path.join(current_app.root_path,
                            'static/uploads/wastes', filename)
        images[0].save(path)
    else:
        filename = ''

    # Retourner une chaîne de caractères contenant la description et la liste des manières pour le recycler
    return description, recycling_instructions
