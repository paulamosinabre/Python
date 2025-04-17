from calculator import Calculator

def main():
    calc = Calculator()
    password = input("Enter the passcode to unlock the secret operation: ")
    calc.set_password(password)
    print("Access Granted!\n")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")    
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    operation = int(input("Enter your choice: "))

    if operation == 1:
        print(f"Result: {num1} + {num2} = {calc.add(num1,num2)}")
    elif operation == 2:
        print(f"Result: {num1} - {num2} = {calc.subtract(num1,num2)}")
    elif operation == 3:
        print(f"Result: {num1} * {num2} = {calc.multiply(num1,num2)}")
    elif operation == 4:
        print(f"Result: {num1} / {num2} = {calc.divide(num1,num2)}")
    elif operation == 5:
        passcode = input("\nEnter passcode: ")
        calc.unlock_secret(passcode)

        if(calc.is_secret_unlocked()):
            print(f"Result: {num1} ** {num2} = {calc.power(num1,num2)}")
        else:
            print("Accesss Denied!")
    else:
        print("Invalid number!")

main()

