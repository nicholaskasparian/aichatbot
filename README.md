**Terminal Chatbot AI using OpenRouter**

This is a simple terminal-based chatbot that runs on your computer. It uses a powerful free language model from Meta, provided through the OpenRouter platform. You can type messages and it will reply intelligently, keeping context of your conversation.

**How to get a free OpenRouter API key**

Go to https://openrouter.ai

Click "Sign in" using your Google or GitHub account

After signing in, go to https://openrouter.ai/keys

Click "Create key" and give it a name like "chatbot"

Copy the key that appears. It will look something like:
sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Open the Python file and paste your API key into the line that says "Authorization"

For example:
"Authorization": "Bearer YOURAPIKEY"

**How it works**

You can type messages and the chatbot will reply

It remembers what you've said during the session
