import random

responses = {
    "hello": ["Hi!", "Hello there!", "Hey!"],
    "how are you": ["I'm fine, thanks!", "Doing great, how about you?"],
    "your name": ["I'm a simple chatbot!", "You can call me ChatBot."],
    "what can you do": ["I can chat about simple things like greetings and how you're doing!"],
    "thank you": ["You're welcome!", "No problem!"],
    "bye": ["Goodbye!", "See you later!", "Bye, take care!"],
}


def get_response(user_input):
    user_input = user_input.lower().strip()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that."


def confirm_exit():
    answer = input("Chatbot: Are you sure you want to leave? (yes/no) ")
    return answer.lower().strip() in ["yes", "y"]


def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if "bye" in user_input.lower():
            if confirm_exit():
                print("Chatbot:", random.choice(responses["bye"]))
                break
            else:
                print("Chatbot: Great, let's keep chatting!")
                continue

        response = get_response(user_input)
        print("Chatbot:", response)


chatbot()