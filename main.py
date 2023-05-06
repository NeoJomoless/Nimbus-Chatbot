import random
import discord
from jellyfish import jaro_winkler_similarity

# define the responses as a dictionary of categories, each with a list of inputs and responses
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

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

# define a threshold for similarity
threshold = 0.6
client=discord.Client(intents=intent)

@client.event
# main loop
async def on_message(message):
    if message.content.startswith('!'):
        user_input = message.content[1:]
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
            await message.channel.send(response)
        else:
            response = random.choice(responses[best_category]["responses"])
            await message.channel.send(response)

client.run("Your token here")