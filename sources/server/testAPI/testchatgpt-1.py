import requests

url = """https://openai80.p.rapidapi.com/chat/completions"""

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
            "content": "Salut !"
			#"content": "Listes moi les différentes possibilités pour recycler une bouteille en plastique ?"
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "8723434702msh7345cd5719d0fbbp1a687cjsn1bb338f0f52d",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

# Vérifier que la réponse contient des choix
if "choices" in response.json() and len(response.json()["choices"]) > 0:
    for choice in response.json()["choices"]:
        if "text" in choice:
            print(choice["text"])
        else:
            print("Pas de texte trouvé pour ce choix.")
else:
    print("Pas de réponse trouvée.")
