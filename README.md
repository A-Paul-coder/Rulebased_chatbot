🤖 RuleBot — Futuristic Rule-Based Chatbot

A modern, futuristic rule-based chatbot built with Python and Tkinter.

RuleBot uses predefined keywords and simple rule-based logic to understand user messages and provide appropriate responses. It features a modern neon interface with gradient backgrounds, chat bubbles, circular avatars, quick-question buttons, and a responsive chat area.

✨ Features

🤖 Rule-based chatbot using Python

💬 Modern chat-bubble interface

🌌 Futuristic gradient background

🟣 Purple, blue, and cyan neon theme

🤖 Circular chatbot logo

👤 Circular user avatar

🟢 Online status indicator

⚡ Quick-question buttons

⌨️ Press Enter to send messages

😊 Emoji button

🕐 Message timestamps

📜 Scrollable chat history

🗑 Clear chat button

✕ Exit button

📱 Resizable application window

🔌 No internet connection required

📦 No external Python packages required

🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Tkinter	Graphical User Interface
Datetime	Message timestamps and date/time responses
🧠 How the Chatbot Works

RuleBot uses simple keyword-based rules.

For example:

RESPONSES = {
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! 😊 Nice to meet you.",
    "what is python": "Python is a high-level programming language."
}


When the user enters a message, RuleBot converts it to lowercase and checks whether any predefined keyword exists in the message.

Example:

User:
What is Python?

        ↓

RuleBot checks:
"what is python"

        ↓

Matching rule found

        ↓

Bot:
Python is a high-level programming language...


If no matching rule is found, the chatbot displays a default response.

📂 Project Structure
RuleBot/
│
├── chatbot.py
├── requirements.txt
└── README.md

chatbot.py

Contains the complete chatbot application, including:

Chatbot rules

Response engine

Tkinter interface

Gradient background

Chat bubbles

Avatars

Quick questions

Input handling

requirements.txt

Lists the project dependencies.

This project does not require external Python packages.

README.md

Project documentation and instructions.

💻 Requirements

Python 3.x

Tkinter

Windows, macOS, or Linux

Tkinter is normally included with Python.

You can check whether Tkinter is installed with:

python -m tkinter


If a small Tkinter window appears, Tkinter is working correctly.

🚀 Installation
1. Clone or download the project

Download the project files to your computer.

2. Open the project folder
cd RuleBot

3. Run the chatbot
python chatbot.py


On some systems, you may need:

python3 chatbot.py

💬 Example Questions

You can ask RuleBot questions such as:

Hello
Hi
How are you?
What is your name?
Who are you?
What is Python?
What is a chatbot?
What is rule based?
What is the time?
What is today's date?
Help
Thank you
Bye


You can also use the Quick Questions buttons in the sidebar.

🎨 User Interface

The application includes a futuristic dark interface with:

Midnight gradient background

Cyan and blue glow effects

Purple neon accents

Circular robot logo

Bot and user avatars

Modern message bubbles

Neon input area

Quick-action sidebar

Example layout:

┌────────────────────────────────────────────────────────────┐
│  🤖 RuleBot                         ✦ RULE-BASED AI ✦     │
│     ● Online • Ready to chat                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  🤖  ┌─────────────────────────────────────┐               │
│      │ RULEBOT                             │               │
│      │ Hello! 👋 How can I help you?      │               │
│      └─────────────────────────────────────┘               │
│                                                            │
│                       ┌────────────────────────┐  👤       │
│                       │ What is Python?        │           │
│                       └────────────────────────┘           │
│                                                            │
│  🤖  ┌─────────────────────────────────────┐               │
│      │ Python is a high-level programming │               │
│      │ language...                         │               │
│      └─────────────────────────────────────┘               │
│                                                            │
├────────────────────────────────────────────────────────────┤
│       😊  Type your message...                    ➤       │
└────────────────────────────────────────────────────────────┘

🧩 Customizing the Chatbot

You can easily add new responses by modifying the RESPONSES dictionary in chatbot.py.

For example:

RESPONSES = {
    "hello": "Hello! 👋",
    "what is java": "Java is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "college": "This is my Python chatbot project."
}


You can add as many rules as you want.

🔄 Example Interaction
User:
Hello

RuleBot:
Hello! 👋 How can I help you today?


User:
What is Python?

RuleBot:
Python is a high-level programming language known
for its simple syntax and wide range of applications.


User:
What is the time?

RuleBot:
The current time is 09:30 PM. ⏰

🎓 Project Objective

The main objective of this project is to demonstrate how a rule-based chatbot can be created using Python.

The project demonstrates:

Python programming

Conditional logic

Dictionary-based rules

String processing

Event-driven programming

GUI development using Tkinter

User input handling

Dynamic UI updates

📚 Learning Outcomes

After completing this project, you will understand:

How a basic chatbot works.

How keyword matching can be used for conversation.

How dictionaries can store chatbot rules.

How to create a GUI using Tkinter.

How to handle button and keyboard events.

How to create a scrollable chat interface.

How to customize a Python GUI with colors and visual effects.


👨‍💻 Project

Project: Rule-Based Chatbot
Language: Python
GUI: Tkinter
Type: Desktop Application
Status: Completed


You can place this file alongside `chatbot.py` and `requirements.txt`:

```text
RuleBot/
├── chatbot.py
├── requirements.txt
└── README.md
