print("What would you like to calculate?")
print("Simple Interest (SI)")
print("Compound Interest (CI)")
print("Annuity Plan (ANU)")

problem = input()

def SI():
    print("input P")
    P = float(input())
    print("input R")
    R = float(input())
    print("input T")
    T = float(input())

    simpleinterest = P * (1 + (R/100)) * T

    print ("Simple Interest is ", simpleinterest)
    return

def CI():
    print("input P")
    P = float(input())
    print("input R")
    R = float(input())
    print("input T")
    T = float(input())
    print("Input N")
    N = float(input())

    compoundinterest = P * pow((1 + (R/100)), N * T)
    print ("Compound Interest is ", compoundinterest)
    return

def ANU():
    print("input P")
    P = float(input())
    print("input R")
    R = float(input())
    print("input T")
    T = float(input())
    print("Input M")
    M = float(input())
    print("input N")
    N = float(input())

    annuityplan = (P * M * T) * (pow((1 + (R/N)), N * T) - 1) / (R/N)
    print ("Annuity Plan is ", annuityplan)
    return

if problem == "SI":
    SI()
elif problem == "CI":
    CI()
elif problem == "ANU":
    ANU()
else:
    print("Invalid input. Please enter SI, CI, or ANU.")