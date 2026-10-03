import tkinter as tk
from datetime import datetime


# ============================================================
#                     CHATBOT RULES
# ============================================================

RESPONSES = {
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! 😊 Nice to meet you.",
    "hey": "Hey! 👋 What can I do for you?",

    "how are you": "I'm doing great! 🤖 Thanks for asking.",
    "what are you doing": "I'm here and ready to chat with you! ✨",

    "your name": "I'm RuleBot 🤖 — your friendly rule-based assistant.",
    "who are you": "I'm RuleBot, a Python rule-based chatbot.",

    "what is python":
        "Python is a high-level programming language known for "
        "its simple syntax and wide range of applications.",

    "what is chatbot":
        "A chatbot is a computer program designed to communicate "
        "with users through text or voice.",

    "rule based":
        "A rule-based chatbot uses predefined keywords and rules "
        "to decide how it should respond.",

    "college project":
        "RuleBot is a great Python college project demonstrating "
        "rule-based logic, GUI design, and event handling.",

    "help":
        "I can answer questions about Python, chatbots, myself, "
        "the current time, date, greetings, and this project.",

    "thanks": "You're welcome! 💜",
    "thank you": "My pleasure! 😊",

    "bye": "Goodbye! 👋 Have an amazing day!",
    "goodbye": "See you later! 🚀"
}


# ============================================================
#                         COLORS
# ============================================================

BG = "#020617"

SIDEBAR = "#060A14"
CHAT_BG = "#050914"

WHITE = "#FFFFFF"
TEXT = "#DDE7FF"
MUTED = "#8993AD"

PURPLE = "#8B5CF6"
PURPLE_DARK = "#5B21B6"
PURPLE_LIGHT = "#B794FF"

BLUE = "#3B82F6"
BLUE_LIGHT = "#60A5FA"

CYAN = "#06B6D4"
CYAN_LIGHT = "#67E8F9"

PINK = "#EC4899"

GREEN = "#22C55E"
RED = "#EF4444"

CARD = "#111B32"
CARD2 = "#142442"

BORDER = "#253452"


# ============================================================
#                     MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("RuleBot • Futuristic AI Assistant")

root.geometry("1200x760")

root.minsize(
    900,
    620
)

root.configure(
    bg=BG
)


# ============================================================
#                 BACKGROUND GRADIENT
# ============================================================

background = tk.Canvas(
    root,
    bg=BG,
    highlightthickness=0
)

background.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)


def draw_gradient(canvas, width, height):

    canvas.delete("gradient")

    # --------------------------------------------------------
    # Midnight gradient
    # --------------------------------------------------------

    colors = [
        "#020617",
        "#031027",
        "#04152F",
        "#061A38",
        "#081D3D",
        "#0A1030",
        "#100A2B"
    ]

    steps = len(colors)

    for i, color in enumerate(colors):

        y1 = int(height * i / steps)
        y2 = int(height * (i + 1) / steps)

        canvas.create_rectangle(
            0,
            y1,
            width,
            y2 + 2,
            fill=color,
            outline="",
            tags="gradient"
        )

    # --------------------------------------------------------
    # Cyan glow - top left
    # --------------------------------------------------------

    canvas.create_oval(
        -250,
        -220,
        300,
        330,
        fill="#062F46",
        outline="",
        tags="gradient"
    )

    # --------------------------------------------------------
    # Blue glow - top right
    # --------------------------------------------------------

    canvas.create_oval(
        width - 420,
        -180,
        width + 150,
        380,
        fill="#101D58",
        outline="",
        tags="gradient"
    )

    # --------------------------------------------------------
    # Purple glow - bottom right
    # --------------------------------------------------------

    canvas.create_oval(
        width - 420,
        height - 350,
        width + 150,
        height + 200,
        fill="#281052",
        outline="",
        tags="gradient"
    )

    # --------------------------------------------------------
    # Cyan glow - bottom left
    # --------------------------------------------------------

    canvas.create_oval(
        -250,
        height - 280,
        250,
        height + 200,
        fill="#053B48",
        outline="",
        tags="gradient"
    )

    # --------------------------------------------------------
    # Center glow
    # --------------------------------------------------------

    canvas.create_oval(
        width * 0.25,
        height * 0.25,
        width * 0.75,
        height * 0.75,
        fill="#0A1230",
        outline="",
        tags="gradient"
    )


