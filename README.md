**#Stress and Strain Analysis System**

**#Group Members**
Uno Timothy Rayven Kabiling – Task 1: Basic Calculations
Isaiah Collado – Task 2: Control Structures
Jeremiah Daniel Padilla– Task 3: Data Structures
Carlos Gabriel Roman – Task 4: Functions
John Christian Ballesteros – Task 5: OOP

Task 6 Modular Integration was completely collaboratively by all members

**#Project Description**
[Write a short 1-2 sentence summary explaining what the program does.]
The program

**## Program Features**
* [Feature 1: e.g., Calculates stress and strain from user inputs]
* [Feature 2: e.g., Displays analysis results graphically or in console]
* [Feature 3: e.g., Validates material thresholds]

**## Installation/Requirements**
* Python 3.12.6
* Visual Studio Code
* Required libraries: `[e.g., numpy, matplotlib, or "None (uses standard library)"]`

To install requirements (if applicable):
```bash
pip install -r requirements.txt

**## Respository Structure**
2DSA2-Group-4/
├── stress_calculator/
│   ├── __init__.py           # Package marker and metadata
│   ├── properties.py         # MaterialProperties dataclass and validations
│   ├── material.py           # Material base class and Metal, Plastic, Composite subclasses
│   ├── tests.py              # StressStrainTest, TestRecord, and TestCollection models
│   ├── utils.py              # Physics formulas, input validators, and CLI UI helpers
│   ├── database.py           # Material catalogs, JSON/CSV I/O, and test simulator
│   └── main.py               # Package orchestrator and interactive CLI menu
├── main.py                   # Root execution entry point
└── data/                     # Storage folder for JSON session histories and CSV exports
