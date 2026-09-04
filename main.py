"""
2DSA2 - Group 4: Python Fundamentals Coding Challenge
Final Integrated Project (Task 6: System Integration)

Authors & Task Contributions:
- Task 1: Basic Calculations & Physics Engine (Kabiling)
- Task 2: Control Structures, Validation & Safety Logic (Collado)
- Task 3: Data Structures (Tuples, Lists, Sets, Dictionaries) & History (Padilla)
- Task 4: Modular Functions & Standardized Formatting (Roman)
- Task 5: Object-Oriented Design (Classes, Inheritance, Dataclass) (Ballesteros)
- Task 6: Complete Architectural Integration (Group 4)
"""

from dataclasses import dataclass
from typing import List, Dict, Set, Optional, Tuple

# constants and data structures
# Tuple (immutable)
UNITS: Tuple[str, ...] = ("N", "m^2", "m", "MPa", "GPa")

# input validation and control structures
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

# core formulas and modular functions
def calculate_stress_pa(force: float, area: float) -> float:
    """Engineering Stress: sigma = Force / Area (in Pascals [Pa])."""
    return force / area


def calculate_stress_mpa(stress_pa: float) -> float:
    """Converts Stress from Pascals to Megapascals [MPa]."""
    return stress_pa / 1e6


def calculate_strain(change_in_length: float, original_length: float) -> float:
    """Engineering Strain: epsilon = delta_L / L_0 (dimensionless)."""
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


# object-oriented data models
@dataclass
class StressStrainTest:
    """Encapsulates the physical measurements of a tension/compression test."""
    force: float            # Applied Force in Newtons (N)
    area: float             # Cross-Sectional Area in square meters (m^2)
    original_length: float  # Original Length in meters (m)
    change_in_length: float # Change in Length in meters (m)


class Material:
    """Base class modeling engineering materials, physical properties, and analysis."""

    def __init__(self, name: str, yield_strength: float, elastic_modulus: float):
        self.name: str = name
        self._yield_strength: float = yield_strength      # in MPa
        self._elastic_modulus: float = elastic_modulus    # in GPa

    @property
    def yield_strength(self) -> float:
        """Rated Yield Strength in MPa."""
        return self._yield_strength

    @property
    def elastic_modulus(self) -> float:
        """Rated Young's Modulus in GPa."""
        return self._elastic_modulus

    def evaluate_test(self, test: StressStrainTest) -> Dict[str, any]:
        """
        DICTIONARY:
        Evaluates the material under the given test parameters and returns a complete record.
        """
        stress_pa = calculate_stress_pa(test.force, test.area)
        stress_mpa = calculate_stress_mpa(stress_pa)
        strain = calculate_strain(test.change_in_length, test.original_length)
        calc_modulus = calculate_youngs_modulus_gpa(stress_pa, strain)
        fos = calculate_factor_of_safety(self.yield_strength, stress_mpa)
        status = determine_safety_status(fos)

        return {
            "material": self.name,
            "force": test.force,
            "area": test.area,
            "original_length": test.original_length,
            "change_in_length": test.change_in_length,
            "stress_pa": stress_pa,
            "stress_mpa": stress_mpa,
            "strain": strain,
            "rated_modulus_gpa": self.elastic_modulus,
            "calculated_modulus_gpa": calc_modulus,
            "yield_strength_mpa": self.yield_strength,
            "fos": fos,
            "safety_status": status
        }

    def __str__(self) -> str:
        return f"{self.name} (Yield Strength: {self._yield_strength:.1f} MPa, Young's Modulus: {self._elastic_modulus:.1f} GPa)"


# Polymorphic subclasses representing material categories
class Metal(Material):
    """Subclass representing metallic alloys."""
    def __init__(self, name: str = "Structural Steel", yield_strength: float = 250.0, elastic_modulus: float = 200.0):
        super().__init__(name, yield_strength, elastic_modulus)


class Plastic(Material):
    """Subclass representing polymers and plastics."""
    def __init__(self, name: str = "ABS Polymer", yield_strength: float = 45.0, elastic_modulus: float = 2.5):
        super().__init__(name, yield_strength, elastic_modulus)


