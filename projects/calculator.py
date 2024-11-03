
# import math

operator=input("Enter an operator(+ - * /)")

num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))

if operator =="+":
    result=num1 + num2
    print(result)
elif operator =="-":
    result =num1 - num2
    print(result)

elif operator =="*":
    result=num1 * num2
    print(result)

elif operator =="/":
    result=num1 / num2
    print(result)
# else:
#     print(f"{operator} is not valid")
    if num2 != 0:  # Checking to avoid division by zero
        
        result = num1 / num2
        print(result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")
