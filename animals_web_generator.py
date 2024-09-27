import data_fetcher
import re

def load_template():
    """for loading data from html file"""
    with open('animals_template.html', 'r', encoding="utf-8") as file:
        html_template = file.read()
        return html_template

def insert_space_before_capitals(text):
    """Inserts a space before each capital letter in the color strings."""
    return re.sub(r'(?<!^)(?=[A-Z])', ', ', text)


def serialize_animal(animal_obj):
    """Serializes animal objects into HTML"""
    output = '<li class="cards__item">\n'
    output += f"<div class='card__title'>Name: {animal_obj['name']}</div><br/>\n"
    output += f"Diet: {animal_obj['characteristics']['diet']}<br/>\n"
    output += f"First Location: {animal_obj['locations'][0]}<br/>\n"
    habitat = animal_obj['characteristics'].get('habitat')
    if habitat and len(habitat) > 0:
        output += f"Habitat: {habitat}<br/>\n"

    lifespan = animal_obj['characteristics'].get('lifespan')
    if lifespan:
        output += f"Lifespan: {lifespan}<br/>\n"

    common_name = animal_obj.get('common_name')
    if common_name:
        output += f"Common Name: {common_name}<br/>\n"

    animal_type = animal_obj['characteristics'].get('type')
    if animal_type:
        output += f"Type: {animal_type}<br/>\n"

    color = animal_obj['characteristics'].get('color')
    if color:
        formatted_color = insert_space_before_capitals(color)
        output += f"Color: {formatted_color}<br/>\n"

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
    animal_name = input("Please enter an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    if animals_data:
        html_data = load_template()
        string_data_animals = string_creation_data(animals_data)
        replace_animals_info(html_data, string_data_animals)
    else:
        print("Error! No data could be found. Please check input.")


if __name__ == "__main__":
    main()