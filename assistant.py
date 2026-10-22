import os
import tkinter as tk
import webbrowser
from datetime import datetime

def submit():
    value = entry.get().strip().lower()

    if value == "":
        return

    chat.insert(tk.END, f"You: {value}\n")

    chat.see(tk.END)

    if value == "time":
        current_time = datetime.now().strftime("%I:%M:%S:%p")
        chat.insert(tk.END, f"Assistant: The current time is {current_time}\n")

    elif value == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        chat.insert(tk.END, f"Assistant: Today's date is {current_date}\n")

    elif value == "open chrome":
        chat.insert(tk.END, "Assistant: Opening Chrome...\n")
        # Make sure Chrome is installed on your computer
        os.system("start chrome")

    elif value == "open notepad":
        chat.insert(tk.END, "Assistant: Opening Notepad...\n")
        os.system("start notepad")

    elif value == "open apex":
        chat.insert(tk.END, "Assistant: Opening Apex...\n")
        os.system("start https://apex-goalstriker-b6453dc0.base44.app/")

    elif value == "open spotify":
        chat.insert(tk.END, "Assistant: Opening Spotify...\n")
        # Make sure Spotify is installed on your computer
        os.system("start spotify")

    elif value == "open word":
        chat.insert(tk.END, "Assistant: Opening Word...\n")
        # Make sure Microsoft Word is installed on your computer
        os.system("start winword")

    elif value == "open downloads":
        chat.insert(tk.END, "Assistant: Opening Downloads...\n")
        # Replace this with your own Downloads folder path
        os.startfile(r"D:\download")
   
    elif value == "open cursor":
        chat.insert(tk.END, "Assistant: Opening Cursor...\n")
        # Make sure Cursor is installed and accessible through Windows
        os.system("start Cursor")

    elif value == "open documents":
        chat.insert(tk.END, "Assistant: Opening Documents...\n")
        # Replace this with your own Documents folder path
        os.startfile(r"C:\Users\fajun\OneDrive\Documents")

    elif value == "open figma":
        chat.insert(tk.END, "Assistant: Opening Figma...\n")
         # Replace this with the path to your Figma executable
        os.startfile(r"C:\Users\fajun\AppData\Local\Figma\Figma.exe")

    elif value == "open ccbp":
        chat.insert(tk.END, "Assistant: Opening CCBP...\n")
        # Personal learning portal — replace with your own portal URL if needed
        webbrowser.open("https://learning.ccbp.in")

    elif value == "open chat gpt":
        chat.insert(tk.END, "Assistant: Opening Chat gpt...\n")
        webbrowser.open("https://chatgpt.com/")

    elif value.startswith("open website "):
       
        website = value.replace("open website ", "")
        chat.insert(tk.END, f"Assistant: Opening {website}...\n")
        webbrowser.open(f"https://www.{website}.com")

    elif value == "help":
        chat.insert(tk.END, "Assistant: Available commands:\n")
        chat.insert(tk.END, "- open chrome\n")
        chat.insert(tk.END, "- open notepad\n")
        chat.insert(tk.END, "- open figma\n")
        chat.insert(tk.END, "- open downloads\n")
        chat.insert(tk.END, "- open documents\n")
        chat.insert(tk.END, "- open website github\n")
        chat.insert(tk.END, "- open website youtube\n")

    

    

    else:
        chat.insert(tk.END, "Assistant: I don't know that command yet.\n")

    if value == "clear":
        chat.delete(1.0, tk.END)

    entry.delete(0, tk.END)

    

window = tk.Tk()
window.title("Desktop Assistant")
window.configure(bg="black")

window.geometry("500x400")

label = tk.Label(window, text="Hello Fajunnisha!", bg="black", fg="white")
label.pack()

label = tk.Label(window, text="What's on your mind today?", bg="black", fg="white")
label.pack()

chat_frame = tk.Frame(window, bg="black")
chat_frame.pack()

chat = tk.Text(chat_frame, height=15, width=50, bg="#1e1e1e", fg="white")
chat.pack(side="left")



scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side="right", fill="y")

scrollbar.config(command=chat.yview)

chat.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(window, bg="#2d2d2d", fg="white", insertbackground="white")
entry.pack()

button = tk.Button(window, text="Submit", bg="white", fg="black", command=submit)
button.pack()

window.bind("<Return>", lambda event: submit())

window.mainloop()