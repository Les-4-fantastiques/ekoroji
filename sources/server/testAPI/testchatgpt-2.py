import requests

url = "https://api.openai.com/v1/engines/davinci-codex/completions"

payload = {
    "prompt": "Comment recycler une bouteille en plastique",
    "max_tokens": 1024,
    "temperature": 0.7,
    "n": 1,
    "stop": "\n"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "8723434702msh7345cd5719d0fbbp1a687cjsn1bb338f0f52d"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    answer = data["choices"][0]["text"]
    print(answer)
else:
    print("Erreur lors de la requête:", response.status_code)
