"""
    Lemar Llanes
    SDEV 300 6380 Building Secure Python Applications (2242)
    1/28/2024
    Assignment Week 3
    U.S. States Information System that allows a user
    to display, sort, and update information about U.S. states.
"""
import operator
import matplotlib.pyplot as plt
from PIL import Image

# Storing state information
us_states = [
    {"name": "Alabama", "capital": "Montgomery", "population": 194696,
     "flower": "Camellia"},
    {"name": "Alaska", "capital": "Juneau", "population": 31317,
     "flower": "Forget-me-not"},
    {"name": "Arizona", "capital": "Phoenix", "population": 1664896,
     "flower": "Saguaro-Cactus-Blossom"},
    {"name": "Arkansas", "capital": "Little Rock", "population": 200546,
     "flower": "Apple-Blossom"},
    {"name": "California", "capital": "Sacramento", "population": 529946,
     "flower": "California-Poppy"},
    {"name": "Colorado", "capital": "Denver", "population": 693279,
     "flower": "Columbine"},
    {"name": "Connecticut", "capital": "Hartford", "population": 119440,
     "flower": "Mountain-Laurel"},
    {"name": "Delaware", "capital": "Dover", "population": 37354, "flower": "Peach-Blossom"},
    {"name": "Florida", "capital": "Tallahassee", "population": 199400,
     "flower": "Orange-Blossom"},
    {"name": "Georgia", "capital": "Atlanta", "population": 487203, "flower": "Cherokee-Rose"},
    {"name": "Hawaii", "capital": "Honolulu", "population": 332954, "flower": "Hibiscus"},
    {"name": "Idaho", "capital": "Boise", "population": 242363, "flower": "Syringa"},
    {"name": "Illinois", "capital": "Springfield", "population": 110879, "flower": "Violet"},
    {"name": "Indiana", "capital": "Indianapolis", "population": 866202, "flower": "Peony"},
    {"name": "Iowa", "capital": "Des Moines", "population": 207105, "flower": "Wild-Rose"},
    {"name": "Kansas", "capital": "Topeka", "population": 125049,
     "flower": "Wild-Native-Sunflower"},
    {"name": "Kentucky", "capital": "Frankfort", "population": 28487, "flower": "Goldenrod"},
    {"name": "Louisiana", "capital": "Baton Rouge", "population": 215440, "flower": "Magnolia"},
    {"name": "Maine", "capital": "Augusta", "population": 19103,
     "flower": "White-Pine-Cone-and-Tassel"},
    {"name": "Maryland", "capital": "Annapolis", "population": 40253,
     "flower": "Black-Eyed-Susan"},
    {"name": "Massachusetts", "capital": "Boston", "population": 599606,
     "flower": "Mayflower"},
    {"name": "Michigan", "capital": "Lansing", "population": 112348,
     "flower": "Michigan-Apple-Blossom"},
    {"name": "Minnesota", "capital": "St. Paul", "population": 296215, "flower": "Lady's-Slipper"},
    {"name": "Mississippi", "capital": "Jackson", "population": 140874,
     "flower": "Mississippi-Magnolia"},
    {"name": "Missouri", "capital": "Jefferson City", "population": 42417, "flower": "Hawthorn"},
    {"name": "Montana", "capital": "Helena", "population": 35503, "flower": "Bitterroot"},
    {"name": "Nebraska", "capital": "Lincoln", "population": 296513,
     "flower": "Nebraska-Goldenrod"},
    {"name": "Nevada", "capital": "Carson City", "population": 59951,
     "flower": "Sagebrush"},
    {"name": "New Hampshire", "capital": "Concord", "population": 44909,
     "flower": "Purple-Lilac"},
    {"name": "New Jersey", "capital": "Trenton", "population": 89844,
     "flower": "New-Jersey-Violet"},
    {"name": "New Mexico", "capital": "Santa Fe", "population": 89738, "flower": "Yucca-Flower"},
    {"name": "New York", "capital": "Albany", "population": 97085, "flower": "Rose"},
    {"name": "North Carolina", "capital": "Raleigh", "population": 474258, "flower": "Dogwood"},
    {"name": "North Dakota", "capital": "Bismarck", "population": 75545,
     "flower": "Wild-Prairie-Rose"},
    {"name": "Ohio", "capital": "Columbus", "population": 908534, "flower": "Scarlet-Carnation"},
    {"name": "Oklahoma", "capital": "Oklahoma City", "population": 702837,
     "flower": "Oklahoma-Rose"},
    {"name": "Oregon", "capital": "Salem", "population": 183600, "flower": "Oregon-Grape"},
    {"name": "Pennsylvania", "capital": "Harrisburg", "population": 50333,
     "flower": "Pennsylvania-Mountain-Laurel"},
    {"name": "Rhode Island", "capital": "Providence", "population": 188471,
     "flower": "Rhode-Island-Violet"},
    {"name": "South Carolina", "capital": "Columbia", "population": 138224,
     "flower": "Yellow-Jessamine"},
    {"name": "South Dakota", "capital": "Pierre", "population": 13931,
     "flower": "American-Pasque"},
    {"name": "Tennessee", "capital": "Nashville", "population": 648591, "flower": "Iris"},
    {"name": "Texas", "capital": "Austin", "population": 967351, "flower": "Bluebonnet"},
    {"name": "Utah", "capital": "Salt Lake City", "population": 203175, "flower": "Sego-Lily"},
    {"name": "Vermont", "capital": "Montpelier", "population": 7981, "flower": "Red-Clover"},
    {"name": "Virginia", "capital": "Richmond", "population": 226406,
     "flower": "American-Dogwood"},
    {"name": "Washington", "capital": "Olympia", "population": 56808,
     "flower": "Coast-Rhododendron"},
    {"name": "West Virginia", "capital": "Charleston", "population": 46043,
     "flower": "Rhododendron"},
    {"name": "Wisconsin", "capital": "Madison", "population": 270248,
     "flower": "Wood-Violet"},
    {"name": "Wyoming", "capital": "Cheyenne", "population": 64722,
     "flower": "Indian-Paintbrush"},

]


