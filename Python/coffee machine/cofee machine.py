resources = {"water": 1000, "milk": 200, "coffee": 100}
beverage_prices = {"latte": 2.5, "cappuccino": 3.0, "espresso": 2.0}
cash_box = {"p": 0.99, "n": 3.0, "d": 9., "q": 22.25}
password = "1234"


# Technician mode
def technician_mode():
    while True:
        pass_input = input("Enter the technician password: ")
        if pass_input == password:
            print("Current coin inventory:")
            for coin, count in cash_box.items():
                print(f"{coin}: {count}")
            print("Current resource inventory:")
            for resource, amount in resources.items():
                print(f"{resource}: {amount}")
            action = input("Do you want to refill resources? (yes/no): ")
            if action.lower() == "yes":
                resources["water"] = 1000
                resources["milk"] = 200
                resources["coffee"] = 100
                print("Fill resources to the maximum.")
            turn_off = input("Do you want to turn off? (yes/no): ")
            if turn_off.lower() == "yes":
                print("Turning off...")
                exit()
            else:
                break
        else:
            print("Invalid password. Try again.")
            break


# User mode
def user_mode():
    while True:
        choice = input("Choose a coffee - latte:2.5$, espresso:2.0$, cappuccino:3.0$ (Type l/e/c or q to quit): ")

        if choice not in ["l", "e", "c", "q"]:
            print("Invalid choice. Please select l, e, c, or off.")
            continue
        elif choice == "q":
            break
        selected_beverage = {"l": "latte", "e": "espresso", "c": "cappuccino"}[choice]
        cost = beverage_prices[selected_beverage]
        print(f"Cost of {selected_beverage}: ${cost}")

        while cost > 0:
            coin_input = input('Insert cash, for penny "p" for nickel "n" for dime "d" for quarter "q": ')
            if coin_input not in ["p", "n", "d", "q"]:
                print("Invalid coin. Please insert p, n, d, or q.")
                continue

            coin_value = {"p": 0.01, "n": 0.05, "d": 0.10, "q": 0.25}[coin_input]
            cash_box[coin_input] += 1
            cost -= coin_value

            if cost <= 0:
                if cost < 0:
                    change = abs(cost)
                    print(f"Here is your change: ${change:.2f}")
                print(f"Enjoy your {selected_beverage}!")
                resources["water"] -= 50
                resources["milk"] -= 10
                resources["coffee"] -= 5

                break

            print(f"Amount left to pay: ${cost:.2f}")

            if resources["water"] < 40 or resources["milk"] < 20 or resources["coffee"] < 5:
                print("Resources depleted. Please call a technician.")
                break


# Main program loop
while True:
    print("welcome to the coffe machine!")
    mode = input("Enter a mode (technician/customer): ")
    if mode == "technician":
        technician_mode()
    elif mode == "customer":
        user_mode()
    else:
        print("Invalid mode. Please select technician or user.")