def resize_background(event):

    draw_gradient(
        background,
        event.width,
        event.height
    )


background.bind(
    "<Configure>",
    resize_background
)


# ============================================================
#                    CHATBOT ENGINE
# ============================================================

def get_response(message):

    text = message.lower().strip()

    if not text:
        return "Please type something first 😊"

    # Check predefined rules
    for keyword, response in RESPONSES.items():

        if keyword in text:
            return response

    # Time rule
    if "time" in text:

        return (
            "The current time is "
            + datetime.now().strftime("%I:%M %p")
            + ". ⏰"
        )

    # Date rule
    if "date" in text or "today" in text:

        return (
            "Today's date is "
            + datetime.now().strftime("%d %B %Y")
            + ". 📅"
        )

    # Default response
    return (
        "Hmm... I don't know that one yet. 🤔\n\n"
        "Try one of the quick questions or type "
        "'help' to see what I can answer."
    )


# ============================================================
#                    UTILITY FUNCTIONS
# ============================================================

def get_time():

    return datetime.now().strftime("%I:%M %p")


def scroll_bottom():

    chat_canvas.update_idletasks()

    chat_canvas.yview_moveto(1.0)


# ============================================================
#                     AVATAR
# ============================================================

def create_avatar(parent, emoji, color):

    avatar = tk.Canvas(
        parent,
        width=54,
        height=54,
        bg=CHAT_BG,
        highlightthickness=0
    )

    # Outer glow
    avatar.create_oval(
        0,
        0,
        54,
        54,
        fill="#111A35",
        outline=""
    )

    # Main circle
    avatar.create_oval(
        4,
        4,
        50,
        50,
        fill=color,
        outline=""
    )

    # Inner border
    avatar.create_oval(
        7,
        7,
        47,
        47,
        fill=color,
        outline="#D6C8FF",
        width=1
    )

    # Emoji
    avatar.create_text(
        27,
        27,
        text=emoji,
        font=("Segoe UI Emoji", 20)
    )

    return avatar


# ============================================================
#                  CHAT BUBBLE
# ============================================================

def create_chat_bubble(parent, message, sender):

    if sender == "bot":

        bubble_color = "#111D35"
        accent = PURPLE

    else:

        bubble_color = "#352080"
        accent = CYAN

    bubble = tk.Frame(
        parent,
        bg=bubble_color,
        padx=17,
        pady=12
    )

    # Accent strip
    accent_strip = tk.Frame(
        bubble,
        bg=accent,
        width=3
    )

    accent_strip.pack(
        side="left",
        fill="y",
        padx=(0, 10)
    )

    content = tk.Frame(
        bubble,
        bg=bubble_color
    )

    content.pack(
        side="left"
    )

    # Bot name
    if sender == "bot":

        tk.Label(
            content,
            text="RULEBOT",
            font=("Segoe UI", 8, "bold"),
            fg=PURPLE_LIGHT,
            bg=bubble_color
        ).pack(
            anchor="w",
            pady=(0, 4)
        )

    # Message
    tk.Label(
        content,
        text=message,
        font=("Segoe UI", 10),
        fg=TEXT if sender == "bot" else WHITE,
        bg=bubble_color,
        justify="left",
        wraplength=540
    ).pack(
        anchor="w"
    )

    # Timestamp
    tk.Label(
        content,
        text=get_time(),
        font=("Segoe UI", 8),
        fg=MUTED,
        bg=bubble_color
    ).pack(
        anchor="e",
        pady=(6, 0)
    )

    return bubble


# ============================================================
#                    ADD MESSAGE
# ============================================================

