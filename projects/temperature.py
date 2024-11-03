# An temperature knowing method


units=input("Is this temperature is Celsius  or Fahrenheit (C/F): ")

temperature=float(input("Enter the temperature: "))

if units =="C":
    temperature=round((9*temperature)/5 +32,1)
    print(f"The temperature in fahrenheit is :{temperature}")
elif units =="F":
    temperature=round((temperature-32)*5/9,1)
    print(f"The temperature in Celsius is:{temperature}")

else:
    print(f"{units} is an invalid unit of temperature !")