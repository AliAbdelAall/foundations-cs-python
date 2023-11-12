import json
# imported for choices "7. Save Tabs" and "8. Import Tabs" and used in saveTabs() and importTabs() functions
# learned the basics of JSON from : https://www.programiz.com/python-programming/json

from urllib.error import URLError
# imported the handle user input to get a valid URL which we can access and used in checkUrl() function
# leaned about it from : https://docs.python.org/3/library/urllib.error.html and from Google search

from urllib.request import urlopen
# imported for choice "3. Switch Tab" and used in switchTab() function
# learned about web scraping from : https://realpython.com/python-web-scraping-practical-introduction/

current_tabs = []


# ------- choice 1 ------ #

# ----- Inputs ---- #
def checkUrl():  # O(N) N is the wrong inputs by the user
    url = input("Enter Tab URL: ").strip()
    while True:  # we use while True to we keep asking the user for URL until the URL is valid to return
        try:  # try block will try to execute the block inside it if an error was raised except block will handle it
            urlopen(url)  # O(1) # urlopen() tries to access the HTML code of a web and returns an object
            return url  # when we return the loop will break
        except ValueError:  # if URL was not in URL format the ERROR will be handled here
            print("This is not a URL")
            url = input("Enter Tab URL again: ").strip()
            # we ask for the URL again from the user to avoid infinite loop
        except URLError:
            # if the URL was not accessible, an appropriate message will be displayed
            print("This URL is INVALID")
            url = input("Enter Tab URL again: ").strip()


# ----- Function ---- #
def openTab():  # O(1) since this only creates a dictionary and append it to the list of tabs
    new_tab = {}
    # this function creates a tab as a dictionary and append it to the list "current_tabs"

    title = input("Enter Tab Title: ").strip()
    url = checkUrl()  # by calling checkUrl() we make sure the user inputs a valid URL

    new_tab["Title"] = title
    new_tab["URL"] = url
    # we create the keys and put the user input as there values,
    # so we can have instant access values, since all tabs have the same keys ("Title", "URL")

    current_tabs.append(new_tab)  # we add the new tab to the list
    print(f"New tab opened with Title : {title}")


# ------- choice 2 ------ #

# ----- Inputs ---- #
def inputTabIndex():  # O(N) N: len(list)
    if len(current_tabs) == 0:
        print("there is no opened Tabs currently!you must open a Tab first.")
        return
        # if the list is empty we print a message and we return None

    print(f"\nyou currently have {len(current_tabs)} opened Tab(s):")
    for i in range(len(current_tabs)):
        print(f'{i+1}_ {current_tabs[i]["Title"]}')
        # we print the parent current tabs
    index = input("\nEnter the Index of the Tab: ").strip()
    # if the list is not empty then we ask the user to input the index of the tab
    if index == "":
        return len(current_tabs) - 1  # if the user did not input an index, then no need for extra steps

    while not index.isdigit() or int(index) > len(current_tabs) or int(index) == 0:
        if not index.isdigit():
            print(f"the Index must be a POSITIVE numeric number!")
            index = input("\nEnter the Index of the Tab again: ").strip()
            # here we handle the user input by checking if the number is a positive integer

        elif len(current_tabs) == 1:
            print("you have only 1 Tab opened at index 1")
            index = input("\nEnter the Index of the Tab again: ").strip()
            # here we take handling user input a step further
            # and make sure the user inputs the right index

        else:
            print(f"choose Tab at index 1 --> {len(current_tabs)}")
            index = input("Enter the Index of the Tab again: ").strip()
            # they may seem extra steps here, but it is more user-friendly
            # so the user can understand what is wrong at each step
    index = int(index) - 1
    # we re-assign the index, so we access the real index of the list in the other functions

    print(f"\nTab at Index {index + 1}:")
    print(current_tabs[index]["Title"])
    if "Nested_Tabs" in current_tabs[index]:
        for j in range(len(current_tabs[index]["Nested_Tabs"])):
            print(f'\t{current_tabs[index]["Nested_Tabs"][j]["Title"]}')
    # and after the user chooses the index we display the tab at this index and its nested-tabs if there are any
    return index


# ----- Function ---- #
def closeTab(index):  # O(1)  here we pop a tab and print it
    if index is None:  # if we have no opened tabs
        return
    current_tabs.pop(index)
    print(f"Tab at index {index+1} has been closed.")


