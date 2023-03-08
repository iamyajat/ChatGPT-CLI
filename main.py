import openai
import os
import json
import argparse
import pickle

#  load api key from a file
openai.api_key_path = "./api_key.txt"
print("API key loaded from:", openai.api_key_path)
print("API Key: ", openai.api_key, end="\n\n")


# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a school teacher who teaches algebra. You are teaching a lesson on solving quadratic equations. You are in the middle of the lesson and you are explaining how to solve a quadratic equation by factoring."},
#         {"role": "user", "content": "What is a quadratic equation?"},
#         {"role": "assistant", "content": "A quadratic equation is an equation that can be written in the form ax^2 + bx + c = 0, where a, b, and c are real numbers and a is not equal to 0."},
#         {"role": "user", "content": "Can you give me some questions to solve?"}
#     ]
# )

# print(response)

# response
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Sure, here are some quadratic equations for you to solve by factoring:\n\n1. x^2 + 5x + 6 = 0\n2. 2x^2 + 7x - 15 = 0\n3. 3x^2 - 10x + 7 = 0\n4. 4x^2 - 12x + 9 = 0\n5. x^2 - 9x + 20 = 0\n\nTo solve each equation, you can follow these steps:\n\n1. Try to factor the quadratic equation into two binomials of the form (px + q)(rx + s).\n2. Set each binomial equal to zero and solve for x.\n3. Check your solutions by plugging them back into the original equation to ensure they work.",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1678300480,
#   "id": "chatcmpl-6rsuWYQ2OPVNo2M6sfdEoHlwRI1NX",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 172,
#     "prompt_tokens": 121,
#     "total_tokens": 293
#   }
# }

# persona is a base prompt which will be given to the model as "system" messages. It defines the context of the conversation.
# persona[0] = {
#   "name": "school-teacher",
#   "prompt": "You are a school teacher who loves answering questions raised by students."
# }
# saved in "./personas.json"


def create_personas():
    with open("personas.json", "r") as f:
        personas = json.load(f)

    #  input a new persona
    new_persona = {}
    new_persona["name"] = input("Enter the name of the persona: ")
    new_persona["prompt"] = input("Enter the prompt for the persona: ")
    personas.append(new_persona)

    #  save the new persona
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


def start_chat(persona="school-teacher"):
    print("\nWelcome to the ChatGPT! Please ask me a question.")
    print("Type 'quit' to exit the chatbot.")
    print("Type 'clear' to clear the chat history.", end="\n\n")

    persona_def = get_persona_prompt(persona)

    messages = [{"role": "system", "content": persona_def}]
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            save_chat_history(messages)
            break
        elif user_input == "clear":
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

    start_chat(persona=args.persona)
