from urllib.request import urlopen
# imported for choice "3. Switch Tab" and used in switchTab() function
# learned about web scraping from : https://realpython.com/python-web-scraping-practical-introduction/
import json
# imported for choices "7. Save Tabs" and "8. Import Tabs" and used in saveTabs() and importTabs() functions
# learned the basics of JSON from : https://www.programiz.com/python-programming/json
current_tabs = []


# ------- choice 1 ------ #

# ----- Inputs ---- #
def checkUrl():  # O(N) N is the wrong inputs by the user
    url = input("Enter Tab URL: ")
    while True:  # we use while True to we keep looping util the URL is valid to return
        # urlopen(url) function will raise an error if the object(access to HTML code) was not found
        # or the parameter (url) was not a URL to begin with
        # and to avoid that we added try/except block with 2 except blocks
        try:
            # the try block tries to execute the code inside it
            # if an error was raised it will skip to except part where it will be handled
            urlopen(url)  # urlopen() tries to access the HTML code of a web and returns an object
            return url  # when we return the loop will break
        except ValueError:  # if the parameter (url) was not a URL it will print an appropriate message
            print("This is not a URL!")
            url = input("Enter Tab URL again: ")
            # to avoid going in an infinite loop we ask again for the URL from the user
        except IOError:
            # if the web's HTML could not be accessed, "urlopen()" will raise an error
            # "except IOError" will print an appropriate message instead of program termination
            # this step is necessary when we print the HTLM code in choice 3
            print("This URL is INVALID")
            url = input("Enter Tab URL again: ")


# ----- Function ---- #
def openTab():  # O(1) since this only creates a dictionary and append it to the list of tabs
    new_tab = {}
    # this function creates a tab as a dictionary and append it to the list "current_tabs"

    title = input("Enter Tab Title: ")
    url = checkUrl()

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
            print(f'{i+1}_ {current_tabs[i]["Title"]}')
        index = input("\nEnter the Index of the Tab: ")
        # if the list is not empty then we ask the user to input the index of the tab

        while not index.isdigit() or int(index) > len(current_tabs) or int(index) == 0:
            if not index.isdigit():
                print(f"the Index must be a POSITIVE numeric number!")
                index = input("\nEnter the Index of the Tab again: ")
                # here we handle the user input by checking if the number is a positive integer

            elif len(current_tabs) == 1:
                print("you have only 1 Tab opened at index 1")
                index = input("\nEnter the Index of the Tab again: ")
                # here we take handling user input a step further
                # and make sure the user inputs the right index

            elif len(current_tabs) > 1:
                print(f"choose Tab at index 1 --> {len(current_tabs)}")
                index = input("Enter the Index of the Tab again: ")
                # they may seem extra steps here, but it is more user-friendly
                # so the user can understand what is wrong at each step

        print(f"\nTab at Index {index}:")
        print(current_tabs[int(index)-1]["Title"])
        if "Nested_Tabs" in current_tabs[int(index)-1]:
            for j in range(len(current_tabs[int(index)-1]["Nested_Tabs"])):
                print(f'\t{current_tabs[int(index)-1]["Nested_Tabs"][j]["Title"]}')

        return str(int(index)-1) if index.isdigit() else index
        # we return the index as a string in case the user did not input an index,
        # so we can access the last opened tab


# ----- Function ---- #
def closeTab(index):  # O(1)  here we pop a tab and print it
    if index is None:  # if we have no opened tabs
        return
    i = -1 if index == "" else int(index)
    # learned about this method while practicing "leetcode"
    # we save the index in a variable depending on the returned "index" from  inputTabIndex() function
    # so we avoid repetition in our code
    current_tabs.pop(i)
    print(f"Tab at index {i+1} has been closed.")


# ------- choice 3 ------ #
def switchTab(index):
    # I am not ganna say O(1) here since it there are functions from an imported library
    # which we cannot see the code inside it, here it depends on the functions inside
    if index is None:
        return
    i = -1 if index == "" else int(index)
    # we have the same method we used in the recent function

    url = current_tabs[i]["URL"]  # we get the URL of the selected tab
    page = urlopen(url)  # since we have a function above to check URL validity we are safe to go here
    html = page.read().decode("utf-8")  # and here we read and decode the object "page" the get the HTML code as text

    print(html)


# ------- choice 4 ------ #

def displayTabs():
    if len(current_tabs) == 0:
        print("There is no opened tabs to display!")
    else:
        print(f"you currently have {len(current_tabs)} opened Tab(s):\n")
        for i in range(len(current_tabs)):
            print(f'{current_tabs[i]["Title"]}')
            if "Nested_Tabs" in current_tabs[i]:
                for j in range(len(current_tabs[i]["Nested_Tabs"])):
                    print(f'\t{current_tabs[i]["Nested_Tabs"][j]["Title"]}')


# ------- choice 5 ------ #

# ----- inputs ---- #
def inputNestedTab():
    nested_tab = {}
    title = input("Enter Tab Title: ")
    url = checkUrl()
    nested_tab["Title"] = title
    nested_tab["URL"] = url
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
            print(f'\t{j}. {current_tabs[i]["Nested_Tabs"][j]["Title"]}')
        nested_tab = inputNestedTab()
        current_tabs[i]["Nested_Tabs"].append(nested_tab)
    else:
        print("This Tab does not have Nested-Tabs")
        nested_tab = inputNestedTab()
        current_tabs[i]["Nested_Tabs"] = [nested_tab]

    print(f'A new nested-Tab:"{nested_tab["Title"]}" was added to Tab:"{current_tabs[i]["Title"]}"')


# ------- choice 6 ------ #
def clearAllTabs():
    for i in range(len(current_tabs)):
        current_tabs.pop()
    print("All tabs has been cleared.")


# ------- choice 7 ------ #
def saveTabs():
    if len(current_tabs) == 0:
        print("There is no Tabs to save! Open a tab first.")
        return
    file_path = "E:/PyCharm/PyCharm Community Edition 2023.1/Coding/foundations-cs-python/Cycle 48/Midterm/Save.JSON"
    # file_path = input("Enter the file-path which you want to save the tabs in: ")
    with open(file_path, "w") as file:
        json.dump(current_tabs, file, indent=4)
    file.close()
    print("All current tabs was SAVED.")


# ------- choice 8 ------ #
def importTabs():
    file_path = "E:/PyCharm/PyCharm Community Edition 2023.1/Coding/foundations-cs-python/Cycle 48/Midterm/Load.JSON"
    # file_path = input("Enter the file-path which you want to load the tabs from: ")
    with open(file_path, "r") as file:
        data = json.load(file)
        for i in range(len(data)):
            current_tabs.append(data[i])
    file.close()
    print("All tabs from selected file was IMPORTED.")


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
            saveTabs()

        elif choice == 8:
            importTabs()

        else:
            print("Invalid choice!")

        displayMenu()
        choice = inputChoice()

    print("you Exited the program...")


main()

# Index display
# index user input adjust
# comment
# run multiple situations and retest the code
