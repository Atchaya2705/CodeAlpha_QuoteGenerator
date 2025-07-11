import tkinter as tk
import random

# List of quotes (quote, author)
quotes = [
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("The purpose of our lives is to be happy.", "Dalai Lama"),
    ("Get busy living or get busy dying.", "Stephen King"),
    ("You have within you right now, everything you need to deal with whatever the world can throw at you.", "Brian Tracy"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Act as if what you do makes a difference. It does.", "William James"),
]

# Function to get a random quote
def get_random_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

# Main App Window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")
root.config(bg="white")

# Quote Label
quote_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, justify="center", bg="white")
quote_label.pack(pady=40)

# Author Label
author_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), bg="white")
author_label.pack(pady=10)

# New Quote Button
new_quote_button = tk.Button(root, text="New Quote", command=get_random_quote, font=("Helvetica", 12), bg="#007acc", fg="white", padx=10, pady=5)
new_quote_button.pack(pady=20)

# Load first quote
get_random_quote()

# Run the app
root.mainloop()
