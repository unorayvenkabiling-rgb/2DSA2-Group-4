# start of roman's part (task 4)

def get_positive_float(prompt, allow_zero=False):
    """
    Handles input validation and exception handling for numerical inputs.
    Prevents negative values, non-numeric values, and zero where invalid.
    """
    while True:
        try:
            val = float(input(prompt))
            if allow_zero and val < 0:
                print(" Error: Input cannot be negative.")
                continue
            elif not allow_zero and val <= 0:
                print(" Error: Input must be strictly greater than zero.")
                continue
            return val
        except ValueError:
            print(" Error: Invalid input. Please enter a numerical value.")


def get_yes_no(prompt):
    """Asks a yes/no question and returns True or False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print(" Error: Please enter 'y' or 'n'.")


def get_predefined_materials():
    """Returns the dictionary of predefined material properties."""
    return {
        "1": ("Steel", 250.0, 200.0),
        "2": ("Aluminum", 95.0, 69.0),
        "3": ("Titanium", 880.0, 114.0)
    }


def select_material():
    """
    Provides material selection menu with predefined engineering properties
    and allows entering custom properties.
    """
    materials = get_predefined_materials()

    print("\n--- Material Selection ---")
    print("1. Steel (Yield Strength: 250 MPa, Young's Modulus: 200 GPa)")
    print("2. Aluminum (Yield Strength: 95 MPa, Young's Modulus: 69 GPa)")
    print("3. Titanium (Yield Strength: 880 MPa, Young's Modulus: 114 GPa)")
    print("4. Custom Material")

    while True:
        choice = input("Select an option (1-4): ").strip()
        if choice in materials:
            return materials[choice]
        elif choice == "4":
            name = input("Enter custom material name: ").strip() or "Custom Material"
            yield_strength = get_positive_float("Enter Yield Strength in MPa: ")
            youngs_modulus = get_positive_float("Enter Young's Modulus in GPa: ")
            return name, yield_strength, youngs_modulus
        else:
            print(" Error: Invalid selection. Please choose options 1, 2, 3, or 4.")


def calculate_stress(force, area):
    """Calculates engineering stress in Pascals (stress = force / area)."""
    return force / area


def calculate_strain(change_in_length, original_length):
    """Calculates engineering strain (change in length / original length)."""
    return change_in_length / original_length


def calculate_youngs_modulus(stress_pa, strain):
    """Calculates Young's Modulus from test data in GPa (E = stress / strain)."""
    if strain == 0:
        return 0.0
    return (stress_pa / strain) / 1e9


def calculate_factor_of_safety(yield_strength_mpa, stress_mpa):
    """Calculates the Factor of Safety (FOS = yield strength / stress)."""
    return yield_strength_mpa / stress_mpa


def determine_safety_status(fos):
    """Classifies safety status based on the Factor of Safety."""
    if fos >= 1.2:
        return "SAFE"
    elif 1.0 <= fos < 1.2:
        return "CAUTION - Loading near material yield point"
    else:
        return "UNSAFE - Material failure / yielding likely!"


def create_test_record(mat_name, force, area, original_length, change_in_length,
                        stress_mpa, strain, rated_modulus_gpa, calculated_modulus_gpa,
                        fos, status):
    """Builds and returns a dictionary for one completed test."""
    return {
        "material": mat_name,
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length,
        "stress": stress_mpa,
        "strain": strain,
        "rated_youngs_modulus": rated_modulus_gpa,
        "calculated_youngs_modulus": calculated_modulus_gpa,
        "fos": fos,
        "safety_result": status
    }


def add_test_record(history_list, unique_materials, record):
    """Adds a test record to the history list and updates unique materials."""
    history_list.append(record)
    unique_materials.add(record["material"])


def compute_session_statistics(history_list):
    """Computes total, safe count, and stress statistics from test history."""
    total = len(history_list)
    if total == 0:
        return None

    safe_tests = sum(1 for record in history_list if record["safety_result"] == "SAFE")
    stress_values = [record["stress"] for record in history_list]

    return {
        "total": total,
        "safe_tests": safe_tests,
        "max_stress": max(stress_values),
        "min_stress": min(stress_values),
        "avg_stress": sum(stress_values) / total
    }


def display_header(title):
    print("\n" + "=" * 50)
    print(f" {title} ")
    print("=" * 50)


