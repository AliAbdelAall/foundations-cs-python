from urllib.request import urlopen

# imported for choice "3. Switch Tab" and used in switchTab() function
# learned about web scraping from : https://realpython.com/python-web-scraping-practical-introduction/
current_tabs = []


# ------- choice 1 ------ #

# ----- Inputs ---- #
def checkUrl():  # O(N) N is the wrong inputs by the user
    url = input("Enter your new Tab URL: ")
    while True:  # we use while True to we keep looping util the URL is valid to return
        try:
            urlopen(url)  # this function tries to access the HTML code of a web and returns an object
            return url  # when we return the loop will break
        except IOError:
            # if the web's HTML could not be accessed, "urlopen()" will raise an error
            # and to avoid that we added try and except to it
            # "except IOError" will not let "urlopen()" to raise an error if it could not return the object
            # instead it will print this message below
            print("This URL is INVALID")


# ----- Function ---- #
def openTab():  # O(1) since this only creates a dictionary and append it to the list of tabs
    new_tab = {}
    # this function creates a tab as a dictionary and append it to the list "current_tabs"

    title = input("Enter your new Tab Title: ")
    url = input("Enter your new Tab URL: ")

    new_tab["Title"] = title
    new_tab["URL"] = url
    # we create the keys and put the user input as there values,
    # so we can have instant access values, since all tabs have the same keys ("Title", "URL")

    current_tabs.append(new_tab)
    print(f"New tab opened with Title : {title}")


# ------- choice 2 ------ #

# ----- Inputs ---- #
def inputTabIndex():  # O(N) or O(N+M) N: len(list) , M: wrong inputs
    if len(current_tabs) == 0:
        print("there is no opened Tabs currently!you must open a Tab first.")
        return
        # if the list is empty then there is no tabs to open, so we return None
    else:
        print(f"\nyou currently have {len(current_tabs)} opened Tab(s):")
        for i in range(len(current_tabs)):
            print(f'{i}. {current_tabs[i]["Title"]}')
        index = input("\nEnter the Index of the Tab: ")
        # if the list is not empty then we ask the user to input the index of the tab

        while not index.isdigit() or int(index) >= len(current_tabs):
            if not index.isdigit():
                print(f"the Index must be a POSITIVE numeric number!")
                index = input("\nEnter the Index of the Tab again: ")
                # here we handle the user input by checking if the number is a positive integer

            elif len(current_tabs) == 1:
                print("you have only 1 Tab opened at index 0")
                index = input("\nEnter the Index of the Tab again: ")
                # here we take handling user input a step further
                # and make sure the user inputs the right index

            elif len(current_tabs) > 1:
                print(f"choose Tab at index 0 --> {len(current_tabs) - 1}")
                index = input("Enter the Index of the Tab again: ")
                # they may seem extra steps here, but it is more user-friendly
                # so the user can understand what is wrong at each step
        print(f"Tab at Index {index}:")
        print(current_tabs[int(index)]["Title"])
        if "Nested_Tabs" in current_tabs[int(index)]:
            for j in range(len(current_tabs[int(index)]["Nested_Tabs"])):
                print(f'\t{current_tabs[int(index)]["Nested_Tabs"][j]["Title"]}')

        return index
        # we return the index as a string in case the user did not input an index,
        # so we can access the last opened tab


# ----- Function ---- #
def closeTab(index):  # O(1)  here we pop a tab and print it
    if index is None:  # if we have no opened tabs
        return
    i = -1 if index == "" else int(index)  # learned about this method while practicing "leetcode"
    # we save the index in a variable depending on the returned "index" from  inputTabIndex() function
    # so we avoid repetition in our code
    current_tabs.pop(i)
    print(f"Tab at index {i} has been closed.")


# ------- choice 3 ------ #
def switchTab(index):
    if index is None:
        return
    i = -1 if index == "" else int(index)
    # we have the same method we used in the recent function

    try:
        url = current_tabs[i]["URL"]  # we get the URL of the selected tab
        page = urlopen(url)
        html = page.read().decode("utf-8")
        print("\nRequest to the HTML code SUCCEEDED!\n")
        print(html)
    except IOError:
        print("\nRequest to the HTML code FAILED!\n")


# ------- choice 4 ------ #

def displayTabs():
    if len(current_tabs) == 0:
        print("There is no opened tabs to display!")
    else:
        print(f"you currently have {len(current_tabs)} opened Tab(s).")
        for i in range(len(current_tabs)):
            print(f'\n{i}. {current_tabs[i]["Title"]}')
            if "Nested_Tabs" in current_tabs[i]:
                for j in range(len(current_tabs[i]["Nested_Tabs"])):
                    print(f'\t{j}. {current_tabs[i]["Nested_Tabs"][j]["Title"]}')


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
    3. Back to Menu
    """)


# ----- Function ---- #
def openNestedTab(index):
    i = -1 if index == "" else int(index)

    if "Nested_Tabs" in current_tabs[i]:
        print(f'Tab at index {i} have {len(current_tabs[i]["Nested_Tabs"])} Nested-Tabs')
        print(f'{i}. {current_tabs[i]["Title"]}')
        for j in range(len(current_tabs[i]["Nested_Tabs"])):
            print(f'\t{i}. {current_tabs[i]["Nested_Tabs"][j]["Title"]}')
        current_tabs[i]["Nested_Tabs"].append(inputNestedTab())
    else:
        print("This Tab does not have Nested-Tabs")
        current_tabs[i]["Nested_Tabs"] = [inputNestedTab()]


# ------- choice 5 ------ #
def clearAllTabs():
    for i in range(len(current_tabs)):
        current_tabs.pop()
    print("All tabs has been cleared.")


# ------- User greeting ------- #
def greetUser():
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
        print("your choice must be numeric number!")
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
            switchTab(inputTabIndex())

        elif choice == 4:
            displayTabs()

        elif choice == 5:
            index = inputTabIndex()
            if index is not None:
                displayNestedTabMenu()
                choice_n = inputChoice()

                while choice_n != 3:
                    if choice_n == 1:
                        openNestedTab(index)
                    elif choice_n == 2:
                        break

                    else:
                        print("Invalid choice!")

                    displayNestedTabMenu()
                    choice_n = inputChoice()

                if choice_n == 2:
                    choice = 5
                    continue

        elif choice == 6:
            clearAllTabs()

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
