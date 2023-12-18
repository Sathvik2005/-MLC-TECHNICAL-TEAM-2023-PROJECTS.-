
greetings = [
    "Hey there!",
    "Hello!",
    "It's nice to meet you!",
    "can you suggest some books for me",
]
responses = {
    "hello": "Hi! What's your name?",
    "name": "Nice to meet you, {name}!",
    "how are you": "I'm doing well, thanks for asking! How about you?",
    "what can you do": "I can chat and answer simple questions. What would you like to talk about?",
    "which genere would you like": "Hmm, how about fantasy? Do you prefer mysteries within the fantasy genre?",
    "are you interested in webnovels": "Yes, I can recommend some webnovels as well. Are you okay with translated works?",
    "yes": "Great! Then you might like 'Reverend Insanity'. It's a dark fantasy cultivation webnovel with intriguing mysteries.",
    "ok but can you suggest others": "Certainly! If you prefer a more steampunk theme with cosmic horror elements, you might enjoy 'Lord of the Mysteries'.",
    "quit": "Bye! It was nice talking to you."
}

while True:
    user_input = input("> ").lower()

    if user_input in greetings:
        response = responses[user_input]
    elif user_input in responses:
        response = responses[user_input]
    elif "how" in user_input:
        response = "I'm not sure I understand your question. Can you rephrase it?"
    else:
        response = f"Hmm, I haven't learned about {user_input} yet. Tell me more!"

    print(response)

    if user_input == "quit":
        break

print("Thanks for chatting!")