def display_material_info(mat_name, yield_strength_mpa, youngs_modulus_gpa, units):
    print("Material Info:")
    print(f" - Material Selected: {mat_name}")
    print(f" - Yield Strength:    {yield_strength_mpa:,.2f} {units[3]}")
    print(f" - Young's Modulus (Rated): {youngs_modulus_gpa:,.2f} {units[4]}")
    print(" - " * 25)


def display_input_parameters(force, area, original_length, change_in_length, units):
    print("Input Parameters:")
    print(f" - Applied Force:         {force:,.2f} {units[0]}")
    print(f" - Cross Sectional Area:  {area:.6f} {units[1]}")
    print(f" - Original Length:       {original_length:.4f} {units[2]}")
    print(f" - Change in Length:      {change_in_length:.6f} {units[2]}")
    print(" - " * 25)


def display_results(stress_mpa, stress_pa, strain, calculated_modulus_gpa, units):
    print("Calculated Outputs:")
    print(f" - Engineering Stress:    {stress_mpa:,.2f} {units[3]} ({stress_pa:,.2f} Pa)")
    print(f" - Engineering Strain:    {strain:.6f}")
    print(f" - Young's Modulus (Calculated): {calculated_modulus_gpa:,.2f} {units[4]}")
    print(" - " * 25)


def display_safety_analysis(fos, status):
    print("Safety Analysis:")
    print(f" - Factor of Safety:      {fos:.2f}")
    print(f" - Safety Status:         {status}")
    print("=" * 50)


def display_session_summary(stats, unique_materials):
    display_header("SESSION SUMMARY REPORT")

    if stats is None:
        print("No calculations were performed during this session.")
        return

    print(f"Total Calculations Performed: {stats['total']}")
    print(f"Unique Materials Tested: {', '.join(unique_materials)}")
    print(f"Total Safe Tests: {stats['safe_tests']} out of {stats['total']}")
    print(" - " * 25)
    print("STRESS STATISTICS:")
    print(f" Highest Stress Recorded: {stats['max_stress']:,.2f} MPa")
    print(f" Lowest Stress Recorded:  {stats['min_stress']:,.2f} MPa")
    print(f" Average Stress Across Tests: {stats['avg_stress']:,.2f} MPa")


def run_single_test(history_list, unique_materials, units):
    """Runs one full test cycle: input, calculation, display, and storage."""
    display_header("Engineering Stress, Strain, and Safety Analysis Calculator (Task 4)")

    mat_name, yield_strength_mpa, rated_modulus_gpa = select_material()

    print("\nPlease enter the requested values below.\n")
    force = get_positive_float(f"Enter applied force (F) in Newton [{units[0]}]: ")
    area = get_positive_float(f"Enter cross sectional area (A) in square meters [{units[1]}]: ")
    original_length = get_positive_float(f"Enter original length in meters [{units[2]}]: ")
    change_in_length = get_positive_float(
        f"Enter change in length in meters [{units[2]}]: ", allow_zero=True
    )

    stress_pa = calculate_stress(force, area)
    stress_mpa = stress_pa / 1e6
    strain = calculate_strain(change_in_length, original_length)
    calculated_modulus_gpa = calculate_youngs_modulus(stress_pa, strain)
    fos = calculate_factor_of_safety(yield_strength_mpa, stress_mpa)
    status = determine_safety_status(fos)

    record = create_test_record(
        mat_name, force, area, original_length, change_in_length,
        stress_mpa, strain, rated_modulus_gpa, calculated_modulus_gpa, fos, status
    )
    add_test_record(history_list, unique_materials, record)

    display_header("Calculation Results")
    display_material_info(mat_name, yield_strength_mpa, rated_modulus_gpa, units)
    display_input_parameters(force, area, original_length, change_in_length, units)
    display_results(stress_mpa, stress_pa, strain, calculated_modulus_gpa, units)
    display_safety_analysis(fos, status)


def main():
    """Main loop for repeated calculations, ending with a session summary."""
    history_list = []
    unique_materials = set()
    units = ["N", "m^2", "m", "MPa", "GPa"]

    while True:
        try:
            run_single_test(history_list, unique_materials, units)
        except KeyboardInterrupt:
            print("\n\nProgram force-closed by user. Exiting gracefully...")
            break

        if not get_yes_no("\nWould you like to perform another calculation? (y/n): "):
            print("Thank you for using the calculator. Program terminated gracefully.")
            break

    display_session_summary(compute_session_statistics(history_list), unique_materials)


if __name__ == "__main__":
    main()

# end of roman's part (task 4)