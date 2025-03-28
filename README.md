# Flashcard App - Spanish to English

This is a simple flashcard application built using Python and Tkinter to help users learn Spanish words with their English translations. The app randomly selects a Spanish word from a .csv of 50,000 of the most frequently used Spanish words, displays it on a card, and then flips the card after a few seconds to reveal the English translation. Users can mark words as known or unknown, and the app keeps track of the words that need further review.

## Features

### Python Concepts Used
- GUI programming with Tkinter
- File handling with Pandas for CSV operations
- Random module for word selection
- Event-driven programming with Tkinter buttons
- Timers using `after` function for delayed execution

### Program Features
- Displays a Spanish word on a flashcard
- Flips the card after 3 seconds to show the English translation
- Users can mark words as known or unknown
- Known words are removed from the list and saved for future sessions

### Code Structure
- **Window Initialization**: Creates the main application window
- **Canvas Setup**: Manages the display of flashcards
- **Image Loading**: Handles images for front and back of flashcards, and buttons
- **Data Handling**: Reads words from a CSV file and tracks known words
- **Functions**:
  - `randomizer()`: Selects a random word and displays it
  - `flip()`: Flips the card to show translation
  - `known()`: Removes the known word from the dataset

## Requirements

- Python 3.x
- Tkinter (built-in with Python)
- Pandas

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/flashcard-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flashcard-app
   ```
3. Install dependencies:
   ```bash
   pip install pandas
   ```

## Running the Program

Run the script using:
```bash
python flashcard.py
```

## Possible Future Improvements
- Add speech synthesis to pronounce words
- Improve UI with animations and themes
- Implement user progress tracking
- Expand the dataset with more words
- Adjust the dataset to filter out names of people and places that do no require translations, and nonsensical words without translations. 

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request with improvements.

## Acknowledgments
Special thanks to the [Udemy 100 Days of Code - Angela Yu](https://www.udemy.com/course/100-days-of-code-the-complete-python-pro-bootcamp-for-2023/) course for inspiration and guidance.
