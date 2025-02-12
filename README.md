# Hangman Game

This is a simple Hangman game implemented in Python. The game selects a random word from a predefined list, and the player must guess the word letter by letter before the hangman drawing is completed.

## Features
- Random word selection from a predefined list.
- Tracks both correct and incorrect guesses.
- Provides visual feedback on game progress using ASCII graphics.
- Handles accented letters by normalizing user input.
- Clears the terminal screen for a clean gameplay experience.

## Requirements
- Python 3.x

## Project Structure
- `hangman.py`: Main script that runs the game.
- `graphics.py`: Contains the ASCII representations of the hangman at different stages.
- `words.py`: Contains a list of words used in the game.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Run the script using:
   ```sh
   python main.py
   ```

## How to Play
1. The game will randomly select a word from `words.py`.
2. You need to guess letters one by one.
3. Correct guesses will reveal letters in the word.
4. Incorrect guesses will add to the hangman drawing (defined in `graphics.py`).
5. The game ends when:
   - You correctly guess the entire word.
   - You reach the maximum number of incorrect guesses.

## Example Gameplay
```

            +-------+
            |       
            |       0
            |      -|-
            |      /
            |
         ==============
        
a m e n d _ _ m 



WRONG LETTERS

R T Y Q W 
Give one letter

```
![DEMO](https://github.com/csantos31/hangman-game/blob/main/demo.gif)


## Notes
- The game normalizes input, meaning accented characters are treated as their unaccented versions.

## Author
[Cyntia Santos](https://www.instagram.com/sra.cy_/)

## License
This project is open-source and free to use for educational purposes.

