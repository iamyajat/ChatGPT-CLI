import openai
import os
import json
import argparse
import pickle
from colorama import Fore, Back, Style

# C:\\Users\\yajat\\.chatgpt-cli
# ~/.chatgpt-cli

import os

BASE_PATH = os.path.expanduser("~") + "/.chatgpt-cli/"

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

filename = "personas.json"
filepath = os.path.join(BASE_PATH, filename)

if not os.path.exists(filepath):
    with open(filepath, "w") as f:
        f.write("{}")


def create_personas():
    with open(BASE_PATH + "personas.json", "r") as f:
        personas = json.load(f)

    new_persona = {}
    new_persona["name"] = input("Enter the name of the persona: ")
    new_persona["prompt"] = input("Enter the prompt for the persona: ")
    personas.append(new_persona)

    with open(BASE_PATH + "personas.json", "w") as f:
        json.dump(personas, f, indent=4)

    return personas


def get_persona_prompt(persona):
    with open(BASE_PATH + "personas.json", "r") as f:
        personas = json.load(f)

    persona_def = ""

    if persona is None:
        persona_def = "You are a helpful assistant."
    else:
        found = False
        for p in personas:
            if p["name"] == persona:
                persona_def = p["prompt"]
                print(
                    Fore.CYAN + persona + " persona loaded" + Style.RESET_ALL,
                    end="\n\n",
                )
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
        with open(BASE_PATH + "history/" + filename + ".pkl", "wb") as f:
            pickle.dump(messages, f)
        print("Chat history saved to:", filename, end="\n\n")


def load_chat_history(filename):
    with open(BASE_PATH + "history/" + filename + ".pkl", "rb") as f:
        messages = pickle.load(f)
    return messages


def start_chat(persona=None, history_file_name=None):
    print(
        Fore.GREEN + "\nWelcome to ChatGPT! Please ask me a question." + Style.RESET_ALL
    )
    print("Type " + Fore.YELLOW + "quit" + Style.RESET_ALL + " to exit the chat.")
    print(
        "Type "
        + Fore.YELLOW
        + "clear"
        + Style.RESET_ALL
        + " to clear the chat history.\n"
    )

    persona_def = get_persona_prompt(persona)
    messages = [{"role": "system", "content": persona_def}]

    if history_file_name is not None:
        messages = load_chat_history(history_file_name)
        for m in messages:
            if m["role"] == "user":
                print(Fore.MAGENTA + "You: " + Style.RESET_ALL + m["content"])
            elif m["role"] == "assistant":
                print(Fore.GREEN + "Assistant: " + Style.RESET_ALL + m["content"])

            print()

    while True:
        user_input = input(Fore.MAGENTA + "You: " + Style.RESET_ALL)
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
        print(
            Fore.GREEN + "\nAssistant: " + Style.RESET_ALL + assistant_message.strip(),
            end="\n\n",
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--persona", type=str, default=None, help="The persona of the chatbot."
    )
    parser.add_argument(
        "-l", "--load", type=str, default=None, help="The chat history to load."
    )
    args = parser.parse_args()

    while True:
        if not os.path.exists(BASE_PATH + "api_key.txt"):
            KEY = input(
                "Enter your OpenAI API key (https://platform.openai.com/account/api-keys): "
            )
            with open(BASE_PATH + "api_key.txt", "w") as f:
                f.write(KEY)

        with open(BASE_PATH + "api_key.txt", "r") as f:
            openai.api_key = f.read()

        if openai.api_key == "":
            print("Please enter a valid API key.")
            continue
        else:
            break
        
    start_chat(persona=args.persona, history_file_name=args.load)
