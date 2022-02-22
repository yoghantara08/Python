num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
operator = input("Enter operator : ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*" or operator == "x" or operator == "X":
    print(num1 * num2)
elif operator == "/" or operator == ":":
    print(num1 / num2)
else:
    print("Invalid Operator!")
