# US States Game 🇺🇸
This is a Python-based interactive game that helps you learn U.S. state names by placing them correctly on a blank map. It uses the turtle graphics module along with data from a CSV file. 

# How it works
- A map of the U.S. is displayed.

- You’ll be prompted to guess the names of the 50 states.

- When you guess correctly, the state name appears on the map in the right location.

- If you type "Exit", the game ends and generates a CSV file with the states you missed, so you can study them later.

# Tools and modules used
- Python

- `turtle` – to display the map and state names

- `pandas` – to read and write CSV data

# Files included
- `main.py`: The main game logic.

- `blank_states_img.gif`: The map used for the game.

- `50_states.csv`: Contains state names and coordinates.

- `states_to_learn.csv`: Auto-generated list of missed states.

# How to Run
1. Make sure Python is installed on your system

2. Clone or download this repository.

3. Place `blank_states_img.gif`, `50_states.csv` in the same directory as `main.py`  
   
4. Run the game using one of the following methods:

    - Terminal (macOS/Linux): 'python3 main.py'
    - Windows (or IDEs like VS Code, PyCharm): 'python main.py' or use the Run button

# License
This project is licensed under the MIT License — feel free to use or modify it for learning purposes.
<br>**Have fun! 😊**
