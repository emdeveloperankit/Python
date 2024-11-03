# This is an weight converter in the python

weight=float(input("Enter your weight :"))

unit=input("Kilograms or Pounds? (K or L):")

if unit =="K":
    weight=weight*2.205
    unit="Lbs."
    print(f"Your weight is:{round(weight,1)}{unit}")

elif unit=="L":
    weight=weight / 2.205
    unit="Kgs."
    print(f"Your weight is:{round(weight,1)}{unit}")
else:
    print(f"{unit} was not valid ") # remove these all below comments then it will works properly

# print(f"Your weight is:{round(weight)}{unit}")

# This is a weight converter in Python

# weight = float(input("Enter your weight: "))

# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} is not a valid input.")
