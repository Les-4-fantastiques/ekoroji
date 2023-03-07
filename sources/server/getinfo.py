import openai
import requests
from io import BytesIO
from PIL import Image

class GetInfoDechet:

    def __init__(self, name: str):
        self.m_name = name
        openai.api_key = "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"

    def getImage(self):
        try:
            response = openai.Image.create(
                prompt=f'3d render of a cute {self.m_name} on dark green background, digital art',
                n = 1,
                size = '512x512'
            )
            image_url = response['data'][0]['url']