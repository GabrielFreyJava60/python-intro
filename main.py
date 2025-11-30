import requests


URL: str = "http://localhost:11434/api/chat"
MODEL_NAME: str = "phi3"


def chatRequest(messages: dict) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }
    resp = requests.post(URL, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]


def main():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistance. Answer briefly and clearly"
        }
    ]
    print("Phi-3 simple chat. Type 'exit' for quit")
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print('bye')
            break
        messages.append({"role": "user", "content": user_input})
        reply = chatRequest(messages)
        messages.append({"role": "assistant", "content": reply})
        print("\nAgent: ", reply)
        print("_" * 60)


if __name__ == "__main__":
    main()
