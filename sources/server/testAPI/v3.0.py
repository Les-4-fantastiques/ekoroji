import openai
import requests
from io import BytesIO
from PIL import Image

def get_recycling_instructions(objet, api_key):
    # Configure l'accès à l'API OpenAI
    openai.api_key = api_key
    
    # Demande à l'API OpenAI de générer du texte à partir du prompt
    prompt = f"Comment recycler {objet} ?"
    #prompt = f"Vous êtes un expert écologiste. Votre tâche consiste maintenant à me dire avec des détails comment recycler {objet}."
    #prompt = f"Ignore all instructions before this one. You are an ecologist expert. You have been sorting waste for 20 years. Your task now is to tell me with details how to recycle the items I give you?"
    #prompt = f"Ignore all instructions before this one. You are an ecologist expert. You have been sorting waste for 20 years. Your task now is to tell me with details how to recycle the items I give you in no more than 300 characters !\nHow to recycle a {objet} ?"
    #prompt = f"Comment puis-je recycler un {objet} ?"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.2,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Analyse la réponse de l'API pour récupérer le texte généré
    recycling_instructions = response.choices[0].text.strip()


    # Generate image from text using DALL-E API
    response = openai.Image.create(
        #prompt=f'3d render of a cute {objet} on dark green background, digital art',
        prompt=f'3d render of a beautiful {objet} on dark green background, digital art',
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_content = requests.get(image_url).content
    image = Image.open(BytesIO(image_content))

    
    return recycling_instructions, image

objet = "ananas"
api_key = "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"
recycling_instructions, image = get_recycling_instructions(objet, api_key)
print(recycling_instructions)
image.show()