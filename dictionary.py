# Dictionary Application

def select_language():
    print("Select a language:")
    print("1. Nupe")
    print("2. Hausa")
    print("3. Yoruba")
    print("4. Eggon")
    print("5. Igala")

    choice = input("Enter your choice: ")

    while choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Try again.")
        choice = input("Enter your choice: ")

    return choice


def load_dictionary(choice):

    dictionary = {
        "Nupe": {
          
        },

        "Hausa": {
  
        },

        "Yoruba": {
          
        },

        "Eggon": {
            "hello": "kama",
            "thank you": "naga",
            "yes": "ehe",
            "no": "kawa",
            "water": "muna",
            "food": "nyaga",
            "house": "luma",
            "mother": "nana",
            "father": "baba",
            "child": "kidi",
            "friend": "meka",
            "book": "taka",
            "school": "kema",
            "market": "duma",
            "eat": "nya",
            "go": "tana",
            "come": "wena",
            "sun": "suma",
            "rain": "nema",
            "dog": "kura"
        },

        "Igala": {
          
        }
    }

    languages = ["Nupe", "Hausa", "Yoruba", "Eggon", "Igala"]

    return dictionary[languages[int(choice) - 1]]


def translate_word(dictionary):
    word = input("Enter an English word: ").lower()

    if word in dictionary:
        print("Translation:", dictionary[word])
    else:
        print("Word not found in dictionary.")



choice = select_language()

dictionary = load_dictionary(choice)

translate_word(dictionary)
