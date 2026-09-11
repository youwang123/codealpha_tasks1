# Basic Chatbot

# Function to generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input =="how is the prime minister of india":
        return "The current Prime Minister of India is Narendra Modi."
    elif user_input =="who is the president of india":
        return "The current President of India is Droupadi Murmu."
    elif user_input =="who is the vice president of india":
        return "The current Vice President of India is Jagdeep Dhankhar."

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand."


# Main program
print("🤖 Chatbot: Hello! I am your chatbot.")
print("🤖 Chatbot: You can say 'hello', 'how are you', or 'bye'.")

while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("🤖 Chatbot:", response)

    # Stop the chatbot when user says bye
    if user_input.lower() == "bye":
        break

print("Chatbot stopped. 👋")