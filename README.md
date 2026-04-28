# Pygame Clicker Game

A simple clicker game built with Python and Pygame. The player earns score by clicking and can purchase upgrades to increase how much each click is worth.

This project was built to practice structuring a program using multiple files and classes, and to better understand how game loops, input handling, and state management work together.

---

## Features

- Click to earn score  
- Upgrade system that increases click power  
- Upgrade cost and multiplier scale over time  
- Basic UI displaying score and upgrade information  

---

## Project Structure

```
main.py      → runs the game loop and handles input  
game.py      → manages game state and logic  
button.py    → handles button rendering and click detection  
upgrade.py   → defines upgrade data and behavior  
ui.py        → handles text rendering and UI elements  
```

---

## How to Run

1. Install Pygame:

```
pip install pygame-ce
```

2. Run the game:

```
python main.py
```

---

## Notes

- Click power is calculated dynamically based on purchased upgrades  
- The project is designed to be easily extendable (more upgrades, screens, etc.)  
- Structure separates logic, UI, and control flow to keep things organized  

---

## Future Improvements

- Multiple upgrade types (passive income, bonuses, etc.)  
- Upgrade screen and navigation system  
- Save/load functionality  
- Improved UI (hover effects, feedback, formatting)  
- Sound effects and animations  

---

## Author

Sam Lalonde  

GitHub: https://github.com/SamuelLalonde
