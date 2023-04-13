import requests

url = "https://openai80.p.rapidapi.com/images/generations"

payload = {
	"prompt": "3d render of a cute banana on dark green background, digital art",
	"n": 2,
	"size": "1024x1024"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "8723434702msh7345cd5719d0fbbp1a687cjsn1bb338f0f52d",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)