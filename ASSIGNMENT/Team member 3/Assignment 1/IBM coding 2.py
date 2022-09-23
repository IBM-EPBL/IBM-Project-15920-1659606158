def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
print("please select the mathematical operation -\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n")
select = (input("Enter the operation :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == "addition":
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == "subtraction":
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == "multiplication":
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == "division":
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Invalid input")
