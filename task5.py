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