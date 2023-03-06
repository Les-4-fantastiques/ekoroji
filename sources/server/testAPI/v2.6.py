import requests
import json
from PIL import Image
from io import BytesIO
import openai
import os

# Set the OpenAI API key
openai.api_key = "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"

class RecyclableItem:
    def __init__(self, name):
        self.name = name
        self.score = None
        self.recycling_info = None
        self.country = None
        self.image_url = None
    
    def get_score(self):
        response = requests.get(f"https://api.ecoindex.fr/v1/get?query={self.name}")
        json_data = json.loads(response.text)
        self.score = json_data["ecoIndex"]["score"]
    
    def get_recycling_info(self):
        response = requests.get(f"https://api.ecoindex.fr/v1/get?query={self.name}")
        json_data = json.loads(response.text)
        self.recycling_info = json_data["ecoIndex"]["recyclingInfo"]
    
    def get_country(self):
        response = requests.get(f"https://api.ecoindex.fr/v1/get?query={self.name}")
        json_data = json.loads(response.text)
        self.country = json_data["ecoIndex"]["country"]
    
    def get_image(self):
        headers = {
            'Authorization': "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",
            'Content-Type': 'application/json',
        }

        data = '{"model": "image-alpha-001", "prompt": "'+self.name+'", "num_images":1}'

        response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=data)

        json_data = json.loads(response.text)
        self.image_url = json_data["data"][0]["url"]
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Recycling info: {self.recycling_info}")
        print(f"Country of origin: {self.country}")
        response = requests.get(self.image_url)
        img = Image.open(BytesIO(response.content))
        img.show()
    
    def get_info(self):
        self.get_score()
        self.get_recycling_info()
        self.get_country()
        self.get_image()
        self.display_info()

# Example usage
item_name = input("Enter an item name to recycle: ")
item = RecyclableItem(item_name)
item.get_info()
