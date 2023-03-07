import openai
import requests
from io import BytesIO

# Configure OpenAI API key
openai.api_key = "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"

# Define the word to look up
word = "python"

# Call OpenAI's GPT-3 to get the word's origin
response = openai.Completion.create(
    engine="davinci",
    prompt=f"Quel est l'origine du mot {word}?",
    max_tokens=50,
)

origin = response.choices[0].text.strip()

# Call the Unsplash API to get a related image
url = "https://api.unsplash.com/search/photos"
querystring = {"query": word}
headers = {"Authorization": "b4uEPkHGfD9Zv3xK_sVp6oYcdmOSZsmwYQxtDlSTYqQ"}
response = requests.request("GET", url, headers=headers, params=querystring)

# Get the URL of the first image returned by the API
json_data = response.json()
print(json_data)

image_url = json_data["results"][0]["urls"]["regular"]

# Download the image and display it
response = requests.get(image_url)
img = BytesIO(response.content)

from PIL import Image
img = Image.open(img)
img.show()

# Print the word's origin
print(f"L'origine du mot {word} est {origin}.")
