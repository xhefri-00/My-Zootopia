import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

import json

# Load the data from the animals_data.json file
with open('animals_data.json', 'r') as file:
    animals_data = json.load(file)

# Iterate through each animal and print the required information
for animal in animals_data:
    name = animal.get('name')
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations', [])

    # Retrieve fields if they exist
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')
    first_location = locations[0] if locations else None

    # Print the details if they exist
    if name:
        print(f"\nName: {name}")
    if diet:
        print(f"Diet: {diet}")
    if first_location:
        print(f"First location: {first_location}")
    if animal_type:
        print(f"Type: {animal_type}")

