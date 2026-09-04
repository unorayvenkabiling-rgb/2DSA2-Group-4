#start of uno's part (task 1)
print(" = " * 50)
print(" Engineering Stress and Strain Calculator")
print(" = " * 50)
print(" PLease enter the requested values below.\n ")

applied_force = float(input("Enter applied force (F) in Newton [N]:"))
cross_sectional_area = float(input(" Enter cross sectional area (A) in square meters [m^2]: "))
original_length = float(input(" Enter original length in meters [m]:"))
change_in_length = float(input(" Enter change in length in meters [m]:"))

stress = applied_force / cross_sectional_area
strain = change_in_length / original_length

print("\n" + "=" * 50)
print(" Calculation results ")
print("=" * 50)

print("Input Parameters:")
print(f" - Applied Force {applied_force:,.2f}N")
print(f" - Cross Sectional Area: { cross_sectional_area:.6f} m^2")
print(f" - Original Length: {original_length:4f}m")
print(f" - Change in Length: {change_in_length:6f}m")
print(" - " * 50)


print(" Calculated Outputs: ")
print(f" - Engineering Stress: {stress:,.2f}Pa")
print(f" - Engineering Strain: {strain:.6f}")
print( " = " * 50)
#end of uno's part

#task 2 start of isaiah's part

def get_positive_float(prompt, allow_zero=False): #input validation
  while True:
    try:
      val = float(input(prompt))
      if allow_zero and val < 0:
        print("Error: The input cannot be negative.")
        continue
      elif not allow_zero and val <= 0:
        print("Error: The input must be strictly greater than zero.")
        continue
      return val
    except ValueError:
      print("Error: Invalid input. Please enter a numerical value.")

def select_material(): #material selection
  materials = {
    "1": ("Steel", 250.0, 200.0),
    "2": ("Aluminum", 95.0, 69.0),
    "3": ("Titanium", 880.0, 114.0),
  }

  print("\n---Material Selection---")
  print("1. Steel (Yield Strength: 250 MPa, Young's Modulus: 200 GPa)")
  print("2. Aluminum (Yield Strength: 95 MPa, Young's Modulus: 69 GPa)")
  print("3. Titanium (Yield Strength: 880 MPa, Young's Modulus: 114 GPa)")
  print("4. Custom Material")

  while True:
        choice = input("Select an option (1-4): ").strip()
        if choice in materials:
          name, yield_strength, youngs_modulus = materials[choice]
          return name, yield_strength, youngs_modulus
        elif choice == "4":
            name = input("Enter custom material name: ").strip() or "Custom Material"
            yield_strength = get_positive_float("Enter Yield Strength in MPa: ")
            youngs_modulus = get_positive_float("Enter Young's Modulus in GPa: ")
            return name, yield_strength, youngs_modulus
        else:
            print("Error: Invalid selection. Please Choose from numbers 1, 2, 3, and 4.")

def run_calculator():
    print(" = " * 20)
    print("Stress, Stress, and Safety Analysis Calculator")
    print(" = " * 20)

    #material selection stuff
    mat_name, yield_strength_mpa, youngs_module_gpa = select_material()

    #input validation time
    print("\nPlease enter the requested values below.\n")
    applied_force = get_positive_float("Enter applied force (F) in Newton (N): ")
    cross_sectional_area = get_positive_float("Enter cross sectional area (A) in square meter [m^2]: ")
    original_length = get_positive_float("Enter original length in meters [m]: ")
    change_in_length = get_positive_float("Enter change in length in meters [m]: ", allow_zero=True)

    #calculations
    stress_pa = applied_force / cross_sectional_area
    stress_mpa = stress_pa / 1e6
    strain = change_in_length / original_length

    #analysis and factor of safety
    fos = yield_strength_mpa / stress_mpa

    if fos >= 1.2:
        status = "SAFE"
    elif 1.0 <= fos < 1.2:
        status = "CAUTION - Loading near material yield point"
    else:
        status = "UNSAFE - Material failure / yielding likely!"

    #output display
    print("\n" + "=" * 50)
    print("Calculation results")
    print("=" * 50)

    print("Material Info:")
    print(f" - Material Selected: {mat_name}")
    print(f" - Yield Strength: {yield_strength_mpa:,.2f} MPa")
    print(f" - Young's Modulus: {youngs_module_gpa:,.2f} GPa")

    print("Input Parameters:")
    print(f" - Applied Force: {applied_force:,.2f} N")
    print(f" - Cross Sectional Area: {cross_sectional_area:.6f} m^2")
    print(f" - Original Length: {original_length:.4f} m")
    print(f" - Change in Length: {change_in_length:.6f} m")

    print("Calculated Outputs:")
    print(f" - Engineering Stress:    {stress_mpa:,.2f} MPa ({stress_pa:,.2f} Pa)")
    print(f" - Engineering Strain:    {strain:.6f}")
    print(" - " * 25)

    print("Safety Analysis:")
    print(f" - Factor of Safety:      {fos:.2f}")
    print(f" - Safety Status:         {status}")
    print(" = " * 50)

