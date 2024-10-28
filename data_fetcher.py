import requests
from dotenv import load_dotenv
import os

def fetch_data(animal_name):
    """
       Fetch data for a specific animal from the API Ninjas service.

       This function sends a request to the API Ninjas' animal endpoint
       to retrieve information about a given animal by its name.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    load_dotenv()
    api_key = os.getenv('API_KEY')

    try:
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:
            return response.json()

        print(f"Error: {response.status_code}, {response.text}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None