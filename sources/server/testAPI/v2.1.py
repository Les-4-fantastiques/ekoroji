import requests

def get_image_pixabay(word):
    API_KEY = "YOUR_PIXABAY_API_KEY"
    
    url = "https://pixabay.com/api/"
    querystring = {"key": API_KEY, "q": word, "image_type": "photo", "safesearch": "true"}
    
    response = requests.request("GET", url, params=querystring)
    json_data = response.json()
    
    if json_data["hits"]:
        image_url = json_data["hits"][0]["largeImageURL"]
        return image_url
    else:
        return "No image found"
    
    

get_image_pixabay("voiture")