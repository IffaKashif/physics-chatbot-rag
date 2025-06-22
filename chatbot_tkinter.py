import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    # apply model inference code here
    # echo for an Example 
    return f"Bot: You said '{user_input}'"

def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    
    response = chatbot_response(user_input)
    chat_area.insert(tk.END, response + "\n\n")
    
    chat_area.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    chat_area.see(tk.END)

# Tkinter window setup
root = tk.Tk()
root.title("Chatbot UI")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=60, height=20)
chat_area.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0,10))

# Keyboard enter key bind
def enter_pressed(event):
    send_message()
    
user_entry.bind("<Return>", enter_pressed)

# Run the Tkinter main loop
root.mainloop()
