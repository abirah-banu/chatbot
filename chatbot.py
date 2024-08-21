def simple_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching
    
    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    # Asking about the bot
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    
    # Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Asking for the bot's name
    elif "what is your name" in user_input:
        return "I am a simple chatbot created to assist you."
    
    # Asking for help
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    
    # Default response for unknown queries
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chatbot interaction loop
print("Welcome to the Simple Chatbot! Type 'bye' to exit.")

while True:
    user_query = input("You: ")
    if "bye" in user_query.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_query)
    print(f"Chatbot: {response}")
