from logging import warning
from os import environ, getcwd

errorCount = int(0)

dataFile = f"{str(environ.get('DATA_PATH') or getcwd())}/inventory.txt"

def load_inventory() -> list[list]:
    with open(dataFile, 'r') as file:
        return [line.strip().split(',') for line in file]

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

def get_value_input() -> list:
    userNameInput = input("Enter product name: ")
    userQuantityInput = input("Enter a stock quantity: ")
    if userNameInput == "quit" or userQuantityInput == "quit":
        return ["quit", int(0)]
    try:
        addedInventory = int(userQuantityInput)
        if addedInventory < 0:
            warnUser("Negative number not accepted, try again!")
            return [str(""), int(0)]
        else:
            return [str(userNameInput), int(addedInventory)]
    except:
        warnUser(f"Input of type {str(type(userInput))} not accepted, try again!")
        return [str(""), int(0)]

def process_delivery(current_total: int, new_value: int) -> int:
    new_total = int(current_total) + int(new_value)
    return new_total

def calculate_tax(amount: int) -> float:
    return (float(0.1) * amount)

def generate_report(total_units: int, failed_attempts: int) -> None:
    print(f"Total Units Processed: {str(total_units)}")
    print(f"Number of Failed/Rejected Entries: {str(failed_attempts)}")

inventory = load_inventory()

userData = ""
while userData != "quit":
    userData = get_value_input()
    if userData[0] == "quit":
        print("Goodbye!")
        break
    if int(userData[1]) > 0:
        inventory = process_delivery(inventory, int(userData[1]))
        print(f"Tax for delivery amount {int(userData[1])}: {calculate_tax(int(userData[1]))}")
    # it doesn't make sense that the program should be blocked if the inventory is more than 500, especially since history is now persistent. if persistent inventory is forever above 500, the program will always quit after 1 user prompt.
    # if inventory > 500:
    #     print("Inventory has overstocked!")
    #     break
generate_report(inventory, errorCount)
