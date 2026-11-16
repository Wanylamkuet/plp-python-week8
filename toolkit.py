import random

# ========================================================
# Personal Mini-Toolkit (toolkit.py)
# ========================================================

# Welcoming start message
print("Welcome! Ready to get some tasks done, crunch numbers, or play a quick game?")

# List stored outside the menu loop so tasks persist across visits
tasks = []

# Main menu loop - keeps running until the user chooses to Quit
while True:
    print("\n========================================")
    print("   WELCOME TO YOUR PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("Please choose a tool from the menu below:")
    print("1. To-Do List Manager")
    print("2. Simple Calculator")
    print("3. Number-Guessing Game")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ").strip()

    # --------------------------------------------------------
    # TOOL 1: TO-DO LIST MANAGER
    # Allows the user to dynamically add, view, and remove tasks from a list.
    # --------------------------------------------------------
    if choice == "1":
        while True:
            print("\n--- To-Do List Manager ---")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Remove a completed task")
            print("4. Return to Main Menu")

            todo_choice = input("Choose an action (1-4): ").strip()

            if todo_choice == "1":
                if len(tasks) == 0:
                    print("\nYour to-do list is currently empty!")
                else:
                    print("\nYour Current Tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"  {index}. {task}")

            elif todo_choice == "2":
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    tasks.append(new_task)
                    print(f"Added '{new_task}' to your to-do list!")
                else:
                    print("Task cannot be empty.")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("\nNothing to remove — your to-do list is empty!")
                else:
                    print("\nYour Current Tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"  {index}. {task}")

                    try:
                        task_num = int(input("Enter the task number to remove: "))
                        if 1 <= task_num <= len(tasks):
                            removed = tasks.pop(task_num - 1)
                            print(f"Completed and removed: '{removed}'")
                        else:
                            print(f"Please enter a number between 1 and {len(tasks)}.")
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print(f"Oops! '{todo_choice}' is not valid. Choose 1, 2, 3, or 4.")

    # --------------------------------------------------------
    # TOOL 2: SIMPLE CALCULATOR
    # Performs basic arithmetic operations (+, -, *, /) on two user-inputted numbers.
    # --------------------------------------------------------
    elif choice == "2":
        print("\n--- Simple Calculator ---")
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Choose an operation (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif operator == "-":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif operator == "*":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif operator == "/":
                if num2 == 0:
                    print("Error: You cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
            else:
                print(f"Sorry, '{operator}' is not a valid operator. Use +, -, *, or /.")

        except ValueError:
            print("Invalid input! Please make sure you enter numeric values.")

    # --------------------------------------------------------
    # TOOL 3: NUMBER-GUESSING GAME
    # Challenges the user to guess a random secret number between 1 and 20 with hints.
    # --------------------------------------------------------
    elif choice == "3":
        print("\n--- Number-Guessing Game ---")
        secret_number = random.randint(1, 20)
        attempts = 5
        print("I am thinking of a number between 1 and 20.")
        print(f"You have {attempts} attempts to guess it!")

        while attempts > 0:
            try:
                guess = int(input(f"\nEnter your guess ({attempts} attempts left): "))

                if guess < 1 or guess > 20:
                    print("Please keep your guess between 1 and 20.")
                    continue

                if guess == secret_number:
                    print(f"Congratulations! You guessed {secret_number} correctly!")
                    break
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")

                attempts -= 1

            except ValueError:
                print("Please enter a whole number.")

        if attempts == 0:
            print(f"\nOut of attempts! The secret number was {secret_number}. Better luck next time!")

    # --------------------------------------------------------
    # OPTION 4: QUIT
    # Exits the program with a friendly goodbye message.
    # --------------------------------------------------------
    elif choice == "4":
        print("\nThanks for using your Personal Mini-Toolkit. Goodbye!")
        break

    # --------------------------------------------------------
    # INVALID MENU CHOICE HANDLER
    # --------------------------------------------------------
    else:
        print(f"\nOops! '{choice}' is not a valid option. Please enter a number from 1 to 4.")