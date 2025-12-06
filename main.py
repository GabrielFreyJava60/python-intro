import requests
import re
import json
from system_content import SYSTEM_CONTENT
from tools import TOOLS
from thinking_dots import start_thinking_dots


URL: str = "http://localhost:11434/api/chat"
MODEL_NAME: str = "phi3"


def chatRequest(messages: dict) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {"temperature": 0.0}
    }
    resp = requests.post(URL, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]


def extractJSON(text: str, properties: list[str] = None) -> dict | None:
    if properties is None:
        properties = ["tool", "arguments"]
    
    regex: str = r"\{[^{}]*\}"
    match: re.Match = re.search(regex, text, re.DOTALL)
    res = None
    if match:
        try:
            data = json.loads(match.group())
            res = {}
            for prop in properties:
                if prop in data:
                    res[prop] = data[prop]
            if not res:
                res = None
        except Exception:
            pass
    return res


def callTool(toolData: dict) -> str:
    res: str = ""
    method = TOOLS.get(toolData.get("tool"))
    if method:
        arguments = toolData.get("arguments", {})
        res = method(**arguments)
    return res


def processLLM(text: str) -> dict:
    res: dict = {"role": "assistant", "content": text}
    toolData: dict | None = extractJSON(text)
    if toolData:
        toolRes = callTool(toolData)
        if toolRes:
            res = {"role": "tool", "content": json.dumps({"result": toolRes})}
    return res


def main():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_CONTENT
        }
    ]
    print("Phi-3 simple chat. Type 'exit' for quit")
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print('bye')
            break
        messages.append({"role": "user", "content": user_input})
        stopEvent = start_thinking_dots("Model Thinking", 0.5)
        reply = chatRequest(messages)
        stopEvent.set()
        response: dict = processLLM(reply)
        messages.append(response)
        print("\nAgent: ", response["content"] if response["role"] == "assistant" else json.loads(response["content"])["result"])
        print("_" * 60)


if __name__ == "__main__":
    main()
