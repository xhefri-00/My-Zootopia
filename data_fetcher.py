import requests

def fetch_data(animal_name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    api_key = "mJhYs7Z+4LdRKUkKW4TT7A==z8iKL7GxYnmLK8yb"

    try:
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None