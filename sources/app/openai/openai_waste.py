import requests
from PIL import Image
from io import BytesIO
from app.openai.keyencryption import KeyEncryption


class WasteOpenAI:
    def __init__(self, name: str):
        """__init__ _summary_

        Parameters
        ----------
        name : str
            _description_
        """
        self.__m_name = name
        key_api = KeyEncryption()
        with open('sources/app/openai/key_api.txt', 'r') as file:
            key_api.setKeyEncrypted(file.read())
        self.url_image = "https://openai80.p.rapidapi.com/images/generations"
        self.url_chat = "https://openai80.p.rapidapi.com/chat/completions"
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key_api.getKeyClean(),
            "X-RapidAPI-Host": "openai80.p.rapidapi.com"
        }

    def getPictures(self, definition: int = 512):
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
        self.description = self.__getRequest(f"Donnez une définition ou une description courte de 150 lettres de l'objet suivant : {self.__m_name}")
        return self.description
    
    def getRecyclingInstructions(self):
        self.recycling_instructions = self.__getRequest(f'Pouvez-vous générer une liste de 5 façons de recycler cet(te) {self.__m_name} ?')
        return self.recycling_instructions
    
    def getName(self):
        return self.__m_name