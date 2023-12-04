import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.use_letters_var = tk.BooleanVar(value=True)
        self.use_numbers_var = tk.BooleanVar(value=True)
        self.use_symbols_var = tk.BooleanVar(value=True)

        # GUI Elements
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(root, textvariable=self.length_var, width=5).grid(row=0, column=1, padx=10, pady=5)

        ttk.Checkbutton(root, text="Include Letters", variable=self.use_letters_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        ttk.Button(root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        use_letters = self.use_letters_var.get()
        use_numbers = self.use_numbers_var.get()
        use_symbols = self.use_symbols_var.get()

        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "At least one character set (letters, numbers, symbols) must be selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.show_password(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def show_password(self, password):
        self.password_var = tk.StringVar(value=password)
        password_window = tk.Toplevel(self.root)
        password_window.title("Generated Password")

        ttk.Label(password_window, text="Your generated password is:").pack(padx=10, pady=5)
        ttk.Entry(password_window, textvariable=self.password_var, state="readonly", width=30).pack(padx=10, pady=5)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
