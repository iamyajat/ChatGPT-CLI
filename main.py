import openai
import os
import json
import argparse
import pickle

openai.api_key_path = "./api_key.txt"


def create_personas():
    with open("personas.json", "r") as f:
        personas = json.load(f)

    new_persona = {}
    new_persona["name"] = input("Enter the name of the persona: ")
    new_persona["prompt"] = input("Enter the prompt for the persona: ")
    personas.append(new_persona)

    with open("personas.json", "w") as f:
        json.dump(personas, f, indent=4)

    return personas


def get_persona_prompt(persona):
    with open("personas.json", "r") as f:
        personas = json.load(f)

    persona_def = ""

    if persona is None:
        persona_def = "You are a helpful assistant."
    else:
        found = False
        for p in personas:
            if p["name"] == persona:
                persona_def = p["prompt"]
                print("Persona loaded:", persona, end="\n\n")
                found = True
                break

        if not found:
            print("Persona not found. Creating a new persona...")
            personas = create_personas()
            persona_def = personas[-1]["prompt"]

    return persona_def


def save_chat_history(messages):
    print()
    save = input("Do you want to save the chat history? (y/n) ")
    if save == "y":
        filename = input("Enter the chat name to save the chat history: ")
        with open("./history/" + filename + ".pkl", "wb") as f:
            pickle.dump(messages, f)
        print("Chat history saved to:", filename, end="\n\n")


def load_chat_history(filename):
    with open("./history/" + filename + ".pkl", "rb") as f:
        messages = pickle.load(f)
    return messages


def start_chat(persona=None, history_file_name=None):
    print("\nWelcome to the ChatGPT! Please ask me a question.")
    print("Type 'quit' to exit the chatbot.")
    print("Type 'clear' to clear the chat history.", end="\n\n")

    persona_def = get_persona_prompt(persona)
    messages = [{"role": "system", "content": persona_def}]

    if history_file_name is not None:
        messages = load_chat_history(history_file_name)
        for m in messages:
            if m["role"] == "user":
                print("You:", m["content"])
            elif m["role"] == "assistant":
                print("Assistant:", m["content"])

            print()

    while True:
        user_input = input("You: ")
        if user_input == "quit":
            save_chat_history(messages)
            break
        elif user_input == "clear":
            save_chat_history(messages)
            print("\nBrain cleared. Start a new conversation.\n")
            messages = [{"role": "system", "content": persona_def}]
            continue

        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        assistant_message = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": assistant_message.strip()})
        #  print it in a different colour
        

        print("\nAssistant:", assistant_message, end="\n\n")


# get values from command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--persona", type=str, default=None, help="The persona of the chatbot."
    )
    parser.add_argument(
        "--load", type=str, default=None, help="The chat history to load."
    )
    args = parser.parse_args()

    start_chat(persona=args.persona, history_file_name=args.load)