class Composite(Material):
    """Subclass representing composite materials."""
    def __init__(self, name: str = "Carbon Fiber Composite", yield_strength: float = 500.0, elastic_modulus: float = 120.0):
        super().__init__(name, yield_strength, elastic_modulus)

# formatting and presentation
BANNER_WIDTH = 61


def display_header(title: str) -> None:
    width = max(BANNER_WIDTH, len(title) + 2)
    print("\n" + "=" * width)
    print(f" {title}")
    print("=" * width)


def display_test_record(record: Dict[str, any], units: Tuple[str, ...] = UNITS) -> None:
    """Formats and prints a single completed test record with precision."""
    display_header("Calculation Results")

    print("Material Info:")
    print(f" - Material Selected:     {record['material']}")
    print(f" - Yield Strength:        {record['yield_strength_mpa']:,.2f} {units[3]}")
    print(f" - Rated Young's Modulus: {record['rated_modulus_gpa']:,.2f} {units[4]}")
    print(" - " * 20)

    print("Input Parameters:")
    print(f" - Applied Force:         {record['force']:,.2f} {units[0]}")
    print(f" - Cross Sectional Area:  {record['area']:.6f} {units[1]}")
    print(f" - Original Length:       {record['original_length']:.4f} {units[2]}")
    print(f" - Change in Length:      {record['change_in_length']:.6f} {units[2]}")
    print(" - " * 20)

    print("Calculated Outputs:")
    print(f" - Engineering Stress:    {record['stress_mpa']:,.2f} {units[3]} ({record['stress_pa']:,.2f} Pa)")
    print(f" - Engineering Strain:    {record['strain']:.6f}")
    print(f" - Calc. Young's Modulus: {record['calculated_modulus_gpa']:,.2f} {units[4]}")
    print(" - " * 20)

    print("Safety Analysis:")
    print(f" - Factor of Safety:      {record['fos']:.2f}")
    print(f" - Safety Status:         {record['safety_status']}")
    print("=" * BANNER_WIDTH)


