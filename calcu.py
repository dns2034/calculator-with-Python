class calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            break

        if operation in ['+', '-', '*', '/']:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except ValueError:
                print("INVALID INPUT! Please enter a number.")
                continue

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    result = "Error! Division by zero."
                else:
                    result = num1 / num2

            print(result)
        else:
            print("INVALID ERROR! Please enter +, -, *, or /.")

if __name__ == "__main__":
    calculator()