def add_message(message, sender="bot"):

    row = tk.Frame(
        chat_inner,
        bg=CHAT_BG
    )

    row.pack(
        fill="x",
        padx=25,
        pady=9
    )

    # --------------------------------------------------------
    # BOT MESSAGE
    # --------------------------------------------------------

    if sender == "bot":

        avatar = create_avatar(
            row,
            "🤖",
            PURPLE
        )

        avatar.pack(
            side="left",
            anchor="n",
            padx=(0, 10)
        )

        bubble = create_chat_bubble(
            row,
            message,
            "bot"
        )

        bubble.pack(
            side="left",
            anchor="w"
        )

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    else:

        bubble = create_chat_bubble(
            row,
            message,
            "user"
        )

        bubble.pack(
            side="right",
            anchor="e",
            padx=(10, 0)
        )

        avatar = create_avatar(
            row,
            "👤",
            BLUE
        )

        avatar.pack(
            side="right",
            anchor="n"
        )

    root.after(
        50,
        scroll_bottom
    )


# ============================================================
#                    SEND MESSAGE
# ============================================================

def send_message(event=None):

    message = entry.get().strip()

    if not message:
        return

    # Add user message
    add_message(
        message,
        "user"
    )

    # Clear input
    entry.delete(
        0,
        tk.END
    )

    # Bot response
    root.after(
        400,
        lambda: add_message(
            get_response(message),
            "bot"
        )
    )


# ============================================================
#                   QUICK QUESTION
# ============================================================

def quick_message(message):

    entry.delete(
        0,
        tk.END
    )

    entry.insert(
        0,
        message
    )

    send_message()


# ============================================================
#                     CLEAR CHAT
# ============================================================

def clear_chat():

    for widget in chat_inner.winfo_children():

        widget.destroy()

    add_message(
        "Chat cleared! ✨\n\n"
        "I'm ready for a fresh conversation. "
        "What would you like to ask?",
        "bot"
    )


# ============================================================
#                       EXIT
# ============================================================

def exit_app():

    root.destroy()


# ============================================================
#                       SIDEBAR
# ============================================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=290
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# ============================================================
#                       LOGO
# ============================================================

logo_area = tk.Frame(
    sidebar,
    bg=SIDEBAR
)

logo_area.pack(
    padx=24,
    pady=(28, 10),
    anchor="w"
)


logo = tk.Canvas(
    logo_area,
    width=70,
    height=70,
    bg=SIDEBAR,
    highlightthickness=0
)

logo.pack(
    side="left"
)


# Outer glow
logo.create_oval(
    1,
    1,
    69,
    69,
    fill="#162047",
    outline=""
)


# Main circle
logo.create_oval(
    7,
    7,
    63,
    63,
    fill=PURPLE,
    outline=CYAN_LIGHT,
    width=2
)


# Robot
logo.create_text(
    35,
    35,
    text="🤖",
    font=("Segoe UI Emoji", 26)
)


# Logo text
logo_text = tk.Frame(
    logo_area,
    bg=SIDEBAR
)

logo_text.pack(
    side="left",
    padx=12
)


tk.Label(
    logo_text,
    text="RuleBot",
    font=("Segoe UI", 21, "bold"),
    fg=WHITE,
    bg=SIDEBAR
).pack(
    anchor="w"
)


tk.Label(
    logo_text,
    text="NEON AI ASSISTANT",
    font=("Segoe UI", 8, "bold"),
    fg=CYAN_LIGHT,
    bg=SIDEBAR
).pack(
    anchor="w"
)


# ============================================================
#                       DIVIDER
# ============================================================

tk.Frame(
    sidebar,
    height=1,
    bg=BORDER
).pack(
    fill="x",
    padx=22,
    pady=22
)


# ============================================================
#                   QUICK QUESTIONS
# ============================================================

tk.Label(
    sidebar,
    text="QUICK QUESTIONS",
    font=("Segoe UI", 9, "bold"),
    fg=MUTED,
    bg=SIDEBAR
).pack(
    padx=25,
    anchor="w"
)


quick_frame = tk.Frame(
    sidebar,
    bg=SIDEBAR
)

quick_frame.pack(
    fill="x",
    padx=17,
    pady=10
)


