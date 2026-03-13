import numpy as np

def solve_equations():
    print("--- Equation Root Finder ---")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")

    choice = input("\nSelect the operation (1, 2, or 3): ")

    if choice == '1':
        print("\nEnter coefficients for Ax² + Bx + C = 0")
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        c = float(input("Enter C: "))
        coeffs = [a, b, c]

    elif choice == '2':
        print("\nEnter coefficients for Ax³ + Bx² + Cx + D = 0")
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        c = float(input("Enter C: "))
        d = float(input("Enter D: "))
        coeffs = [a, b, c, d]

    elif choice == '3':
        print("\nEnter coefficients for Ax⁴ + Bx³ + Cx² + Dx + E = 0")
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        c = float(input("Enter C: "))
        d = float(input("Enter D: "))
        e = float(input("Enter E: "))
        coeffs = [a, b, c, d, e]

    else:
        print("Invalid choice!")
        return

    # NumPy finds all roots (including imaginary ones) automatically
    roots = np.roots(coeffs)

    print("\nThe roots are:")
    for i, root in enumerate(roots, 1):
        # We round to 2 decimal places to keep it clean
        print(f"Root {i}: {np.round(root, 2)}")

# Run the program
solve_equations()