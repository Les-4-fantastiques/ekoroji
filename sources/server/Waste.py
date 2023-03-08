import openai
import requests
from io import BytesIO
from PIL import Image

class Waste:

    def __init__(self, name:str):
        self.m_name = name
        openai.api_key = ''

    def getPicture(self, definition:int = 512):
        try:
            response = openai.Image.create(
                prompt=f'3d render of a cute {self.m_name} on dark green background, digital art',
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
        self.recycling_instructions = self.__getRequest(f'Fais moi une liste des différentes possibilités pour recycler {self.m_name} ?')
        return self.recycling_instructions

    def getDescription(self):
        self.description = self.__getRequest(f"C'est quoi un {self.m_name} ?")
        return self.description