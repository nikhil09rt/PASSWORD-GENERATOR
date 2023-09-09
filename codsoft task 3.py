#TASK 3:- PASSWOD GENRATOR


import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar()
        self.complexity_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        length_label = tk.Label(self.root, text="Password Length:")
        length_label.pack()

        length_entry = tk.Entry(self.root, textvariable=self.length_var)
        length_entry.pack()

        complexity_label = tk.Label(self.root, text="Password Complexity:")
        complexity_label.pack()

        complexity_combo = ttk.Combobox(self.root, textvariable=self.complexity_var, values=["Low", "Medium", "High"])
        complexity_combo.pack()

        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack()

        password_label = tk.Label(self.root, text="Generated Password:")
        password_label.pack()

        password_entry = tk.Entry(self.root, textvariable=self.password_var)
        password_entry.pack()

    def generate_password(self):
        complexity = self.complexity_var.get()
        length = self.length_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

def main():
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
