"""
main.py (stress_calculator package entry point)
Coordinates all modules into a unified, interactive engineering application.
Group 4 - Task 6: System Integration
"""

from typing import List, Optional
from .material import Material, Metal, Plastic, Composite
from .properties import MaterialProperties
from .tests import (
    StressStrainTest,
    TestRecord,
    TestCollection,
    evaluate_test_on_material,
    display_test_record
)
from .database import (
    MaterialDatabase,
    save_session_to_json,
    load_session_from_json,
    export_session_to_csv,
    generate_simulated_test,
    DEFAULT_DATA_DIR
)
from .utils import (
    get_positive_float,
    get_yes_no,
    display_header,
    BANNER_WIDTH,
    UNITS
)


class StressCalculatorApp:
    """
    Main application coordinator that ties together the database,
    tests, calculations, file persistence, and CLI interface.
    """

    def __init__(self):
        self.db = MaterialDatabase()
        self.history = TestCollection()

    def select_material_menu(self) -> Material:
        """Presents an interactive menu to choose an existing material or define a custom one."""
        print("\n--- Material Selection ---")
        for i, mat in enumerate(self.db.materials, start=1):
            print(f"{i}. {mat}")
        print(f"{len(self.db.materials) + 1}. Create Custom Material")

        num_options = len(self.db.materials) + 1
        while True:
            choice = input(f"Select an option (1-{num_options}): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(self.db.materials):
                    return self.db.materials[idx - 1]
                elif idx == num_options:
                    # Custom material definition
                    name = input("Enter custom material name: ").strip() or "Custom Material"
                    ys = get_positive_float(f"Enter Yield Strength in {UNITS[3]}: ")
                    mod = get_positive_float(f"Enter Young's Modulus in {UNITS[4]}: ")
                    cat = input("Enter category (e.g. Metal, Polymer, Composite): ").strip() or "Custom"
                    custom_mat = Material(name, MaterialProperties(ys, mod, category=cat))
                    self.db.add_material(custom_mat)
                    return custom_mat
            print(f"Error: Please choose a valid number from 1 to {num_options}.")

    def prompt_physical_inputs(self) -> StressStrainTest:
        """Collects and validates the physical test parameters."""
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

    def run_single_analysis(self) -> None:
        """Performs a single material analysis, displays results, and records into history."""
        material = self.select_material_menu()
        test = self.prompt_physical_inputs()

        record = evaluate_test_on_material(material, test)
        self.history.add_record(record)
        display_test_record(record)

    def run_multi_material_comparison(self) -> None:
        """
        TASK 5 OOP FEATURE:
        Evaluates a single load test across all materials in the database side-by-side.
        """
        display_header("Multi-Material Comparison Analysis")
        test = self.prompt_physical_inputs()

        print("\n" + "=" * BANNER_WIDTH)
        print(f"{'Material':<15} | {'Stress (MPa)':<12} | {'Strain':<10} | {'FOS':<6} | {'Status'}")
        print("-" * BANNER_WIDTH)

        for mat in self.db.materials:
            record = evaluate_test_on_material(mat, test)
            self.history.add_record(record)
            print(f"{record.material:<15} | {record.stress_mpa:<12.2f} | {record.strain:<10.6f} | {record.fos:<6.2f} | {record.safety_status}")
        print("=" * BANNER_WIDTH)

    def run_simulated_test(self) -> None:
        """
        STANDARD LIBRARY RANDOM FEATURE:
        Generates simulated physical test measurements and evaluates them.
        """
        display_header("Simulated Random Test Data Generator")
        material = self.select_material_menu()
        test = generate_simulated_test()

        print("\n[Simulated Physical Measurements Generated via Python random]")
        print(f" - Force:            {test.force:,.2f} N")
        print(f" - Area:             {test.area:.6f} m^2")
        print(f" - Original Length:  {test.original_length:.2f} m")
        print(f" - Change in Length: {test.change_in_length:.6f} m")

        record = evaluate_test_on_material(material, test)
        self.history.add_record(record)
        display_test_record(record)

    def export_to_csv_action(self) -> None:
        """Exports the test history to a CSV spreadsheet."""
        if not self.history.records:
            print("\nError: No test records available to export. Run some tests first!")
            return

        filename = input(f"Enter CSV filename [default: test_export.csv]: ").strip() or "test_export.csv"
        if not filename.endswith(".csv"):
            filename += ".csv"

        path = export_session_to_csv(self.history.records, filename=filename)
        print(f"\n Successfully exported {len(self.history.records)} records to CSV: {path.resolve()}")

    def save_to_json_action(self) -> None:
        """Saves session test history to a JSON file."""
        if not self.history.records:
            print("\nError: No test records to save. Run some tests first!")
            return

        filename = input(f"Enter JSON filename [default: session_history.json]: ").strip() or "session_history.json"
        if not filename.endswith(".json"):
            filename += ".json"

        path = save_session_to_json(self.history.records, filename=filename)
        print(f"\n Successfully saved {len(self.history.records)} records to JSON: {path.resolve()}")

    def load_from_json_action(self) -> None:
        """Loads previously saved test records from a JSON file."""
        filename = input(f"Enter JSON filename to load [default: session_history.json]: ").strip() or "session_history.json"
        if not filename.endswith(".json"):
            filename += ".json"

        try:
            records = load_session_from_json(filename=filename)
            for r in records:
                self.history.add_record(r)
            print(f"\n Successfully loaded {len(records)} test records from JSON.")
        except FileNotFoundError as e:
            print(f"\n Error: {e}")
        except Exception as e:
            print(f"\n Error loading JSON: {e}")


def main() -> None:
    """Main application loop coordinating all modules."""
    app = StressCalculatorApp()

    display_header("Engineering Stress, Strain, and Safety Analysis Calculator")
    print("Welcome to the Group 4 Integrated Material Testing Suite.")

    while True:
        try:
            print("\nSelect Action:")
            print(" 1. Single Material Analysis")
            print(" 2. Multi-Material Comparative Analysis")
            print(" 3. Generate Simulated Random Test Data (random)")
            print(" 4. View Session Summary Statistics")
            print(" 5. Export Test Data to CSV (csv)")
            print(" 6. Save Session History to JSON (json)")
            print(" 7. Load Session History from JSON (json)")
            print(" 8. Exit Application")

            choice = input("\nEnter choice (1-8): ").strip()

            if choice == "1":
                app.run_single_analysis()
            elif choice == "2":
                app.run_multi_material_comparison()
            elif choice == "3":
                app.run_simulated_test()
            elif choice == "4":
                app.history.display_summary_report()
            elif choice == "5":
                app.export_to_csv_action()
            elif choice == "6":
                app.save_to_json_action()
            elif choice == "7":
                app.load_from_json_action()
            elif choice == "8":
                print("\nTerminating session...")
                break
            else:
                print("Error: Invalid selection. Please choose an option from 1 to 8.")
                continue

            if not get_yes_no("\nWould you like to perform another action? (y/n): "):
                print("\nTerminating session...")
                break

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully...")
            break

    # Guaranteed final summary report
    app.history.display_summary_report()
    print("\nThank you for using the calculator. Program terminated successfully.")


if __name__ == "__main__":
    main()

