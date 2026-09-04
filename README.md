**Stress and Strain Analysis System**

**Group Members**
Uno Timothy Rayven Kabiling – Task 1: Basic Calculations

Isaiah Collado – Task 2: Control Structures

Jeremiah Daniel Padilla– Task 3: Data Structures

Carlos Gabriel Roman – Task 4: Functions

John Christian Ballesteros – Task 5: OOP

Task 6 Modular Integration was completely collaboratively by all members

**Project Description**
This program is an engineering calculator that computes for the stress, strain, Young's modulus, and safety factor based on the applied force, area, and deformation.

**Program Features**
* Single Material Analysis: Calculate Engineering Stress(Pa/Mpa), Engineering Strain, Young's Modulus, and Factor of Safety
* Multi Material Comparison: Metals, Plastics and composites with side by side comparison
* Stimulated Test Data: Physical tests (Force, Area, Length and Deformation)
* Data Persistence: Logs timestamps
* Session History: Tracks test run

**Installation / Requirements**
* Python 3.12.6
* Visual Studio Code
* Libraries used: dataclasses, typing, datetime, json, csv, pathlib, random


To install requirements (if applicable):
*Python 3.8 or higher
* External Packages: None


2DSA2-Group-4

* stress_calculator

*  __init__.py           # Package marker and metadata

* properties.py         # MaterialProperties dataclass and validations

* material.py           # Material base class and Metal, Plastic, Composite subclasses

* tests.py              # StressStrainTest, TestRecord, and TestCollection models

* utils.py              # Physics formulas, input validators, and CLI UI helpers

* database.py           # Material catalogs, JSON/CSV I/O, and test simulator

* main.py               # Package orchestrator and interactive CLI menu

* main.py                # Root execution entry point

* data/                  # Storage folder for JSON session histories and CSV exports
