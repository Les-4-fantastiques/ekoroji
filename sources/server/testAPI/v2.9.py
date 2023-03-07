import openai

# Définir la clé API
openai.api_key = "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"

# Envoyer une demande d'achèvement à GPT-3.5-Turbo-0301
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Comment recycler une voiture ?",
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.5,
)

# Afficher la réponse générée par GPT-3.5-Turbo-0301
print(response.choices[0].text)
