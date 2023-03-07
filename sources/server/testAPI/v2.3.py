import openai
import requests
import json

openai.api_key = "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"

def get_recycling_options(item):
    prompt = f"List different ways to recycle {item}."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recycling_options = response.choices[0].text.strip()
    return recycling_options

item = "white paper"
recycling_options = get_recycling_options(item)
print(f"Voici différentes façons de recycler une {item}:")
print(recycling_options)
