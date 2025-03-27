from tkinter import *
import pandas as pd
import random

# Global Variables
BACKGROUND_COLOR = "#B1DDC6"
word_dict        = {}
random_row       = {}
flip_timer       = None

# Window Initialization
window = Tk()
window.title("Flashcards")
window.config(padx=50, 
              pady=50, 
              bg=BACKGROUND_COLOR)

# Canvas Initialization
canvas = Canvas(width=800, 
                height=526)

# Images
card_front_img  = PhotoImage(file="images/card_front.png")
card_back_img   = PhotoImage(file="images/card_back.png")
unknown_img     = PhotoImage(file="images/wrong.png")
known_img       = PhotoImage(file="images/right.png")

# Database
try:
    word_df     = pd.read_csv("data/spanish_words_to_learn.csv")
except FileNotFoundError:
    ori_word_df = pd.read_csv("data/spanish_50k_dataset.csv")
    word_dict   = ori_word_df.to_dict(orient="records")
else:
    word_dict   = word_df.to_dict(orient="records")

# Function to Generate Random Word with Translation
def randomizer():
    global random_row, flip_timer

    # Reset Flip Timer
    if flip_timer:
        window.after_cancel(flip_timer)

    random_row      = random.choice(word_dict)
    canvas.itemconfig(card_title,
                      text="Spanish",
                      fill="black")
    canvas.itemconfig(card_word, 
                      text=random_row["Spanish"],
                      fill="black")
    canvas.itemconfig(card,
                      image=card_front_img)
    
    # Flip Card After 3s
    flip_timer = window.after(3000, flip)

# Function to Flip the Card and Show Translation
def flip():
    canvas.itemconfig(card, 
                      image=card_back_img)
    canvas.itemconfig(card_title, 
                      text="English", 
                      fill="white")
    canvas.itemconfig(card_word, 
                      text=random_row["English"], 
                      fill="white")
    
# Function to Remove Known Word and Generate New Word
def known():
    word_dict.remove(random_row)
    data = pd.DataFrame(word_dict)
    data.to_csv("data/spanish_words_to_learn.csv",
                index=False)

    randomizer()
    
# Flashcard - Front 
card    = canvas.create_image(400, 263, 
                                  image=card_front_img)
card_title  = canvas.create_text(400, 150, 
                                 text="Spanish", 
                                 font=("Lexend", 40, "italic"))
card_word   = canvas.create_text(400, 263, 
                                 text="", 
                                 font=("Lexend", 55, "bold"))

canvas.config(bg=BACKGROUND_COLOR, 
              highlightthickness=0)

canvas.grid(row=0, 
            column=0, 
            columnspan=2)

# Button If Word Was Unknown
unknown_button  = Button(image=unknown_img, 
                         highlightthickness=0, 
                         borderwidth=0, 
                         command=randomizer)

unknown_button.grid(row=1, column=0)

# Button If Word Was Known
known_button    = Button(image=known_img, 
                         highlightthickness=0, 
                         borderwidth=0, 
                         command=known)

known_button.grid(row=1, column=1)

# Flip Timer
# flip_timer = window.after(3000, flip)

# Initial Random Word
randomizer()

# Loop to Keep Window Open
window.mainloop()
