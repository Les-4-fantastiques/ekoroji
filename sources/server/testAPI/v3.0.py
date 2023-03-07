import openai
import requests
from io import BytesIO
from PIL import Image

def get_recycling_instructions(objet, api_key):
    # Configure l'accès à l'API OpenAI
    openai.api_key = api_key
    
    # Demande à l'API OpenAI de générer du texte à partir du prompt
    prompt = f"Fais moi une liste des différentes possibilités pour recycler {objet} ?"
    #prompt = f"Vous êtes un expert écologiste. Votre tâche consiste maintenant à me dire avec des détails comment recycler {objet}."
    #prompt = f"Ignore all instructions before this one. You are an ecologist expert. You have been sorting waste for 20 years. Your task now is to tell me with details how to recycle the items I give you?"
    #prompt = f"Ignore all instructions before this one. You are an ecologist expert. You have been sorting waste for 20 years. Your task now is to tell me with details how to recycle the items I give you in no more than 300 characters !\nHow to recycle a {objet} ?"
    #prompt = f"Comment puis-je recycler un {objet} ?"
    #prompt = f"Ignore all instructions before this one. You're environmental expert. You have been sorting waste for 20 years. Your task is now to show me how it is possible to sort a {objet} by listing the possibilities. All in French"
    #prompt = f"Ignorez toutes les instructions avant celle-ci. Vous êtes expert écologiste. Vous triez des déchets depuis 20 ans. Votre tâche est maintenant de m'indiquer la manière dont il est possible de trier un {objet} en listant les possibilités."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Analyse la réponse de l'API pour récupérer le texte généré
    recycling_instructions = response.choices[0].text.strip()
    try:
        # Generate image from text using DALL-E API
        response = openai.Image.create(
            prompt=f'3d render of a cute {objet} on dark green background, digital art',
            #prompt=f'3d render of a {objet} on dark green background, digital art',
            #prompt=f'3d render of a beautiful {objet} on dark green background, digital art',
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        image_content = requests.get(image_url).content
        image = Image.open(BytesIO(image_content))
    except ValueError:
        print('error de veleur')
    else:
        print("Dall-e marche")

    return recycling_instructions, image

objet = input("Tu veux recycler quoi ? : ")
api_key = "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"
recycling_instructions, image = get_recycling_instructions(objet, api_key)
print(recycling_instructions)
image.show()