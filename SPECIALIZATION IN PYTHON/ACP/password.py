import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

# Password Length Label
tk.Label(root, text="Enter Password Length:").pack(pady=5)

# Length Entry
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "8")  # Default length

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Password Display
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=10)

# Run Application
root.mainloop()