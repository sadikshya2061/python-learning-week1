# Simple Calculator with basic operations
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations: +, -, *, /, ^, %")
    
    while True:
        try:
            # Get input
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /, ^, %) or 'q' to quit: ")
            
            if operation.lower() == 'q':
                print("Goodbye!")
                break
                
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            elif operation == '^':
                result = num1 ** num2
            elif operation == '%':
                result = num1 % num2
            else:
                print("Invalid operation. Please try again.")
                continue
            
            # Show result
            print(f"Result: {num1} {operation} {num2} = {result}")
            
            # Ask to continue
            again = input("Calculate again? (y/n): ").lower()
            if again != 'y':
                print("Thank you! Goodbye!")
                break
                
        except ValueError:
            print("Error: Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()