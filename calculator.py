print("Welcome to my Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nPerforming all operations:")
print("Addition:", num1, "+", num2, "=", num1 + num2)
print("Subtraction:", num1, "-", num2, "=", num1 - num2)
print("Multiplication:", num1, "*", num2, "=", num1 * num2)

if num2 != 0:
    print("Division:", num1, "/", num2, "=", num1 / num2)
else:
    print("Division:", num1, "/", num2, "= Error: Division by zero is not allowed.")
