print(" = " * 50) 
print(" Engineering Stress and Strain Calculator")
print(" = " * 50)
print(" PLease enter the request values below.\n ")

applied_force = float(input("Enter applied force (F) in Newtown [N]:"))
cross_sectional_area = float(input(" Enter cross sectional area (A) in square meters [m^2]: "))
original_length = float(input(" Enter original length in meters [m]:"))
change_in_length = float(input(" Enter change in length in meters [m]:"))

stress = applied_force / original_length
strain = change_in_length / original_length

print("\n" + "=" * 50)
print(" Calculation results ")
print("=" * 50)

print("Input Parameters:")
print(f" - Applied Force {applued_forceL,.2f}N")
print(f" - Cross Sectional Area: { cross_sectional_area:.6f} m^2")
print(f" - Original Length: {original_length:4f}m")
print(f" - Change in Length: {change_in_length:6f}m")
print(" - " * 50)

print(" Calculated Outputs: ")
print(f" - Engineering Stress: {stress:,.2f}Pa")
print(f" - Engineering Strain: {straing:.6f}")
print( " = " * 50)       
