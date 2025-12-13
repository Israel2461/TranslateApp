dictionary = {
    "hello": "ndewo",
    "food": "nri",
    "water": "mmiri",
    "house": "ulo",
    "love": "ihunanya"
}

def translate(word):
    return dictionary.get(word, "Word not found")