def main():
    while True:
      try:
          run_calculator()
      except KeyboardInterrupt:
          print("\n\nProgram force-closed by user. Existing gracefully...")
          break

      repeat = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
      if repeat != 'y':
          print("Thank you for using the calculator. Program terminated.")
          break

if __name__ == "__main__":
  main()

#end of isaiah's part

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

#start of john's part (task 5)
from dataclasses import dataclass
from typing import List

#===========================================================================
#Helper Functions: Input Validation
def get_positive_float(prompt: str, allow_zero: bool = False) -> float:
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


def get_yes_no(prompt: str) -> bool:
    """Asks a yes/no question and returns True or False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print(" Error: Please enter 'y' or 'n'.")
#===========================================================================

#Task 5: OOP
#--------------------------------------------------------
#dataclass: StressStrainTest
#modeled StressStrainTest parameters as an object
@dataclass
class StressStrainTest:
    force: float            #Applied Force (N)
    area: float             #Cross-sectional Area (m^2)
    original_length: float  #Original Length (m)
    change_in_length: float #Change in Length (m)
#--------------------------------------------------------

#--------------------------------------------------------------------------------
#base class: Material
class Material:
    def __init__(self, name: str, yield_strength: float, elastic_modulus: float):
        self.name = name
        self._yield_strength = yield_strength   #in MPa
        self._elastic_modulus = elastic_modulus #in GPa

    @property
    def yield_strength(self) -> float:
        return self._yield_strength

    @property
    def elastic_modulus(self) -> float:
        return self._elastic_modulus

    #formula for stress: stress = force / area
    def calculate_stress_pa(self, test: StressStrainTest) -> float:
        return test.force / test.area

    #converts pascals to megapascals
    def calculate_stress_mpa(self, test: StressStrainTest) -> float:
        return self.calculate_stress_pa(test) / 1e6

    #formula for strain = change / original
    def calculate_strain(self, test: StressStrainTest) -> float:
        return test.change_in_length / test.original_length

    #converts Young's Modulus in pascals to gigapascals
    def calculate_calculated_modulus(self, test: StressStrainTest) -> float:
        strain = self.calculate_strain(test)
        if strain == 0:
            return 0.0
        return (self.calculate_stress_pa(test) / strain) / 1e9

    #formula for factor of satefy (fos): yield / stress
    def calculate_factor_of_safety(self, test: StressStrainTest) -> float:
        stress_mpa = self.calculate_stress_mpa(test)
        if stress_mpa == 0:
            return 0.0
        return self._yield_strength / stress_mpa

    #status determined by fos
    def determine_safety_status(self, fos: float) -> str:
        if fos >= 1.2:
            return "SAFE"
        elif 1.0 <= fos < 1.2:
            return "CAUTION - Loading near material yield point"
        else:
            return "UNSAFE - Material failure / yielding likely!"

    #special method: string representation
    def __str__(self) -> str:
        return f"{self.name} (Yield Strength: {self._yield_strength} MPa, Young's Modulus: {self._elastic_modulus} GPa)"
#--------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------
#child classes: Metal, Plastic, Material
class Metal(Material):
    def __init__(self, name: str = "Structural Metal", yield_strength: float = 250.0, elastic_modulus: float = 200.0):
        super().__init__(name, yield_strength, elastic_modulus)

class Plastic(Material):
    def __init__(self, name: str = "Polymer Plastic", yield_strength: float = 45.0, elastic_modulus: float = 2.5):
        super().__init__(name, yield_strength, elastic_modulus)

class Composite(Material):
    def __init__(self, name: str = "Carbon Fiber Composite", yield_strength: float = 500.0, elastic_modulus: float = 120.0):
        super().__init__(name, yield_strength, elastic_modulus)
#---------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#composition and system creation | manages a collection of Material objects and compares test outputs
class StressAnalysisSystem:
    #composition
    def __init__(self):
        self.materials: List[Material] = []

    def add_material(self, material: Material):
        self.materials.append(material)

    def compare_and_analyze(self, test: StressStrainTest):
        print("\n" + "=" * 49)
        print(" " * 6 + "MULTIPLE MATERIAL COMPARISON ANALYSIS" + " " * 6)
        print("=" * 49)
        print("Test Setup Parameters:")
        print(f" • Applied Force:        {test.force:,.2f} N")
        print(f" • Cross-Sectional Area: {test.area:.6f} m²")
        print(f" • Original Length:      {test.original_length:.4f} m")
        print(f" • Change in Length:     {test.change_in_length:.6f} m")
        print("-" * 49)

        for mat in self.materials:
            stress_mpa = mat.calculate_stress_mpa(test)
            strain = mat.calculate_strain(test)
            calc_modulus = mat.calculate_calculated_modulus(test)
            fos = mat.calculate_factor_of_safety(test)
            status = mat.determine_safety_status(fos)

            print(f"Material: {mat.name}")
            print(f" • Rated Yield Strength:  {mat.yield_strength:,.2f} MPa")
            print(f" • Rated Young's Modulus: {mat.elastic_modulus:,.2f} GPa")
            print(f" • Calculated Stress:     {stress_mpa:,.2f} MPa")
            print(f" • Calculated Strain:     {strain:.6f}")
            print(f" • Calc. Young's Modulus: {calc_modulus:,.2f} GPa")
            print(f" • Factor of Safety:      {fos:.2f}")
            print(f" • Safety Status:         {status}")
            print("-" * 49)
#-----------------------------------------------------------------------------

#==========================================
#main execution code
def stress_strain_program():

    units = ["N", "m^2", "m", "MPa", "GPa"]

    print("=" * 58)
    print(" " * 6 + "Task 5: Object-Oriented Stress & Strain System" + " " * 6)
    print("=" * 58)

    while True:
        #system creation and populate material hierarchy
        system = StressAnalysisSystem()
        system.add_material(Metal("Steel (Metal)", yield_strength = 250.0, elastic_modulus = 200.0))
        system.add_material(Plastic("ABS (Plastic)", yield_strength = 45.0, elastic_modulus = 2.5))
        system.add_material(Composite("Carbon Fiber (Composite)", yield_strength = 500.0, elastic_modulus = 120.0))

        #user input
        print("\nPlease enter the test parameters below:\n")
        force = get_positive_float(f"Enter applied force (F) in Newton [{units[0]}]: ")
        area = get_positive_float(f"Enter cross sectional area (A) in square meters [{units[1]}]: ")
        orig_len = get_positive_float(f"Enter original length in meters [{units[2]}]: ")
        chg_len = get_positive_float(f"Enter change in length in meters [{units[2]}]: ", allow_zero=True)

        #initiate the inputs into the dataclass object
        test_run = StressStrainTest(force = force, area = area, original_length = orig_len, change_in_length = chg_len)

        #execute the computational analysis
        system.compare_and_analyze(test_run)

        #try again prompt
        if not get_yes_no("\nWould you like to run another OOP test comparison? (y/n): "):
            print("Thank you for using the Task 5 OOP Analyzer. Program terminated gracefully.")
            break
#==========================================

if __name__ == "__main__":
    stress_strain_program()

#end of john's part (task 5)
