current_tabs = []


def openTab():
    new_tab = {}

    title = input("Enter your new Tab Title: ")
    url = input("Enter your new Tab URL: ")

    new_tab["Title"] = title
    new_tab["URL"] = url

    current_tabs.append(new_tab)


def inputTabIndex():
    print(f"you have {len(current_tabs)} opened.")
    index = input("Enter the Index of the Tab you wish to close: ")

    while not index.isdigit():
        print("the Index must be numeric!")
        index = input("Enter the Index of the Tab you wish to close again: ")

    if len(current_tabs) >= 1:
        while int(index) >= len(current_tabs):
            print(f"you have {len(current_tabs)} opened.")

            if len(current_tabs) == 1:
                print("you have only 1 Tab opened at index 0")
            elif len(current_tabs) > 1:
                print("choose Tab at index 0 --> {len(current_tabs) - 1}")

    return index


# ------- User login & greeting ------- #
def greetUser():
    print("Log-in:")
    username = input("Enter your Username: ")

    while username == "":
        print("you must enter a Username!")
        username = input("Enter your Username again: ")

    print("Welcome to our program", username)


# ------- Menu Display ------- #
def displayMenu():
    print("""
1. Open Tab
2. Close Tab
3. Switch Tab
4. Display All Tabs
5. Open Nested Tab
6. Clear All Tabs
7. Save Tabs
8. Import Tabs
9. Exit
""")


# ------- Choice Input ------- #
def inputChoice():
    choice = input("Enter a number as your choice: ")

    while not choice.isdigit():
        print("your choice must me numeric number!")
        choice = input("Enter a number as your choice again: ")

    return int(choice)


# ------- Main ------- #
def main():
    greetUser()
    displayMenu()
    choice = inputChoice()

    while choice != 9:
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        else:
            print("Invalid choice!")

        displayMenu()
        choice = inputChoice()

    print("you Exited the program...")


main()
