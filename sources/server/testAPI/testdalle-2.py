import requests
from PIL import Image
from io import BytesIO

# Configuration de la requête HTTP
url = "https://openai80.p.rapidapi.com/images/generations"
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "8723434702msh7345cd5719d0fbbp1a687cjsn1bb338f0f52d",
    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
}
payload = {
    "prompt": "Dessine à la manière d'un enfant, une maison avec un chat et un chien.",
    "n": 2,
    "size": "1024x1024"
}

# Envoi de la requête HTTP
response = requests.post(url, headers=headers, json=payload)

# Traitement des réponses
if response.status_code == 200:
    data = response.json()
    # Récupération des images
    for i, image_data in enumerate(data["data"]):
        image_url = image_data["url"]
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        # Enregistrer l'image sous le nom "image_<numéro>.png"
        image.save(f"image_{i+1}.png")
        print(f"Image {i+1} enregistrée avec succès.")
else:
    print(f"Erreur lors de la requête : {response.status_code} {response.reason}")
