import openai_secret_manager
import requests

def get_recycling_options(object_name):
    # Get Clarifai API credentials
    clarifai_secrets = openai_secret_manager.get_secret("clarifai")

    # Set up headers and query parameters
    headers = {
        "Authorization": f"Bearer {clarifai_secrets['api_key']}",
        "Content-Type": "application/json",
    }
    data = {"inputs": [{"data": {"concepts": [{"name": object_name}]}}]}
    url = "https://api.clarifai.com/v2/models/" + clarifai_secrets['model_id'] + "/outputs"

    # Make request to Clarifai API
    response = requests.post(url, headers=headers, json=data)

    # Parse response and extract recycling options
    recycling_options = []
    if response.status_code == 200:
        results = response.json()["outputs"][0]["data"]["concepts"]
        for result in results:
            if result["name"] != object_name and result["value"] > 0.75:
                recycling_options.append(result["name"])
    return recycling_options

item = "bouteille en plastique"
recycling_options = get_recycling_options(item)
print(f"Voici différentes façons de recycler une {item}:")
print(recycling_options)