quick_questions = [
    ("👋", "Say Hello", "Hello"),
    ("🐍", "What is Python?", "What is Python?"),
    ("🤖", "What is a chatbot?", "What is a chatbot?"),
    ("⏰", "Current Time", "What is the time?"),
    ("📅", "Today's Date", "What is today's date?"),
    ("❓", "Show Help", "Help")
]


for icon, title, question in quick_questions:

    button = tk.Button(
        quick_frame,
        text=f"  {icon}   {title}",
        command=lambda q=question: quick_message(q),
        bg=SIDEBAR,
        fg=TEXT,
        activebackground=CARD2,
        activeforeground=WHITE,
        font=("Segoe UI", 10),
        relief="flat",
        borderwidth=0,
        cursor="hand2",
        anchor="w",
        padx=12,
        pady=10
    )

    button.pack(
        fill="x",
        pady=2
    )


# ============================================================
#                       DIVIDER
# ============================================================

tk.Frame(
    sidebar,
    height=1,
    bg=BORDER
).pack(
    fill="x",
    padx=22,
    pady=20
)


# ============================================================
#                         ABOUT
# ============================================================

tk.Label(
    sidebar,
    text="ABOUT",
    font=("Segoe UI", 9, "bold"),
    fg=MUTED,
    bg=SIDEBAR
).pack(
    padx=25,
    anchor="w"
)


tk.Label(
    sidebar,
    text=(
        "RuleBot uses predefined keywords\n"
        "and rules to generate responses.\n\n"
        "Built with Python + Tkinter.\n"
        "No API required."
    ),
    font=("Segoe UI", 9),
    fg=MUTED,
    bg=SIDEBAR,
    justify="left"
).pack(
    padx=25,
    pady=10,
    anchor="w"
)


# ============================================================
#                    SIDEBAR BUTTONS
# ============================================================

bottom = tk.Frame(
    sidebar,
    bg=SIDEBAR
)

bottom.pack(
    side="bottom",
    fill="x",
    padx=20,
    pady=20
)


# Clear
clear_button = tk.Button(
    bottom,
    text="🗑   CLEAR CHAT",
    command=clear_chat,
    bg=CARD2,
    fg=TEXT,
    activebackground="#283A60",
    activeforeground=WHITE,
    relief="flat",
    font=("Segoe UI", 9, "bold"),
    cursor="hand2",
    pady=11
)

clear_button.pack(
    fill="x",
    pady=4
)


# Exit
exit_button = tk.Button(
    bottom,
    text="✕   EXIT",
    command=exit_app,
    bg="#29121D",
    fg="#FDA4AF",
    activebackground="#421725",
    activeforeground=WHITE,
    relief="flat",
    font=("Segoe UI", 9, "bold"),
    cursor="hand2",
    pady=11
)

exit_button.pack(
    fill="x",
    pady=4
)


# ============================================================
#                     MAIN CHAT AREA
# ============================================================

