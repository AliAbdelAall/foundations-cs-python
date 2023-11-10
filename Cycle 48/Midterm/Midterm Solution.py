current_tabs = []


# ------- choice 1 ------ #
def openTab():
    new_tab = {}

    title = input("Enter your new Tab Title: ")
    url = input("Enter your new Tab URL: ")

    new_tab["Title"] = title
    new_tab["URL"] = url

    current_tabs.append(new_tab)
    print(f"New tab opened with Title : {title}")


# ------- choice 2 ------ #

# ----- Inputs ---- #
def inputTabIndex():
    if len(current_tabs) == 0:
        return
    print(f"you have {len(current_tabs)} opened Tabs.")
    index = input("Enter the Index of the Tab you wish to close: ")

    while not index.isdigit():
        print("the Index must be numeric!")
        index = input("Enter the Index of the Tab you wish to close again: ")

    if len(current_tabs) >= 1:
        while int(index) >= len(current_tabs):
            print(f"you have {len(current_tabs)} opened Tabs.")

            if len(current_tabs) == 1:
                print("you have only 1 Tab opened at index 0")
                index = input("Enter the Index of the Tab you wish to close again: ")
            elif len(current_tabs) > 1:
                print("choose Tab at index 0 --> {len(current_tabs) - 1}")
                index = input("Enter the Index of the Tab you wish to close again: ")

    return index


# ----- Function ---- #
def closeTab(index):
    if index is None:
        print("there is no opened Tabs currently!you must open a Tab first.")

    elif index == "":
        current_tabs.pop()
        print(f"Tab at index {len(current_tabs) - 1} has been closed.")

    else:
        current_tabs.pop(int(index))
        print("Tab at index ", index, " has been closed.")


# ------- choice 4 ------ #

def displayTabs():
    if len(current_tabs) == 0:
        print("There is no opened tabs to display!")
    for i in range(len(current_tabs)):
        print(f'Tab{i + 1} : {current_tabs[i]["Title"]}')
        if "Nested_Tabs" in current_tabs[i]:
            for j in range(len(current_tabs[i]["Nested_Tabs"])):
                if current_tabs[i]["Nested_Tabs"][j] != current_tabs[i]["Nested_Tabs"][-1]:
                    print(f'Nested-Tab{j + 1} : {current_tabs[i]["Nested_Tabs"][j]["Title"]}, ', end='')
                else:
                    print(f'Nested-Tab{j + 1} : {current_tabs[i]["Nested_Tabs"][j]["Title"]}')


# ------- choice 5 ------ #

# ----- inputs ---- #
def inputNestedTab():
    nested_tab = {}
    title = input("Enter the Title of the Nested-Tab: ")
    content = input("Enter the content of the Nested-Tab: ")
    nested_tab["Title"] = title
    nested_tab["Content"] = content
    return nested_tab


def displayNestedTabMenu():
    print("""
    1. Add a Nested-Tab
    2. Change Tab index
    3. Back
    """)


# ----- Function ---- #
def openNestedTab(index):
    if len(current_tabs) == 0:
        print("There is no opened tabs!open a tab first")

    if index == "":
        ind = -1
    else:
        ind = int(index)

    if "Nested_Tabs" in current_tabs[ind]:
        print(f'This Tab have {len(current_tabs[-1]["Nested_Tabs"])} Nested-Tabs')
        current_tabs[ind]["Nested_Tabs"].append(inputNestedTab())
    else:
        print("This Tab does not have Nested-Tabs")
        current_tabs[ind]["Nested_Tabs"] = [inputNestedTab()]


# ------- User login & greeting ------- #
def greetUser():
    print("Log-in:")
    username = input("Enter your Username: ")

    while username == "":
        print("you must enter a Username!")
        username = input("Enter your Username again: ")

    print(f"Welcome to our program, {username}!")


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
            openTab()

        elif choice == 2:
            closeTab(inputTabIndex())

        elif choice == 3:
            pass

        elif choice == 4:
            displayTabs()

        elif choice == 5:
            index = inputTabIndex()
            displayNestedTabMenu()
            choice_n = inputChoice()

            while choice_n != 3:
                if choice_n == 1:
                    openNestedTab(index)

                elif choice_n == 2:
                    choice = 5
                    continue

                else:
                    print("Invalid choice!")

                displayNestedTabMenu()
                choice_n = inputChoice()

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
