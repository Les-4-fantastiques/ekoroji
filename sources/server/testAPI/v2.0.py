import openai
import requests
from io import BytesIO
from PIL import Image

def get_recycling_instructions(objet, api_key, unsplash_access_key):
    # Configure l'accès à l'API OpenAI
    openai.api_key = api_key
    
    # Demande à l'API OpenAI de générer du texte à partir du prompt
    #prompt = f"Comment recycler {objet} ?"
    #prompt = f"Vous êtes un expert écologiste. Votre tâche consiste maintenant à me dire avec des détails comment recycler {objet}."
    prompt = f"Comment trier et recycler l'objet suivant : {objet} ?"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        #temperature=0.7,
    )
    
    # Analyse la réponse de l'API pour récupérer le texte généré
    recycling_instructions = response.choices[0].text.strip()
    
    # Utilise l'API Unsplash pour récupérer une image correspondant à l'objet
    url = "https://api.unsplash.com/search/photos"
    querystring = {"query": objet}
    headers = {"Authorization": f"Client-ID {unsplash_access_key}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    # Analyse la réponse de l'API pour récupérer l'URL de l'image
    json_data = response.json()
    image_url = json_data["results"][0]["urls"]["regular"]
    
    # Télécharge l'image à partir de son URL
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    # Affiche l'image
    img.show()
    
    return recycling_instructions

objet = "brique jus de fruit"
api_key = "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"
unsplash_access_key = "b4uEPkHGfD9Zv3xK_sVp6oYcdmOSZsmwYQxtDlSTYqQ"
recycling_instructions = get_recycling_instructions(objet, api_key, unsplash_access_key)
print(recycling_instructions)
