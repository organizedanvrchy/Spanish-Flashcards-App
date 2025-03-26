from tkinter import *
import pandas as pd

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

# Flashcard - Front 
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Spanish", font=("Lexend", 40, "italic"))
canvas.create_text(400, 263, text=f"{word}", font=("Lexend", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Flashcard - Back


# Button if word was unknown
unknown_button = Button(image=unknown_img, highlightthickness=0, borderwidth=0 )
unknown_button.grid(row=1, column=0)

# Button if word was known
known_button = Button(image=known_img, highlightthickness=0, borderwidth=0)
known_button.grid(row=1, column=1)
window.mainloop()

