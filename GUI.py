from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Speech_to_Text
import Action
import subprocess
import os
import webbrowser

# Functions
def ask():
    text.delete(1.0, END)
    query = Speech_to_Text.Speech_to_Text()
    if query:
        response = Action.Action(query)
        text.insert(END, f"You said: {query}\nAssistant: {response}\n")

def send():
    user_input = entry.get()
    if user_input.strip():
        response = Action.Action(user_input)
        text.insert(END, f"You: {user_input}\nAssistant: {response}\n")
        entry.delete(0, END)

def delete():
    text.delete(1.0, END)
    entry.delete(0, END)

def play_chess():
    try:
        script_path = os.path.join(os.path.dirname(__file__), "FlaskChess", "flask_app.py")
        subprocess.Popen(["python", script_path], shell=True)
        webbrowser.open("http://127.0.0.1:5000")
    except Exception as e:
        print(f"Failed to launch chess game: {e}")

def detect_image():
    try:
        script_path = os.path.join(os.path.dirname(__file__), "gad", "gad.py")
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Create Main Window
root = Tk()
root.title("AI Assistant")
root.geometry("700x800")
root.resizable(False, False)
root.config(bg="#121212")

# Centering the Window
screen_width = root.winfo_screenwidth()
window_width = 700
x = (screen_width // 2) - (window_width // 2)
root.geometry(f"{window_width}x800+{x}+30")

# Fonts and Colors
HEADER_FONT = ("Segoe UI", 22, "bold")
TEXT_FONT = ("Consolas", 11)
TEXT_COLOR = "#FFFFFF"
FRAME_BG = "#1F1F2E"
TEXT_BG = "#2C2F4A"
ENTRY_BG = "#1B1D2A"

# Header Frame
frame = Frame(root, bg=FRAME_BG, bd=2, relief="groove")
frame.place(x=150, y=20, width=400, height=80)
header_label = Label(frame, text="🤖 AI ASSISTANT", font=HEADER_FONT, bg=FRAME_BG, fg=TEXT_COLOR)
header_label.pack(pady=20)

# Image
image = Image.open("Images/Assistant.webp")
image = image.resize((280, 280), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)
image_label = Label(root, image=image, bg="#121212")
image_label.place(x=210, y=110)

# Text Output
text = Text(root, font=TEXT_FONT, bg=TEXT_BG, fg=TEXT_COLOR, wrap=WORD, bd=1, relief="solid")
text.place(x=100, y=420, width=500, height=120)

# Entry Field
entry = Entry(root, font=("Segoe UI", 11), bg=ENTRY_BG, fg=TEXT_COLOR, justify="center", bd=1, relief="solid", insertbackground=TEXT_COLOR)
entry.place(x=150, y=560, width=400, height=35)

# Button Styling with ttk
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TButton",
                font=("Segoe UI", 10, "bold"),
                foreground="white",
                background="#3D5AFE",
                padding=10,
                borderwidth=0)
style.map("Custom.TButton",
          background=[("active", "#5C6BC0")])

# Buttons Row 1
ask_btn = ttk.Button(root, text="🎤 ASK", style="Custom.TButton", command=ask)
ask_btn.place(x=90, y=620, width=150, height=40)

delete_btn = ttk.Button(root, text="🧹 DELETE", style="Custom.TButton", command=delete)
delete_btn.place(x=270, y=620, width=180, height=40)  # Increased width

send_btn = ttk.Button(root, text="📩 SEND", style="Custom.TButton", command=send)
send_btn.place(x=480, y=620, width=150, height=40)

# Buttons Row 2
chess_btn = ttk.Button(root, text="🎮 PLAY CHESS", style="Custom.TButton", command=play_chess)
chess_btn.place(x=130, y=690, width=200, height=40)  # Increased width

detect_btn = ttk.Button(root, text="🧠 DETECT IMAGE", style="Custom.TButton", command=detect_image)
detect_btn.place(x=370, y=690, width=200, height=40)

# Run the GUI
root.mainloop()
