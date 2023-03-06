import openai
import requests
from io import BytesIO

# Configuration de l'API de OpenAI
openai.api_key = "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"
model_engine = "text-davinci-002"

# Configuration de l'API de DALL-E
API_ENDPOINT = 'https://api.openai.com/v1/images/generations'

# Fonction pour obtenir une image de DALL-E
def get_dall_e_image(prompt):
    response = requests.post(API_ENDPOINT,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai.api_key}'
        },
        json={
            'model': 'image-alpha-001',
            'prompt': prompt,
            'num_images': 1,
            'size': '1024x1024',
            'response_format': 'url'
        }
    )

    if response.status_code != 200:
        raise ValueError("Failed to generate image from DALL-E")

    image_url = response.json()['data'][0]['url']
    response = requests.get(image_url)
    image = BytesIO(response.content)

    return image

# Fonction pour obtenir le score écologique d'un objet
def get_eco_score(object_name):
    prompt = f"Recycler {object_name} est écologiquement bon ou mauvais ?"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    eco_score = response.choices[0].text.strip()

    return eco_score

# Fonction principale qui demande à l'utilisateur le nom d'un objet
# et renvoie l'image et le score écologique correspondants
def get_object_image_and_eco_score():
    object_name = input("Entrez le nom d'un objet : ")
    image = get_dall_e_image(f"recyclage {object_name}")
    eco_score = get_eco_score(object_name)

    return image, eco_score

# Utilisation de la fonction principale
image, eco_score = get_object_image_and_eco_score()
print(f"Score écologique : {eco_score}")
# Affichage de l'image récupérée