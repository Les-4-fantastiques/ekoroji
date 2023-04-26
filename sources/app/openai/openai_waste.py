import requests
from PIL import Image
from io import BytesIO
from app.openai.keyencryption import KeyEncryption


class WasteOpenAI:
    def __init__(self, name: str):
        """
        Initialise une instance de la classe WasteOpenAI.
        
        Parameters
        ----------
        name : str
            Nom du déchet dont on veut récupérer des informations.
        """
        self.__m_name = name

        # Récupération de la clé d'API pour OpenAI.
        key_api = KeyEncryption()
        with open('sources/app/openai/key_api.txt', 'r') as file:
            key_api.setKeyEncrypted(file.read())

        # Définition des URLs et des headers pour les requêtes.
        self.url_image = "https://openai80.p.rapidapi.com/images/generations"
        self.url_chat = "https://openai80.p.rapidapi.com/chat/completions"
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key_api.getKeyClean(),
            "X-RapidAPI-Host": "openai80.p.rapidapi.com"
        }

    def getPictures(self, definition: int = 512):
        """
        Récupère une image générée par OpenAI à partir du nom du déchet.
        
        Parameters
        ----------
        definition : int, optional
            La définition de l'image (par défaut 512).
        
        Returns
        -------
        List[Image]
            La liste des images générées.
        """
        self.images = []
        try:
            self.payload = {
                "prompt": f"Un(e) {self.__m_name} au centre de l'image sur un fond vert foncé (#446127)",
                "n": 1,
                "size": f'{definition}x{definition}'
            }
            response = requests.post(
                self.url_image, headers=self.headers, json=self.payload)
            if response.status_code == 200:
                data = response.json()
                for i, image_data in enumerate(data['data']):
                    image_url = image_data['url']
                    image_content = requests.get(image_url).content
                    self.images.append(Image.open(BytesIO(image_content)))
            else:
                print(
                    f"Erreur lors de la requête : {response.status_code} {response.reason}")
        except ValueError:
            #print('value error')
            return None
        else:
            #print('no error')
            pass
        return self.images

    def __getRequest(self, prompt: str):
        """
        Effectue une requête à OpenAI à partir d'un prompt donné.
        
        Parameters
        ----------
        prompt : str
            Le prompt à utiliser pour la requête.
        
        Returns
        -------
        str
            La réponse de la requête.
        """
        request_value = ''
        try:
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            response = requests.request("POST", self.url_chat, json=payload, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                request_value = data['choices'][0]['message']['content']
            else:
                print(
                    f"Erreur lors de la requête : {response.status_code} {response.reason}")
        except ValueError:
            #print('value error')
            return None
        else:
            #print('no error')
            pass
        return request_value
    
    def getDescription(self):
        """
        Récupère une définition ou une description courte de l'objet à partir de son nom grâce à une requête à l'API OpenAI.
        
        Returns
        -------
        str
            La description de l'objet.
        """
        self.description = self.__getRequest(f"Donnez une définition ou une description courte de 150 lettres de l'objet suivant : {self.__m_name}")
        return self.description
    
    def getRecyclingInstructions(self):
        """
        Récupère une liste de 5 façons de recycler l'objet à partir de son nom grâce à une requête à l'API OpenAI.
        
        Returns
        -------
        str
            La liste des façons de recycler l'objet.
        """
        self.recycling_instructions = self.__getRequest(f'Pouvez-vous générer une liste de 5 façons de recycler cet(te) {self.__m_name} ?')
        return self.recycling_instructions
    
    def getName(self):
        """
        Récupère le nom de l'objet.
        
        Returns
        -------
        str
            Le nom de l'objet.
        """
        return self.__m_name