# ------- choice 3 ------ #

# ----- Inputs ---- #

def inputNestedTabIndex():  # O(N) N: Wrong input by the user
    index = input("Enter Index: ")
    while not index.isdigit():
        print("Index must me a Positive Numeric number!")
        index = input("Enter Index again: ")
    return int(index)


def getUrl(index):  # O(N) N: wrong inputs by the user
    if index is None:
        return  # if the list is empty we return None
    elif "Nested_Tabs" not in current_tabs[index]:
        return current_tabs[index]["URL"]
        # if the tab does not have nested tabs it will print the HTM right away
    else:
        print("Enter 1 for parent tab, 2 for nested tab(s): ")
        choice = inputNestedTabIndex()
        # we let the user choose between parent or nested tab the print it HTML code
        while choice != 1 and choice != 2:
            print("Enter 1 for parent tab, 2 for nested tab(s): ")
            choice = inputNestedTabIndex()

        if choice == 1:
            return current_tabs[index]["URL"]  # we return the parent tab URL if the user chooses 1
        else:
            print()  # for nested tabs we print the nested tab inside the parent tab and let the user choose
            for j in range(len(current_tabs[index]["Nested_Tabs"])):
                print(f'{j+1}_ {current_tabs[index]["Nested_Tabs"][j]["Title"]}')
            print()
            nested_index = inputNestedTabIndex()
            while nested_index > len(current_tabs[index]["Nested_Tabs"]) or nested_index == 0:
                print("Invalid Index!")
                nested_index = inputNestedTabIndex()
            # after the user choose the index of the nested tab we return its URL
            return current_tabs[index]["Nested_Tabs"][nested_index - 1]["URL"]


# ----- Function ---- #
def switchTab(url):  # O(N) N: the size of HTML code in the page
    if url is None:
        return
    page = urlopen(url)  # O(1)
    # since we have a function above to check URL validity we are safe to go here
    html = page.read().decode("utf-8")  # O(N) N: the size of HTML code in the page
    # and here we read and decode the object "page" the get the HTML code as text

    print(f"\nHTML code:\n{html}")


# ------- choice 4 ------ #

def displayTabs():  # O(N^2) N: opened tabs
    if len(current_tabs) == 0:  # if there is no opened tabs a message will be displayed
        print("There is no opened tabs to display!")
    else:
        print(f"you currently have {len(current_tabs)} opened Tab(s):\n")
        for i in range(len(current_tabs)):  # we display the the parent tab(s)
            print(f'{current_tabs[i]["Title"]}')
            if "Nested_Tabs" in current_tabs[i]:
                for j in range(len(current_tabs[i]["Nested_Tabs"])):
                    print(f'\t{current_tabs[i]["Nested_Tabs"][j]["Title"]}')
                    # if there are nested tab(s) we display them under the parent tab hierarchically


# ------- choice 5 ------ #

# ----- inputs ---- #
def inputNestedTab():
    # O(N) since we have checkUrl() inside this function N : Wrong inputs by the user
    nested_tab = {}
    title = input("Enter Tab Title: ").strip()
    url = checkUrl()  # O(N)
    nested_tab["Title"] = title
    nested_tab["URL"] = url
    return nested_tab
    # this function creates a nested tab as a dictionary


def displayNestedTabMenu():  # O(1) we display a menu
    print("""
    1. Add a Nested-Tab
    2. Change Tab index
    3. Back to Menu
    """)


# ----- Function ---- #
def openNestedTab(index):  # O(N) since we call inputNestedTab() inside it
    if "Nested_Tabs" in current_tabs[index]:
        nested_tab = inputNestedTab()   # O(N)
        current_tabs[index]["Nested_Tabs"].append(nested_tab)
    else:
        nested_tab = inputNestedTab()  # O(N)
        current_tabs[index]["Nested_Tabs"] = [nested_tab]

    print(f'A new nested-Tab:"{nested_tab["Title"]}" was added to Tab:"{current_tabs[index]["Title"]}"')


# ------- choice 6 ------ #
def clearAllTabs():  # O(1) since we only assign to an empty list
    global current_tabs  # the global statement let us access the global variable like it is outside the function
    current_tabs = []  # we re-assign the variable to an empty list instead of looping to pop all elements inside
    print("All tabs has been cleared.")


