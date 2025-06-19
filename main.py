import requests
import json

messages = [{
    "role": "system",
    "content": "You are a terminal-based assistant. Do not use formatting like italics, bold, or markdown. You can use emojis 😊 and line breaks.\nRespond in plain text only."
}]

using = True
while using == True:
    msg = input()
    messages.append({"role": "user", "content": msg})

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer YOURAPIKEY",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "google/gemma-3-27b-it:free",
            "messages": messages
        })
    )

    reply = response.json()['choices'][0]['message']['content']
    print(reply)
    messages.append({"role": "assistant", "content": reply})
