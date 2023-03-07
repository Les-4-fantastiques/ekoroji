import requests
import json

class RecyclingFactsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.recyclingfactsapi.com/v0/"

    def get_info(self, query):
        endpoint = "search/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "query": query
        }
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)
        return data

def main():
    api_key = "YOUR_API_KEY"
    r = RecyclingFactsAPI(api_key)
    query = input("Enter an object to recycle: ")
    data = r.get_info(query)
    print(f"Object: {query}")
    print(f"Recycling description: {data[0]['description']}")
    print(f"Recycling tips: {data[0]['recycling_tips']}")
    print(f"Materials: {data[0]['materials']}")
    print(f"Categories: {data[0]['categories']}")

if __name__ == "__main__":
    main()
