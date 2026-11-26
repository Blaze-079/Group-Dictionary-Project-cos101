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
            "hello": "kówo",
            "thank you": "nago",
            "yes": "ehen",
            "no": "ká",
            "water": "nuwan",
            "food": "eyangici",
            "house": "emi",
            "mother": "nna",
            "father": "baba",
            "child": "dzankan",
            "friend": "eya",
            "book": "takada",
            "school": "makanta",
            "market": "dzuko",
            "eat": "gi",
            "go": "tá",
            "come": "wá",
            "sun": "yigidi",
            "rain": "ele",
            "dog": "eshigi"
        },

        "Hausa": {
           "hello": "sannu",
            "thank you": "na gode",
            "yes": "eh",
            "no": "a'a",
            "water": "ruwa",
            "food": "abinci",
            "house": "gida",
            "mother": "uwa",
            "father": "uba",
            "child": "yaro",
            "friend": "aboki",
            "book": "littafi",
            "school": "makaranta",
            "market": "kasuwa",
            "eat": "ci",
            "go": "tafi",
            "come": "zo",
            "sun": "rana",
            "rain": "ruwan sama",
            "dog": "kare"
        },

        "Yoruba": {
          "hello": "bawo ni",
            "thank you": "ẹ ṣé",
            "yes": "bẹ́ẹ̀ni",
            "no": "bẹ́ẹ̀ kọ́",
            "water": "omi",
            "food": "ounjẹ",
            "house": "ilé",
            "mother": "ìyá",
            "father": "bàbá",
            "child": "ọmọ",
            "friend": "ọ̀rẹ́",
            "book": "ìwé",
            "school": "ilé-ẹ̀kọ́",
            "market": "ọjà",
            "eat": "jẹ",
            "go": "lọ",
            "come": "wá",
            "sun": "òòrùn",
            "rain": "òjò",
            "dog": "ajá"

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
            "hello": "kóma",
            "thank you": "nago",
            "yes": "ehe",
            "no": "kó",
            "water": "nima",
            "food": "ẹnyọ",
            "house": "ọma",
            "mother": "nna",
            "father": "baba",
            "child": "ọmọ",
            "friend": "ẹka",
            "book": "taka",
            "school": "ẹkọ",
            "market": "ọja",
            "eat": "nya",
            "go": "la",
            "come": "wa",
            "sun": "ọjọ",
            "rain": "ẹma",
            "dog": "ẹja"
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
