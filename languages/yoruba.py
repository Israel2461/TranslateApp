dictionary = {
    "hello": "bawo",
    "food": "ounje",
    "water": "omi",
    "house": "ile",
    "love": "ife"
}

def translate(word):
    return dictionary.get(word, "Word not found")
