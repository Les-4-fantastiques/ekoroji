import requests

url = "https://openai80.p.rapidapi.com/chat/completions"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Hello!"
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "cd79626b36msh4396c66ae573e37p15450cjsn5764d2310748",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

data = response.json()
print(response.status_code)
print(data['choices'][0]['message']['content'])