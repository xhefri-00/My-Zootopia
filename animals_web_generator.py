import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
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
    with open('animals_template.html', 'r', encoding="utf-8") as file:
        html_template = file.read()
        return html_template


def serialize_animal(animal_obj):
    """Serializes animal objects into HTML"""
    output = '<li class="cards__item">\n'
    output += f"<div class='card__title'>Name: {animal_obj['name']}</div><br/>\n"
    output += f"Diet: {animal_obj['characteristics']['diet']}<br/>\n"
    output += f"First Location: {animal_obj['locations'][0]}<br/>\n"
    habitat = animal_obj['characteristics'].get('habitat')
    if habitat and len(habitat) > 0:
        output += f"Habitat: {habitat[:]}<br/>\n"  # Using the first habitat if there are multiple

    lifespan = animal_obj['characteristics'].get('lifespan')
    if lifespan:
        output += f"Lifespan: {lifespan[:]}<br/>\n"

    common_name = animal_obj.get('common_name')
    if common_name:
        output += f"Common Name: {common_name[:]}<br/>\n"

    animal_type = animal_obj['characteristics'].get('type')
    if animal_type:
        output += f"Type: {animal_type}<br/>\n"

    color = animal_obj['characteristics'].get('color')
    if color:
        output += f"Color: {color[:]}<br/>\n"

    output += '</li>\n'
    return output


def string_creation_data(animals_data):
    """Creates an HTML string for all animals"""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output

def replace_animals_info(html_data, string_data_animals):
    replaced_data = html_data.replace('__REPLACE_ANIMALS_INFO__', string_data_animals)
    print(replaced_data)

    with open('edited_animals.html', 'w', encoding="utf-8") as file:
        html_template = file.write(replaced_data)


def main():
    animals_data = load_data('animals_data.json')
    html_data = load_template()
    string_data_animals = string_creation_data(animals_data)
    replace_animals_info(html_data, string_data_animals)


if __name__ == "__main__":
    main()