def display_states():
    """
        Display all U.S. States in Alphabetical order with Capital, Population, and Flower
    """
    sorted_states = sorted(us_states, key=operator.itemgetter("name"))
    for state in sorted_states:
        print(
            f"{state['name']}: Capital - {state['capital']}, "
            f"Population - {state['population']}, Flower - {state['flower']}")


def search_state():
    """
        Search for a specific state and display information
    """
    state_name = input("Enter the state name: ")
    state_found = next((state for state in us_states
                        if state["name"].lower() == state_name.lower()), None)

    if state_found:
        print(f"Capital: {state_found['capital']}")
        print(f"Population: {state_found['population']}")
        print(f"State Flower: {state_found['flower']}")

        # Display the image of the state flower
        image_path = f"US_States_Flowers/{state_found['flower'].replace(' ', '_').lower()}.png"
        try:
            img = Image.open(image_path)
            img.show()
        except FileNotFoundError:
            print("Image not found.")

        # You can use external libraries like PIL for handling images
    else:
        print("State not found.")


def display_top5_population_states():
    """
        Provide a Bar graph of the top 5 populated States
    """
    top5_states = sorted(us_states, key=operator.itemgetter("population"), reverse=True)[:5]

    states = [state["name"] for state in top5_states]
    populations = [state["population"] for state in top5_states]

    plt.bar(states, populations)
    plt.xlabel("US States")
    plt.ylabel("Population")
    plt.title("Top 5 Populated States")
    plt.show()


def update_population():
    """
        Update the overall state population for a specific state
    """
    state_name = input("Enter the state name: ")
    state_found = next((state for state in us_states
                        if state["name"].lower() == state_name.lower()), None)

    if state_found:
        while True:
            new_population_str = input(f"Enter the new population for {state_found['name']}: ")

            # This is a validation from the user try to convert string to integer
            # if it's not a number then exception will be handled the error
            try:
                new_population = int(new_population_str)
                if new_population <= 0:
                    print("Population must be a non-negative number.")
                else:
                    state_found["population"] = new_population
                    print("Population updated successfully.")
                    break

            except ValueError:
                print("Invalid input. No Letter/s allowed.")
    else:
        print("State not found.")


def main():
    """
        This is the main of the program
    :return:
    """
    while True:
        print("\n----------------------------------------------")
        print("Welcome to the U.S. States Information System:")
        print("----------------------------------------------")
        print("1. Display all U.S. States")
        print("2. Search for a specific state")
        print("3. Display Bar graph of top 5 populated states")
        print("4. Update state population")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_states()
        elif choice == "2":
            search_state()
        elif choice == "3":
            display_top5_population_states()
        elif choice == "4":
            update_population()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
