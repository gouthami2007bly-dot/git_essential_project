import json
import os

EXPENSES_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
        with open(EXPENSES_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


print("student expense tracker  ")


def add_expense(expense):
    new_expense = input("enter expense: ")
    expense.append(new_expense)
    save_expenses(expense)
    print(f"expense {new_expense} added successfully")


def view_expense(expense):
    if not expense:
        print("no expenses found")
    else:
        print("expense list:")
        for i, item in enumerate(expense, 1):
            print(f"{i}. {item}")
def split_expense(expense):
    if not expense:
        print("no expenses to split")
        return
    total_expense = sum(float(item) for item in expense)
    num_people = int(input("enter number of people to split the expense: "))
    if num_people <= 0:
        print("number of people must be greater than zero")
        return
    split_amount = total_expense / num_people
    print(f"total expense: {total_expense}")
    print(f"each person should pay: {split_amount}")        

def main():
    expense = load_expenses()
    while True:
        print("\n1. Add expense")
        print("2. View expense")
        print("3. Exit")
        choice = input("enter your choice: ")
        if choice == "1":
            add_expense(expense)
        elif choice == "2":
            view_expense(expense)
        elif choice == "3":
            print("exiting the program")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
