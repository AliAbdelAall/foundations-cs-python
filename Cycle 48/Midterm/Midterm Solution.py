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


def inputChoice():
    choice = input("Enter a number as your choice: ")
    while not choice.isdigit():
        print("your choice must me numeric number!")
        choice = input("Enter a number as your choice again: ")
    return int(choice)

