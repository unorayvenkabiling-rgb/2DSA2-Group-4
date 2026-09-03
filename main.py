print(" = " * 50) 
print(" Engineering Stress and Strain Calculator")
print(" = " * 50)
print(" PLease enter the requested values below.\n ")

applied_force = float(input("Enter applied force (F) in Newton [N]:"))
cross_sectional_area = float(input(" Enter cross sectional area (A) in square meters [m^2]: "))
original_length = float(input(" Enter original length in meters [m]:"))
change_in_length = float(input(" Enter change in length in meters [m]:"))

stress = applied_force / original_length
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

#task 2
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

def select_material #material selection
  materials = {
    "1": (Steel, 250.0, 200.0),
    "2": ("Aluminum", 95.0, 69.0),
    "3": ("Titanium, 880.0, 114.0),
  }

  print("\n---Material Selection---)
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
print(f" - Young's Modulus: {youngs_modulus_gpa:,.2f} GPa")

print("Input Parameters:")
print(f" - Applied Force: {applied_force:,.2f} N")
print(f" - Cross Sectional Area: {cross_sectional_area:.6f} m^2")
print(f" - Original Length: {original_length:.4f} m")
print(f" - Change in Length: {change_in_length:.6f} m")

print("Calculated Outputs:")
print(f" - Engineering Stress:    {stress_mpa:,.2f} MPa")
print(f" - Yield Strength: {yield_strength_mpa:,.2f} MPa")
print(f" - Young's Modulus: {youngs_modulus_gpa:,.2f} GPa")

