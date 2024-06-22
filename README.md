# Dice Roller

This Python script is a simple interactive dice roller that simulates rolling a six-sided dice and displays the result using ASCII art. 

## Features:

-  Generates random dice rolls from 1 to 6.
-  Displays each roll as an ASCII representation of the dice face.
-  Prompts the user to roll again after each roll. 

## How to Use:

1. **Save the code:** Save the code provided in this repository as a `.py` file (e.g., `dice_roller.py`).
2. **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the script. Run the script using the command `python dice_roller.py`.
3. **Roll the dice:** Follow the on-screen prompts to roll the dice and see the results.

## Code Explanation:

The code consists of two main parts:

- **Dice representation:** A dictionary `dice` stores ASCII art representations for each dice face (1 to 6).
- **Function `rolling()`:** 
    - Takes user input to start rolling.
    - Generates a random dice roll using `random.randint(1, 6)`.
    - Prints the ASCII representation of the rolled face using `print_dice_face()`.
    - Loops until the user chooses to stop.

Feel free to modify the code to customize the dice faces or add more features! 
