import random
from jellyfish import jaro_winkler_similarity

responses = {
    "greetings": {
        "inputs": ["hello", "hi", "hey", "hiya"],
        "responses": ["Hi there!", "Hello!", "Greetings!"]
    },
    "feelings": {
        "inputs": ["how are you", "how's it going", "what's up", "how you doing"],
        "responses": ["I'm doing well, thank you.", "Not too bad, thanks for asking.", "I'm feeling great!"]
    },
    "name": {
        "inputs": ["what's your name", "who are you", "your name"],
        "responses": ["My name is Nimbus.", "I'm Nimbus! Nice to meet you.", "People call me Nimbus."]
    },
    "default": {
        "inputs": [],
        "responses": ["I'm sorry, I don't understand what you're asking."]
    }
}

threshold = 0.1

while True:
    user_input = input(">> ")

    best_category = "default"
    best_match_score = 0
    for category, data in responses.items():
        for input_phrase in data["inputs"]:
            match_score = jaro_winkler_similarity(input_phrase.lower(), user_input.lower())
            if match_score > best_match_score:
                best_match_score = match_score
                best_category = category

    if best_match_score >= threshold:
        response = random.choice(responses[best_category]["responses"])
        print(response)
    else:
        response = random.choice(responses["default"]["responses"])
        print(response)