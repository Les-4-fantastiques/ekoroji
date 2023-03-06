import openai
import requests
from io import BytesIO
from PIL import Image

# Set OpenAI API key
openai.api_key = "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"

# Generate image from text using DALL-E API
def generate_image(text):
    response = openai.Image.create(
        prompt=f'3d render of a cute {text} on dark green background, digital art',
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_content = requests.get(image_url).content
    image = Image.open(BytesIO(image_content))
    return image

# Example usage
image = generate_image("home")
image.show()
