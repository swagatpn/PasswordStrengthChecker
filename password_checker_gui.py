import re
import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    suggestions = []

    if not length_criteria:
        suggestions.append("Increase password length (8+ characters).")
    if not uppercase_criteria:
        suggestions.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Add at least one lowercase letter.")
    if not digit_criteria:
        suggestions.append("Include at least one number.")
    if not special_char_criteria:
        suggestions.append("Use at least one special character.")

    return score, suggestions

def evaluate_password(*args):
    password = password_entry.get()
    score, suggestions = check_password_strength(password)
    
    strength_bar['value'] = score * 20  
    strength_label.config(text=f"Strength: {['Weak', 'Moderate', 'Strong'][min(score // 2, 2)]}")
    suggestion_text = "\n".join(suggestions) if suggestions else "Great job!"
    suggestions_label.config(text=suggestion_text)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="👁️")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="🔒")

def generate_password():
    length = 12  # Default length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    evaluate_password()

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x500")
root.resizable(False, False)


# Header
header_label = ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

# Password Entry Frame
password_frame = ttk.Frame(root)
password_frame.pack(pady=10)

password_entry = ttk.Entry(password_frame, show="*", font=("Helvetica", 12), width=25)
password_entry.pack(side="left", padx=5)
password_entry.bind("<KeyRelease>", evaluate_password)

toggle_button = ttk.Button(password_frame, text="🔒", command=toggle_password_visibility, width=3)
toggle_button.pack(side="right")

# Strength Bar
strength_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=100)
strength_bar.pack(pady=10)

# Strength Label
strength_label = ttk.Label(root, text="Strength: ", font=("Helvetica", 12))
strength_label.pack(pady=10)

# Suggestions Label
suggestions_label = ttk.Label(root, text="", font=("Helvetica", 10), wraplength=350)
suggestions_label.pack(pady=10)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

copy_button = ttk.Button(button_frame, text="Copy Password", command=copy_to_clipboard)
copy_button.pack(side="left", padx=5)

generate_button = ttk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side="right", padx=5)

# Signature
signature_label = ttk.Label(root, text="Crafted by Swagat", font=("Helvetica", 9, "italic"), foreground="gray")
signature_label.pack(side="bottom", pady=5)

# Run the App
root.mainloop()
