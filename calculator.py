num1 = float(input("Enter the first number:"))
operator = (input("Enter the operator ( + , - , * , /):"))
num2 = float(input("Enter the second number:"))

if operator == "+":
    print("result =" , num1 + num2)

elif operator == "-":
    print("result =" , num1 - num2)

elif operator == "*":
    print("result = " , num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("result = " , num1 / num2)
    else:
        print("Error: division by zero is not allowed.")

else:
    print("invalid operator:")

    


