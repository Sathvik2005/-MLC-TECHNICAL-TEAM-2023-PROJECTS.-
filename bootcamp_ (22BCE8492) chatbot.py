import datetime  # Used to get the time

responses = {
    "hello": ["Hey there! What's up?", "Hi! What's going on?", "What's new, friend?"],
    "hi": ["Hey there! What's up?", "Hi! What's going on?", "What's new, friend?"],
    "how are you": ["I'm doing great, thanks! How about you?", "Feeling good, how are you?", "Chillin' like a villain. How about you?"],
    "what can you do": ["I can chat and answer questions. Ask me anything!", "I'm here to talk and help out. What's on your mind?", "I'm like a talking encyclopedia, but more fun."],
    "hungry": ["Sounds like you need a snack! Grab something to eat.", "Your tummy's talking! Time for some food.", "Don't let your stomach growl, go get some grub!"],
    "thirsty": ["Drink up! Water is your best friend.", "Stay hydrated, my friend. Grab a drink!", "Don't forget to quench your thirst."],
    "time": lambda: "It's " + str(datetime.datetime.now().time()),  #  the time
    "quit": ["See you later, friend!", "Bye for now, catch you next time!", "Take care, talk to you soon!"]
}

while True:
    s = input("Hi! How can I help you today? Say 'exit' or 'quit' to leave. ").lower()  # takes input and stores as "s"

    if "book" in s:
        print("How about a mystery in a fantasy world? Sound interesting?")

    elif "joke" in s:
        print("What did the ocean say to the beach? Nothing, it just waved.")  # jokes 

    elif "weather" in s:
        print("I can't tell you the weather right now, but I can tell you the time!")

    elif "music" in s:
        print("I love music! What kind of tunes do you like?")

    elif "bored" in s:
        print("Let's play a game! How about 20 questions?")

    elif "thanks" in s:
        print("No problem, happy to help!")

    elif s in responses:
        response = random.choice(responses[s])  # Chooses a random response
        if callable(response):
            response = response()
        print(response)

    else:
        print("Sorry, I don't understand. Could you rephrase that?")

    if s in ("exit", "quit"):
        break

print("Thanks for chatting! It was fun.")
