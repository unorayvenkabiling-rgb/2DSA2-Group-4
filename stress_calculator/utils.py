"""
utils.py
Contains reusable calculation, conversion utilities, input validation, and formatting.
Part of Task 6: System Integration
"""

from typing import Tuple


# ==============================================================================
# CONSTANTS
# ==============================================================================
# TUPLE (Task 3): Immutable engineering units
# Index 0: Force [N], 1: Area [m^2], 2: Length [m], 3: Stress [MPa], 4: Modulus [GPa]
UNITS: Tuple[str, ...] = ("N", "m^2", "m", "MPa", "GPa")

# Width for terminal header banners and dividers
BANNER_WIDTH: int = 61


# ==============================================================================
# PHYSICAL CALCULATIONS (TASK 1 & TASK 4)
# ==============================================================================
def calculate_stress_pa(force: float, area: float) -> float:
    """Engineering Stress: sigma = Force / Area (in Pascals [Pa])."""
    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly positive.")
    return force / area


def calculate_stress_mpa(stress_pa: float) -> float:
    """Converts Stress from Pascals to Megapascals [MPa]."""
    return stress_pa / 1e6


def calculate_strain(change_in_length: float, original_length: float) -> float:
    """Engineering Strain: epsilon = delta_L / L_0 (dimensionless)."""
    if original_length <= 0:
        raise ValueError("Original length must be strictly positive.")
    return change_in_length / original_length


def calculate_youngs_modulus_gpa(stress_pa: float, strain: float) -> float:
    """Calculated Young's Modulus: E = sigma / epsilon (in Gigapascals [GPa])."""
    if strain == 0:
        return 0.0
    return (stress_pa / strain) / 1e9


def calculate_factor_of_safety(yield_strength_mpa: float, stress_mpa: float) -> float:
    """Factor of Safety: FOS = Yield Strength / Working Stress."""
    if stress_mpa == 0:
        return 0.0
    return yield_strength_mpa / stress_mpa


def determine_safety_status(fos: float) -> str:
    """Categorizes the structural safety status based on Factor of Safety."""
    if fos >= 1.2:
        return "SAFE"
    elif 1.0 <= fos < 1.2:
        return "CAUTION - Loading near material yield point"
    else:
        return "UNSAFE - Material failure / yielding likely!"


# ==============================================================================
# INPUT VALIDATION & UI PROMPTS (TASK 2 & TASK 4)
# ==============================================================================
def get_positive_float(prompt: str, allow_zero: bool = False) -> float:
    """
    Validates numeric user inputs with robust exception handling.
    Rejects non-numeric entries, negative numbers, and zero when disallowed.
    """
    while True:
        try:
            val = float(input(prompt))
            if allow_zero and val < 0:
                print(" Error: The input cannot be negative.")
                continue
            elif not allow_zero and val <= 0:
                print(" Error: The input must be strictly greater than zero.")
                continue
            return val
        except ValueError:
            print(" Error: Invalid input. Please enter a numerical value.")


def get_yes_no(prompt: str) -> bool:
    """Prompts for a (y/n) confirmation with strict input validation."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        print(" Error: Please respond with 'y' or 'n'.")


def display_header(title: str, width: int = BANNER_WIDTH) -> None:
    """Displays a standardized terminal header banner with symmetrical borders."""
    w = max(width, len(title) + 2)
    print("\n" + "=" * w)
    print(f" {title}")
    print("=" * w)