# ------- choice 7 ------ #

# ----- inputs ---- #
def checkFilePath():  # O(N) N: wrong inputs by the user
    file_path = input("Enter file path: ").strip()
    while True:
        try:  # we try to open the file as "read" to check its validity
            with open(file_path, "r") as file:  # O(1) it try to access the file
                pass
            file.close()  # if the file is valid we close it and return the file path
            return file_path
        except PermissionError:
            # if the selected file is a folder it will be handled here
            print("File path is INVALID")
            file_path = input("Enter file path again: ").strip()
        except FileNotFoundError:  # if the input was not a file path or the file does not exist it will be handled
            print("File path is INVALID")
            file_path = input("Enter file path again: ").strip()


# ----- Function ---- #
def saveTabs():  # O(N) N : the size of data going to the file
    if len(current_tabs) == 0:
        print("There is no Tabs to save! Open a tab first.")
        return
    file_path = checkFilePath()
    with open(file_path, "w") as file:
        # we open the file in "write" mode to save the data inside the file
        # if the file exists all data on it will be wiped, else a new file will be created
        json.dump(current_tabs, file, indent=4)
        # we dump the tabs inside the file with indentation = 4 for better visual reasons
    file.close()
    # we make sure to close the file after we finish saving, so we can access it again without terminating the program
    print("All current tabs was SAVED.")


# ------- choice 8 ------ #
def importTabs():  # O(N) N : the size of data in the file
    file_path = checkFilePath()
    with open(file_path, "r") as file:  # we open the file in "read" mode to access the data inside the JSON file
        data = json.load(file)
        # we load the data inside the file and store it inside a variable for later usage
        for i in range(len(data)):
            current_tabs.append(data[i])
        # we loop to add all the data inside the list "data" to ADD them to current_tabs list
    file.close()  # and we close the file
    print("All tabs from selected file was IMPORTED.")


# ------- User greeting ------- #
def greetUser():  # O(1)
    name = input("Enter your Name: ").strip()

    if name == "":  # this was just a little nice thing to add
        name = "User"

    print(f"Welcome, {name}!")
    return name


# ------- Menu Display ------- #
def displayMenu():  # O(1) we only print
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
def inputChoice():  # O(N) N: wrong input(s) by the user
    choice = input("Enter a number as your choice: ").strip()

    while not choice.isdigit():
        print("your choice must be a POSITIVE numeric number!")
        choice = input("Enter a number as your choice again: ").strip()

    return int(choice)


# ------- Main ------- #
def main():  # overall O(N^2) ;choice 4 displayTabs() is the dominant/slowest
    name = greetUser()  # O(1)
    displayMenu()  # O(1)
    choice = inputChoice()  # O(N)

    while choice != 9:
        if choice == 1:
            openTab()  # O(1)

        elif choice == 2:
            closeTab(inputTabIndex())  # O(N)

        elif choice == 3:
            switchTab(getUrl(inputTabIndex()))  # O(N)

        elif choice == 4:
            displayTabs()  # O(N^2)

        elif choice == 5:
            index = inputTabIndex()  # O(N)
            if index is not None:  # if the list of tabs is empty
                displayNestedTabMenu()  # O(1)
                choice_n = inputChoice()  # O(N)

                while choice_n != 3:
                    if choice_n == 1:
                        openNestedTab(index)  # O(N)
                    elif choice_n == 2:
                        break  # if the user want to change index we break out of the inner loop to access the main loop

                    else:
                        print("Invalid choice!")

                    displayNestedTabMenu()  # O(1)
                    choice_n = inputChoice()  # O(N)

                if choice_n == 2:
                    choice = 5  # after breaking out of the loop we assign choice = 5 to enter choice 5 again
                    continue  # and then the "continue" statement will let us skip all steps after it and loop again

        elif choice == 6:
            clearAllTabs()  # O(1)

        elif choice == 7:
            saveTabs()  # O(N)

        elif choice == 8:
            importTabs()  # O(N)

        else:
            print("Invalid choice!")

        displayMenu()  # O(1)
        choice = inputChoice()  # O(N)
    print(f"We hope you enjoyed the program, {name}!")
    print("Exiting the program...")


main()