# system composition and session management
class StressAnalysisSystem:
    """
    Composition Manager that coordinates materials, tests,
    session history logging (List), unique materials (Set), and statistical summaries.
    """

    def __init__(self):
        # List(stores all individual test records)
        self.history_list: List[Dict[str, any]] = []
        # Set(tracks unique material names tested_
        self.unique_materials: Set[str] = set()
        # Catalog of pre-configured materials
        self.materials_catalog: List[Material] = [
            Metal("Steel", yield_strength=250.0, elastic_modulus=200.0),
            Metal("Aluminum", yield_strength=95.0, elastic_modulus=69.0),
            Metal("Titanium", yield_strength=880.0, elastic_modulus=114.0),
            Plastic("ABS Polymer", yield_strength=45.0, elastic_modulus=2.5),
            Composite("Carbon Fiber", yield_strength=500.0, elastic_modulus=120.0),
        ]

    def add_material_to_catalog(self, material: Material) -> None:
        """Adds a custom material to the system catalog."""
        self.materials_catalog.append(material)

    def log_record(self, record: Dict[str, any]) -> None:
        """Stores test record into history list and updates unique materials set."""
        self.history_list.append(record)
        self.unique_materials.add(record["material"])

    def select_material_dialog(self) -> Material:
        """Presents an interactive menu to choose an existing or custom material."""
        print("\n--- Material Selection ---")
        for i, mat in enumerate(self.materials_catalog, start=1):
            print(f"{i}. {mat}")
        print(f"{len(self.materials_catalog) + 1}. Create Custom Material")

        num_options = len(self.materials_catalog) + 1
        while True:
            choice = input(f"Select an option (1-{num_options}): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(self.materials_catalog):
                    return self.materials_catalog[idx - 1]
                elif idx == num_options:
                    # Custom material creation
                    name = input("Enter custom material name: ").strip() or "Custom Material"
                    ys = get_positive_float(f"Enter Yield Strength in {UNITS[3]}: ")
                    mod = get_positive_float(f"Enter Young's Modulus in {UNITS[4]}: ")
                    custom_mat = Material(name, ys, mod)
                    self.add_material_to_catalog(custom_mat)
                    return custom_mat
            print(f"Error: Please choose a valid number from 1 to {num_options}.")

    def prompt_test_parameters(self) -> StressStrainTest:
        """Collects and validates input parameters for a physical test run."""
        print("\nPlease enter the test parameters below:\n")
        force = get_positive_float(f"Enter applied force (F) in Newton [{UNITS[0]}]: ")
        area = get_positive_float(f"Enter cross sectional area (A) in square meters [{UNITS[1]}]: ")
        orig_len = get_positive_float(f"Enter original length in meters [{UNITS[2]}]: ")
        chg_len = get_positive_float(f"Enter change in length in meters [{UNITS[2]}]: ", allow_zero=True)

        return StressStrainTest(
            force=force,
            area=area,
            original_length=orig_len,
            change_in_length=chg_len
        )

    def run_single_test(self) -> None:
        """Conducts a single test cycle on a chosen material and logs results."""
        material = self.select_material_dialog()
        test = self.prompt_test_parameters()

        record = material.evaluate_test(test)
        self.log_record(record)
        display_test_record(record)

    def run_multi_material_comparison(self) -> None:
        """
        TASK 5 OOP FEATURE:
        Evaluates a single set of test parameters across ALL catalog materials simultaneously.
        """
        display_header("Multi-Material Comparison Analysis")
        test = self.prompt_test_parameters()

        print("\n" + "=" * BANNER_WIDTH)
        print(f"{'Material':<15} | {'Stress (MPa)':<12} | {'Strain':<10} | {'FOS':<6} | {'Status'}")
        print("-" * BANNER_WIDTH)

        for mat in self.materials_catalog:
            record = mat.evaluate_test(test)
            self.log_record(record)
            print(f"{record['material']:<15} | {record['stress_mpa']:<12.2f} | {record['strain']:<10.6f} | {record['fos']:<6.2f} | {record['safety_status']}")
        print("=" * BANNER_WIDTH)

    def display_session_summary(self) -> None:
        """
        SESSION SUMMARY REPORT (Task 3 & Task 4):
        Aggregates and prints comprehensive session statistics.
        """
        display_header("SESSION SUMMARY REPORT")

        total = len(self.history_list)
        if total == 0:
            print("No calculations were performed during this session.")
            return

        safe_tests = sum(1 for rec in self.history_list if rec["safety_status"] == "SAFE")
        stress_vals = [rec["stress_mpa"] for rec in self.history_list]
        max_stress = max(stress_vals)
        min_stress = min(stress_vals)
        avg_stress = sum(stress_vals) / total

        print(f"Total Calculations Performed: {total}")
        print(f"Unique Materials Tested:      {', '.join(sorted(self.unique_materials))}")
        print(f"Total Safe Tests:             {safe_tests} out of {total}")
        print(" - " * 20)
        print("STRESS STATISTICS:")
        print(f" - Highest Stress Recorded:   {max_stress:,.2f} {UNITS[3]}")
        print(f" - Lowest Stress Recorded:    {min_stress:,.2f} {UNITS[3]}")
        print(f" - Average Stress Across:     {avg_stress:,.2f} {UNITS[3]}")
        print("=" * BANNER_WIDTH)


# main application entry point
def main() -> None:
    """Main interactive execution loop."""
    system = StressAnalysisSystem()

    display_header("Engineering Stress, Strain, and Safety Analysis Calculator")
    print("Welcome to the Group 4 Integrated Material Testing Suite.")

    while True:
        try:
            print("\nSelect Mode:")
            print(" 1. Single Material Analysis")
            print(" 2. Multi-Material Comparative Analysis")
            print(" 3. View Current Session Statistics")
            print(" 4. Exit Application")

            choice = input("\nEnter choice (1-4): ").strip()

            if choice == "1":
                system.run_single_test()
            elif choice == "2":
                system.run_multi_material_comparison()
            elif choice == "3":
                system.display_session_summary()
            elif choice == "4":
                print("\nTerminating session...")
                break
            else:
                print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")
                continue

            # Prompt to continue or exit
            if not get_yes_no("\nWould you like to perform another action? (y/n): "):
                print("\nTerminating session...")
                break

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully...")
            break

    # Guaranteed Session Summary Report on exit
    system.display_session_summary()
    print("\nThank you for using the calculator. Program terminated successfully.")


if __name__ == "__main__":
    main()