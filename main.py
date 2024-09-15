import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def iterating_data(animals_data):
    """Iterate through each animal and print the required information"""
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


def load_template():
    """for loading data from html file"""
    with open('animals_template.html', 'r') as file:
        html_template = file.read()
        return html_template


def string_creation_data(animals_data):
    output = ""
    for animal in animals_data:
    # append information to each string
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        output += f"First location: {animal['locations'][0]}\n"
        animal_type = animal['characteristics'].get('type')
        if animal_type:
            output += f"Type: {animal['characteristics']['type']}\n"
    return output

def replace_animals_info(html_data, string_data_animals):
    replaced_data = html_data.replace('__REPLACE_ANIMALS_INFO__', string_data_animals)
    print(replaced_data)

    with open('edited_animals.html', 'w') as file:
        html_template = file.write(replaced_data)


def main():
    animals_data = load_data('animals_data.json')
    iteration_data = iterating_data(animals_data)
    html_data = load_template()
    string_data_animals = string_creation_data(animals_data)
    replace_animals_info(html_data, string_data_animals)


if __name__ == "__main__":
    main()