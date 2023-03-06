import requests

def get_recycling_info(object_name):
    url = f"https://api.recyclenow.com/{object_name}"
    response = requests.get(url)

    if response.status_code == 404:
        return f"Sorry, we couldn't find any recycling information for {object_name}."

    recycling_info = response.json()

    result = f"Recycling information for {object_name}:\n"
    result += f"    - Can it be recycled? {recycling_info['recyclable']}\n"
    result += f"    - How to recycle it: {recycling_info['recycling_method']}\n"
    result += f"    - Additional information: {recycling_info['additional_info']}\n"

    return result

# Example usage
object_name = input("Enter an object name to get recycling information: ")
print(get_recycling_info(object_name))
