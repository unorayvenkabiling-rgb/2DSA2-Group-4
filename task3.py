# start of jeremiah's part (task 3)
def run_calculator_task3(history_list, unique_materials, units):
    #Executes the calculator and stores the data in the history list and unique materials set
    print("\n" + " = " * 25)
    print(" Engineering Stress, Strain, and Safety Analysis Calculator ")
    print(" = " * 25)

    # 1. Material Selection & Set update
    mat_name, yield_strength_mpa, youngs_modulus_gpa = select_material()
    unique_materials.add(mat_name)

    # 2. Input Validation (Replaces simple float(input()) calls)
    print("\nPlease enter the requested values below.\n")
    applied_force = get_positive_float(f"Enter applied force (F) in Newton [{units[0]}]: ")
    cross_sectional_area = get_positive_float(f"Enter cross sectional area (A) in square meters [{units[1]}]: ")
    original_length = get_positive_float(f"Enter original length in meters [{units[2]}]: ")
    change_in_length = get_positive_float(f"Enter change in length in meters [{units[2]}]: ", allow_zero=True)

    # 3. Calculations
    stress_pa = applied_force / cross_sectional_area
    stress_mpa = stress_pa / 1e6
    strain = change_in_length / original_length

    # 4. Safety Analysis & Factor of Safety
    fos = yield_strength_mpa / stress_mpa
    if fos >= 1.2:
        status = "SAFE"
    elif 1.0 <= fos < 1.2:
        status = "CAUTION - Loading near material yield point"
    else:
        status = "UNSAFE - Material failure / yielding likely!"

    # 5. Dictionary to store the calculation data for history
    test_data = {
        "material": mat_name,
        "force": applied_force,
        "area": cross_sectional_area,
        "original_length": original_length,
        "change_in_length": change_in_length,
        "stress": stress_mpa,
        "strain": strain,
        "fos": fos,
        "Young's Modulus": youngs_modulus_gpa,
        "safety result": status
    }

    #6. List to store the test data for history
    history_list.append(test_data)

    #Output Display
    print("\n" + "=" * 50)
    print(" Calculation results ")
    print("=" * 50)
    print("Material Info:")
    print(f" - Material Selected: {test_data['material']}")
    print(f" - Yield Strength:    {yield_strength_mpa:,.2f} {units[3]}")
    print(f" - Young's Modulus:   {youngs_modulus_gpa:,.2f} {units[4]}")
    print(" - " * 25)
    print("Input Parameters:")
    print(f" - Applied Force:         {test_data['force']:,.2f} {units[0]}")
    print(f" - Cross Sectional Area:  {test_data['area']:.6f} {units[1]}")
    print(f" - Original Length:       {test_data['original_length']:.4f} {units[2]}")
    print(f" - Change in Length:      {test_data['change_in_length']:.6f} {units[2]}")
    print(" - " * 25)
    print("Calculated Outputs:")
    print(f" - Engineering Stress:    {test_data['stress']:,.2f} {units[3]}")
    print(f" - Engineering Strain:    {test_data['strain']:.6f}")
    print(" - " * 25)
    print("Safety Analysis:")
    print(f" - Factor of Safety:      {test_data['fos']:.2f}")
    print(f" - Safety Status:         {test_data['safety result']}")
    print(" = " * 50)

def session_summary(history_list, unique_materials):
    #Displays the session summary with  basic statistical information
    print("\n" + "=" * 50)
    print(" SESSION SUMMARY REPORT ")
    print("=" * 50)

    total_calculations = len(history_list)
    if total_calculations == 0:
        print("No calculations were performed during this session.")
        return

    safe_tests = sum(1 for data in history_list if data['safety result'] == "SAFE")
    stress_values = [data['stress'] for data in history_list]
    max_stress = max(stress_values)
    min_stress = min(stress_values)
    avg_stress = sum(stress_values) / total_calculations

    print(f"Total Calculations Performed: {total_calculations}")
    print(f"Unique Materials Tested: {', '.join(unique_materials)}")
    print(f"Total Safe Tests: {safe_tests} out of {total_calculations}")
    print(" - " * 25)
    print("STRESS STATISTICS:")
    print(f" Highest Stress Recorded: {max_stress:,.2f} MPa")
    print(f" Lowest Stress Recorded: {min_stress:,.2f} MPa")
    print(f" Average Stress Across Tests: {avg_stress:,.2f} MPa")

def main_task3():
    """Main loop for repeated calculations."""
    #TUPLE: Values that should remain constant
    #constant_values = ("N", "m^2", "m", "MPa", "GPa")

    #LIST: Stores the history of calculations performed in the session
    #session_history = []

    #SET: Stores unique materials tested during the session
    #session_materials = set()

    history_list = []
    unique_materials = set()
    units = ["N", "m^2", "m", "MPa", "GPa"]  # Units for force, area, length, stress, modulus

    while True:
        try:
            run_calculator_task3(history_list, unique_materials, units)
        except KeyboardInterrupt:
            print("\n\nProgram force-closed by user. Exiting gracefully...")
            break

        # Repeated Calculations check
        repeat = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Thank you for using the calculator. Program terminated gracefully.")
            break

if __name__ == "__main__":
    main_task3()

#end of jeremiah's part(task 3)