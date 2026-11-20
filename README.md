
def calculator():
    print("\n--- Arithmetic Calculator ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

   choice = input("Choose operation (1-4): ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid choice!")


def km_to_miles():
    km = float(input("Enter kilometres: "))
    miles = km * 0.621371
    print("Miles:", round(miles, 2))


def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", round(fahrenheit, 2))


def currency_converter():
    print("\n1. INR to USD")
    print("2. USD to INR")

    choice = input("Choose conversion: ")

    # Example rates only; update with current rates
    inr_to_usd = 1 / 88
    usd_to_inr = 88

    amount = float(input("Enter amount: "))

    if choice == "1":
        print("USD:", round(amount * inr_to_usd, 2))
    elif choice == "2":
        print("INR:", round(amount * usd_to_inr, 2))
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n===== INTERACTIVE CALCULATOR =====")
        print("1. Arithmetic Calculator")
        print("2. KM to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. Currency Converter")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            km_to_miles()
        elif choice == "3":
            celsius_to_fahrenheit()
        elif choice == "4":
            currency_converter()
        elif choice == "5":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice! Please try again.")


main()
