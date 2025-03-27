from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Window initialization
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas initialization
canvas = Canvas(width=800, height=526)

# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
unknown_img = PhotoImage(file="images/wrong.png")
known_img = PhotoImage(file="images/right.png")

# Database
word_df = pd.read_csv("data/spanish_50k_dataset.csv")
word_dict = word_df.to_dict("records")

# Function to generate random word with translation
def randomizer():
    global random_row
    random_row = random.choice(word_dict)
    spanish_word = random_row["Spanish"]
    english_word = random_row["English"]

    canvas.itemconfig(span_word, text=spanish_word)
    # canvas.itemconfig(eng_word, text=english_word)
    # return spanish_word, english_word

# Function to flip the card and show translation
def flip():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(span_word, text=random_row["English"])

# Flashcard - Front 
card = canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Spanish", font=("Lexend", 40, "italic"))
span_word = canvas.create_text(400, 263, text="", font=("Lexend", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button if word was unknown
unknown_button = Button(image=unknown_img, highlightthickness=0, borderwidth=0, command=randomizer)
unknown_button.grid(row=1, column=0)

# Button if word was known
known_button = Button(image=known_img, highlightthickness=0, borderwidth=0, command=randomizer)
known_button.grid(row=1, column=1)

# Button to flip the card
flip_button = Button(text="Flip", command=flip)
flip_button.grid(row=2, column=0, columnspan=2)

# Initial random word
randomizer()

# Loop to keep the window open
window.mainloop()
