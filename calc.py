print("------ Simple Calculator ------")

num1 = float(input("Enter first number: "))
opr = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if opr == "+":
    result = num1 + num2
elif opr == "-":
    result = num1 - num2
elif opr == "*":
    result = num1 * num2
elif opr == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero."
else:
    result = "Invalid operator."

print("Result:", result)
