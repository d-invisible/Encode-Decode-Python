import tkinter as tk
from tkinter import ttk

def encode_message(message):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            else:
                encoded_message += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        else:
            encoded_message += char
    return encoded_message

def decode_message(message):
    decoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                decoded_message += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            else:
                decoded_message += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        else:
            decoded_message += char
    return decoded_message

def process_message():
    user_input = entry.get()
    if user_input:
        if operation.get() == "Encode":
            result.set(encode_message(user_input))
        elif operation.get() == "Decode":
            result.set(decode_message(user_input))
    else:
        result.set("Please enter a message.")

# Create the main window
window = tk.Tk()
window.title("Encode/Decode Tool - Dark Mode")
window.geometry("400x300")
window.configure(bg="#333")

# Style
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="black")
style.configure("TLabel", padding=6, background="#333", foreground="white")
style.configure("TCombobox", fieldbackground="#444", background="#444", foreground="white", arrowcolor="white")

# Create and place widgets with dark mode styling
tk.Label(window, text="Enter Message:", font=("Helvetica", 12), bg="#333", fg="white").pack(pady=5)
entry = tk.Entry(window, width=30, font=("Helvetica", 12), bg="#444", fg="white", insertbackground="white")
entry.pack(pady=5)

tk.Label(window, text="Choose Operation:", font=("Helvetica", 12), bg="#333", fg="white").pack(pady=5)
operation = tk.StringVar()
operation.set("Encode")
operation_menu = ttk.Combobox(window, textvariable=operation, values=["Encode", "Decode"], state="readonly", font=("Helvetica", 12), style="TCombobox")
operation_menu.pack(pady=5)

process_button = ttk.Button(window, text="Process", command=process_message, style="TButton")
process_button.pack(pady=10)

tk.Label(window, text="Result:", font=("Helvetica", 12), bg="#333", fg="white").pack(pady=5)
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Helvetica", 12), bg="#333", fg="white")
result_label.pack(pady=5)

# Start the main loop
window.mainloop()