main = tk.Frame(
    root,
    bg=CHAT_BG
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# ============================================================
#                         HEADER
# ============================================================

header = tk.Frame(
    main,
    bg=CHAT_BG,
    height=90
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


header_left = tk.Frame(
    header,
    bg=CHAT_BG
)

header_left.pack(
    side="left",
    padx=30,
    pady=17
)


tk.Label(
    header_left,
    text="RuleBot Assistant",
    font=("Segoe UI", 20, "bold"),
    fg=WHITE,
    bg=CHAT_BG
).pack(
    anchor="w"
)


# Online status
status = tk.Frame(
    header_left,
    bg=CHAT_BG
)

status.pack(
    anchor="w",
    pady=(3, 0)
)


tk.Label(
    status,
    text="●",
    font=("Arial", 10),
    fg=GREEN,
    bg=CHAT_BG
).pack(
    side="left"
)


tk.Label(
    status,
    text=" Online • Ready to chat",
    font=("Segoe UI", 9),
    fg=MUTED,
    bg=CHAT_BG
).pack(
    side="left"
)


# Header badge
tk.Label(
    header,
    text="✦  RULE-BASED AI  ✦",
    font=("Segoe UI", 9, "bold"),
    fg=CYAN_LIGHT,
    bg=CHAT_BG
).pack(
    side="right",
    padx=30
)


# Header divider
tk.Frame(
    main,
    height=1,
    bg=BORDER
).pack(
    fill="x"
)


# ============================================================
#                     CHAT CONTAINER
# ============================================================

chat_container = tk.Frame(
    main,
    bg=CHAT_BG
)

chat_container.pack(
    fill="both",
    expand=True
)


# Canvas
chat_canvas = tk.Canvas(
    chat_container,
    bg=CHAT_BG,
    highlightthickness=0
)


# Scrollbar
scrollbar = tk.Scrollbar(
    chat_container,
    orient="vertical",
    command=chat_canvas.yview,
    bg=CHAT_BG,
    troughcolor=CHAT_BG,
    activebackground=PURPLE,
    relief="flat"
)


# Inner frame
chat_inner = tk.Frame(
    chat_canvas,
    bg=CHAT_BG
)


chat_window = chat_canvas.create_window(
    (0, 0),
    window=chat_inner,
    anchor="nw"
)


def update_scroll(event=None):

    chat_canvas.configure(
        scrollregion=chat_canvas.bbox("all")
    )


def resize_chat(event):

    chat_canvas.itemconfig(
        chat_window,
        width=event.width
    )


chat_inner.bind(
    "<Configure>",
    update_scroll
)

chat_canvas.bind(
    "<Configure>",
    resize_chat
)

chat_canvas.configure(
    yscrollcommand=scrollbar.set
)


chat_canvas.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar.pack(
    side="right",
    fill="y"
)


# ============================================================
#                     WELCOME MESSAGE
# ============================================================

add_message(
    "Hey there! 👋\n\n"
    "Welcome to RuleBot — your futuristic "
    "rule-based Python chatbot.\n\n"
    "Ask me about Python, chatbots, the time, "
    "the date, or choose a quick question. ✨",
    "bot"
)


# ============================================================
#                      INPUT AREA
# ============================================================

input_area = tk.Frame(
    main,
    bg=CHAT_BG
)

input_area.pack(
    fill="x",
    padx=25,
    pady=(8, 4)
)


# Neon outer border
input_glow = tk.Frame(
    input_area,
    bg="#243B82",
    padx=2,
    pady=2
)

input_glow.pack(
    fill="x"
)


# Input box
input_box = tk.Frame(
    input_glow,
    bg=CARD,
    padx=10,
    pady=8
)

input_box.pack(
    fill="x"
)


# Emoji button
emoji_button = tk.Button(
    input_box,
    text="😊",
    bg=CARD,
    fg=MUTED,
    activebackground=CARD,
    activeforeground=WHITE,
    relief="flat",
    borderwidth=0,
    font=("Segoe UI Emoji", 15),
    cursor="hand2",
    command=lambda: entry.insert(tk.END, " 😊")
)

emoji_button.pack(
    side="left",
    padx=(2, 8)
)


# Text entry
entry = tk.Entry(
    input_box,
    bg=CARD,
    fg=TEXT,
    insertbackground=CYAN_LIGHT,
    font=("Segoe UI", 11),
    relief="flat",
    bd=0
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)


# Send button
send_button = tk.Button(
    input_box,
    text="➤",
    command=send_message,
    bg=PURPLE,
    fg=WHITE,
    activebackground=PINK,
    activeforeground=WHITE,
    relief="flat",
    borderwidth=0,
    font=("Segoe UI", 15, "bold"),
    cursor="hand2",
    width=3,
    pady=4
)

send_button.pack(
    side="right",
    padx=(8, 0)
)


# Enter key
entry.bind(
    "<Return>",
    send_message
)


# ============================================================
#                         FOOTER
# ============================================================

tk.Label(
    main,
    text="RuleBot  •  Python + Tkinter  •  Powered by predefined rules",
    font=("Segoe UI", 8),
    fg="#52617E",
    bg=CHAT_BG
).pack(
    pady=(2, 9)
)


# ============================================================
#                         START
# ============================================================

entry.focus()

root.mainloop()
