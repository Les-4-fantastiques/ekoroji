import openai
import requests
from io import BytesIO
from PIL import Image
from KeyEncryption import *

class Waste:

    def __init__(self, name:str):
        """
        Constructeur de la classe Waste. Il initialise le nom de l'objet déchet et la clé API OpenAI.
        """
        self.__m_name = name
        key_api_openai = KeyEncryption()
        key_api_openai.setKeyEncrypted('tl.SOhM7SCDkO{LvxHoK6:IU4CmclGKsRbTC:{PuFbFLHRnDtXW')
        openai.api_key = key_api_openai.getKeyClean()

    def getPicture(self, definition:int = 512):
        """
        Cette méthode permet de récupérer une image du déchet en question en faisant une requête à l'API d'OpenAI.
        
        Paramètres:
        - definition : la définition de l'image à récupérer
        
        Retourne:
        - self.image : une instance de la classe Image (PIL) de l'image récupérée
        """
        try:
            response = openai.Image.create(
                prompt=f'3d render of a cute {self.__m_name} on dark green background, digital art',
                n = 1,
                size = f'{definition}x{definition}'
            )
            image_url = response['data'][0]['url']
            image_content = requests.get(image_url).content
            self.image = Image.open(BytesIO(image_content))
        except ValueError:
            print('value error')
            return None
        else:
            print('no error')
        return self.image
        
    def __getRequest(self, prompt:str):
        """
        Cette méthode est une méthode privée qui permet de faire une requête textuelle à l'API d'OpenAI en donnant un prompt.
        
        Paramètres:
        - prompt : la demande à envoyer à l'API d'OpenAI
        
        Retourne:
        - request_value : la réponse de l'API à la demande sous forme de chaîne de caractères
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            request_value = response.choices[0].text.strip()
        except ValueError:
            print('value error')
            return None
        else:
            print('no error')
        return request_value

    def getRecyclingInstructions(self):
        """
        Cette méthode permet de récupérer les différentes possibilités de recyclage du déchet en question.
        
        Retourne:
        - self.recycling_instructions : une chaîne de caractères contenant les différentes possibilités de recyclage
        """
        self.recycling_instructions = self.__getRequest(f'Fais moi une liste des différentes possibilités pour recycler {self.__m_name} ?')
        return self.recycling_instructions

    def getDescription(self):
        """
        Cette méthode permet de récupérer la description du déchet en question.
        
        Retourne:
        - self.description : une chaîne de caractères contenant la description du déchet
        """
        self.description = self.__getRequest(f"C'est quoi un {self.__m_name} ? Dis moi en français")
        return self.description

    def getName(self):
        return self.__m_name