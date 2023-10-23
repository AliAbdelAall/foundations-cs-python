from datetime import date

today = str(date.today()).replace("-", "")

# ---------------------------------------- File Opening ---------------------------------------- #

file_path = "E:/PyCharm/PyCharm Community Edition 2023.1/Coding/foundations-cs-python/mid-term_2023_Ali_Abdelaal/" \
            "tickets.txt"
# https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy
with open(file_path, 'r') as file:  # we open the file to only read what is inside without changing any data
    lines = file.readlines()  # this method allow us to convert the file into a list of strings

tickets_list = []

for line in lines:  # here we convert the input list of strings into a list of dictionaries
    line_list = line.split(", ")
    tickets_list.append({"ticket_id": line_list[0], "event_id": line_list[1], "username": line_list[2],
                         "timestamp": line_list[3], "priority": int(line_list[4])})

file.close()


# ---------------------------------------- tickets Sort ---------------------------------------- #
def ticketSort(tickets, key1, key2, key3, key4):  # learned merge sort after session 7 with georgio
    if len(tickets) <= 1:
        return tickets  # when we have 1 element in the list it will be automatically sorted, so we return it as the
        # last step of the recursion

    middle = len(tickets) // 2  # we divide the list into 2 half's

    left_half = ticketSort(tickets[:middle], key1, key2, key3, key4)  # we use recursion to divide the list again and
    # again until we have 1 element in the list using the split lists as arguments
    right_half = ticketSort(tickets[middle:], key1, key2, key3, key4)

    return merge(left_half, right_half, key1, key2, key3, key4)  # we use another function for merging to sort the
    # divided  lists


def merge(left, right, key1, key2, key3, key4):
    merged_list = []  # we assign an empty list
    left_index = 0  # we assign 2 indices 1 for each half list, and we set it to 0, so we can always access the first
    right_index = 0  # item in the list

    while left_index < len(left) and right_index < len(
            right):  # here we use a while loop to compare the 2 lists there is elements in 1 of the lists

        if key1 == "ticket_id":  # since the ticket ID we can sort it only by ID no need for extra steps

            if left[left_index][key1] < right[right_index][key1]:
                merged_list.append(left[left_index])
                left_index += 1
                # for each time we append a number from the left/right list we move to the next element by increasing
                # the index by 1
            else:
                merged_list.append(right[right_index])
                right_index += 1

        elif left[left_index][key1] < right[right_index][key1]:
            merged_list.append(left[left_index])
            left_index += 1

        elif left[left_index][key1] == right[right_index][key1]:
            # if the two half's have equal keys we use another key for sorting this can continue to the last key(key4)
            if left[left_index][key2] < right[right_index][key2]:
                merged_list.append(left[left_index])
                left_index += 1

            elif left[left_index][key2] == right[right_index][key2]:

                if left[left_index][key3] > right[right_index][key3]:
                    merged_list.append(left[left_index])
                    left_index += 1
                elif left[left_index][key3] == right[right_index][key3]:

                    if left[left_index][key4] > right[right_index][key4]:
                        merged_list.append(left[left_index])
                        left_index += 1
                    else:
                        merged_list.append(right[right_index])
                        right_index += 1
                else:
                    merged_list.append(right[right_index])
                    right_index += 1

            else:
                merged_list.append(right[right_index])
                right_index += 1

        else:
            merged_list.append(right[right_index])
            right_index += 1  # we do the same index increasing here too

    merged_list.extend(left[left_index:])  # if the list still have element(s) that we did not append to the list
    merged_list.extend(right[right_index:])  # we append it here since the item left is the bigger one

    return merged_list


# ---------------- ticket ID Input ---------------- #
def ticketIdInput():  # this function is to ensure that the ticket ID input is correct
    while True:
        ticket_id = input("Enter ticket ID : ")
        ticket_num = ticket_id[4:]

        if not ticket_id.startswith("tick") or not ticket_num.isdigit() or len(ticket_num) != 3:
            print("Invalid Ticket-ID. ticket-ID should be in 'tickXXX' format, XXX as 3-digit number.")
        else:
            return ticket_id


# ---------------- Event ID Input ---------------- #
def eventIdInput():  # this function is to ensure that the event ID input is correct
    while True:
        event_id = input("Enter event ID : ")
        event_num = event_id[2:]

        if not event_id.startswith("ev") or not int(event_num) or len(event_num) != 3:
            print("Invalid Event-ID. Event-ID should be in 'evXXX' format, XXX as 3-digit number.")
        else:
            return event_id


# ---------------- Priority Input ---------------- #
def intPriorityInput():  # this function is to ensure that the priority as int(input()) is correct
    while True:
        try:
            n = input("Enter the priority number : ")
            num = int(n)

            if num < 0:
                print("priority cannot be negative !")
            else:
                return num

        except ValueError:
            print("this is not a number!")


# ---------------- timestamp Input ---------------- #
def timestampInput():  # this function is to ensure that the timestamp input is correct
    while True:
        try:
            len_date = 8
            timestamp = input("Enter event date as (YYYYMMDD) : ")
            if not timestamp.isdigit():
                raise ValueError  # if the date format is not a number a proper error message will print at line 178

            if len(timestamp) != len_date:
                print("enter the full/correct date format plz!")  # date len should be 8 as "YYYYMMDD"

            elif len(timestamp) == 8:  # slicing the date format : "YYYYMMDD"
                year = int(timestamp[:4])  # year = YYYY
                month = int(timestamp[4:6])  # month = MM
                day = int(timestamp[6:])  # day = DD

                if year < int(today[:4]):
                    print("you cant book a ticket in the past.")

                elif year > (int(today[:4]) + 50):
                    print("booking date limit exceeded!")

                elif month < 0 or month > 12:
                    print("there is only 12 months in a year!")

                elif month in [4, 6, 9, 11] and (day < 0 or day > 30):  # months[4, 6, 9, 11] have 30 days
                    print("in this month day must be between 1--30.")

                elif month == 2:
                    # february have 28 days in a normal year and 29 day in a linear year
                    if year % 4 == 0 and (day < 0 or day > 29):
                        print("in this year february is 29 days.")

                    elif year % 4 != 0 and (day < 0 or day > 28):
                        print("in this year february is 28 days.")

                    else:
                        return timestamp

                elif day < 0 or day > 31:
                    print("in this month day must be between 1--31.")  # since we limited the months to 12 and made a
                # condition for february and the months [4,6,9,11] the rest of the months left are [1,3,5,7,8,10,12]
                # have 31 days
                else:
                    return timestamp

        except ValueError:
            print("this is not a date.")


# ---------------------------------------- 1. Display statistics ---------------------------------------- #
def displayStatistics(tickets):
    event_tickets = {}
    highest_value = 0  # we create the necessary variables for our function
    result = ""
    highest_events = []

    for ticket in tickets:
        event_id = ticket["event_id"]  # with a for loop we check each tick's event ID

        if event_id in event_tickets:
            event_tickets[event_id] += 1  # if event ID Exist in the dictionary w add 1 to the event ticket count
        else:
            event_tickets[event_id] = 1  # if not we create a new key with a value = 1

    for key, value in event_tickets.items():
        print(key, ":", value, "ticket(s)")  # since (tickets) is a list sorted by event ID the dictionary will be too

        if highest_value < value:  # each time we have a bigger value it will become the highest value
            highest_value = value  # and append it to the list of highest events after clearing the previous ones
            highest_events = []
            highest_events.append(key)
            result = f"{key} has the most tickets, {highest_value} ticket(s)."
        elif highest_value == value:
            highest_events.append(key)  # if the highest value have 1 or more equal(s) it will be added to the list

    if len(highest_events) == 1 and len(highest_events) != 0:
        return result  # if only 1 event have the most tickets it will return the first result

    elif len(highest_events) > 1:
        result = ", ".join(highest_events)
        return f"{result} have the most tickets, {highest_value} tickets each."
        # if more than 1 event have the highest tickets it return the 2nd result with the highest equal events
    else:
        return "No Events found"


# ---------------------------------------- 2. book a ticket ---------------------------------------- #
def adminBookTicketInput(tickets):
    username = input("Enter username : ")
    event_id = eventIdInput()  # we use the input functions we created and assign each one to a variable
    timestamp = timestampInput()
    priority = intPriorityInput()

    last_ticket = int(tickets[-1]["ticket_id"][4:])  # since the list is sorted by ticket ID we take the ticket ID
    new_ticket = "tick" + str(last_ticket + 1)  # to auto create a new ticket ID

    if last_ticket >= 999:
        print("maximum ticket counter reached")  # since the ticket ID have 3-digits we are limited to 999 tickets
        # if necessary can be adjusted by adding a function to add : "tick" + ("0"*n) + ticket_num
    else:

        tickets_list.append(
            {"ticket_id": new_ticket,
             "event_id": event_id,
             "username": username,
             "timestamp": timestamp,
             "priority": priority})  # if the last ticket is less than tick999 the ticket will be added to the list

        # here we print the newly booked ticket with its details
        print(f"""
Ticket successfully booked.
    here's your tickets : 
    
    Ticket ID  : {new_ticket}   
    Event ID   : {event_id}
    Username   : {username}
    Event Date : {timestamp}
    Priority   : {priority}
""")


# ---------------------------------------- 3. display all tickets ---------------------------------------- #
def displayTickets(tickets):
    n = 1  # since the list is sorted by date we print all events as (today, tomorrow, ...)
    if len(tickets) > 0:  # using imported date from the pc
        print("This are the tickets in queue : ")

        for i in range(len(tickets) - 1):

            if tickets[i]["timestamp"] >= today:
                ticket_id = tickets[i]['ticket_id']
                event_id = tickets[i]['event_id']
                username = tickets[i]['username']
                timestamp = tickets[i]['timestamp']
                priority = tickets[i]['priority']

                print(
                    f"{n}_{ticket_id}, {timestamp}, {event_id}, {username}, {priority}")
                n += 1

    else:
        print("No tickets found.")


# ---------------------------------------- 4. Change Priority ---------------------------------------- #
def changePriority(tickets):
    ticket_id = ticketIdInput()
    # here we check in the list for the ticket with the specific ticket ID using the ticket ID input function
    for i in range(len(tickets) - 1):

        if tickets[i]["ticket_id"] == ticket_id:  # when the ticket is found we print its details
            print(f"""
Ticket found: 

    Ticket ID  : {tickets[i]["ticket_id"]}
    Event ID   : {tickets[i]["event_id"]}
    Username   : {tickets[i]["username"]}
    Event Date : {tickets[i]["timestamp"]}
    Priority   : {tickets[i]["priority"]}
            """)

            priority = intPriorityInput()  # here we set the new priority for the ticket
            old_priority = tickets[i]["priority"]  # and print old and current priority
            tickets[i]["priority"] = priority
            return f"priority for this ticket has changed from '{old_priority}' to '{priority}'"

    return f"{ticket_id} does not exist."  # if ticket not found an appropriate message is displayed


# ---------------------------------------- 5. del Ticket ---------------------------------------- #
def delTicket(tickets):
    ticket_id = ticketIdInput()

    for i in range(len(tickets)):  # here we search for the ticket in the list
        if tickets[i]["ticket_id"] == ticket_id:
            # if the ticket is found we print its details
            print(f"""
Ticket found: 

    Ticket ID  : {tickets[i]["ticket_id"]}
    Event ID   : {tickets[i]["event_id"]}
    Username   : {tickets[i]["username"]}
    Event Date : {tickets[i]["timestamp"]}
    Priority   : {tickets[i]["priority"]}
            """)

            tickets.pop(i)  # ticket removed
            return f"Ticket _{ticket_id}_ has been removed"

    return f"{ticket_id} does not exist."  # if ticket not found an appropriate message is displayed


# ---------------------------------------- 6. Run Events ---------------------------------------- #
def RunEvents(tickets):
    today_event_index = []  # we make an empty list to fill with the index of tickets of today's events
    ticket_count = 1

    print("today's event tickets:")

    for i in range(len(tickets) - 1):

        if tickets[i]["timestamp"] == today:  # if the date of the ticket is today
            today_event_index.insert(0, i)  # we add the indices of the tickets here
            # we print the details of each ticket
            print(f"""
  {ticket_count}-Ticket ID  : {tickets[i]["ticket_id"]}
    Event ID   : {tickets[i]["event_id"]}
    Username   : {tickets[i]["username"]}
    Event Date : {tickets[i]["timestamp"]}
    Priority   : {tickets[i]["priority"]}""")
            ticket_count += 1  # ticket count is just for display, so we count how many tickets we have for today

    if len(today_event_index) != 0:  # we have at least 1 event happening on today's date
        for index in today_event_index:  # after printing all tickets details
            tickets.pop(index)  # we remove them from the list

    else:
        print("No Tickets Found.")  # if no tickets found an appropriate message is displayed


# ---------------------------------------- 1. Book a Ticket (user) ---------------------------------------- #
def userBookTicket(tickets, user_type):
    username = user_type
    event_id = eventIdInput()  # we use the input function assigned as variables
    timestamp = timestampInput()  # same as admin Booking Ticket function but with fewer features
    priority = 0

    last_ticket = int(tickets[-1]["ticket_id"][4:])  # since the list is sorted by ticket ID we take the ticket ID
    new_ticket = "tick" + str(last_ticket + 1)  # to auto create a new ticket ID

    if last_ticket >= 999:
        print("maximum ticket counter reached")  # since the ticket ID have 3-digits we are limited to 999 tickets
    else:
        tickets_list.append(
            {"ticket_id": new_ticket,
             "event_id": event_id,            # we add the new ticket to the list
             "username": username,
             "timestamp": timestamp,
             "priority": priority})
        # we print the details
        print(f"""
Ticket successfully booked.
    here's your ticket : 

    Ticket ID  : {new_ticket}
    Event ID   : {event_id}
    Username   : {username}
    Event Date : {timestamp}
    Priority   : {priority}
""")


# ---------------- Save Option Input (admin) ---------------- #
def saveChangesInput():   # input for admin option to save or no
    while True:
        answer = input("Do you want to save the changes you made? y(yes)/n(no) : ")
        if answer != "y" and answer != "n":
            print("Pleas answer with y/(yes) and n/(no) : ")
        else:
            return answer


# ---------------------------------------- Save to file ---------------------------------------- #
def saveChanges(tickets):
    with open(file_path, 'w') as file_1:  # when we open the file to write it will be cleared
        # https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python

        for ticket in tickets:
            ticket_id = ticket['ticket_id']
            event_id = ticket['event_id']
            username = ticket['username']
            timestamp = ticket['timestamp']
            priority = ticket['priority']
            # here we add to the file for each line a ticket in format "tick101, ev003, fred, 20230802, 0"
            file_1.write(f"{ticket_id}, {event_id}, {username}, {timestamp}, {priority}")
            if ticket != tickets[-1]:  # if this is not the last element of the list
                file_1.write("\n")  # we use \n to get to a new line each time we add a ticket
        file_1.close()  # and we close the file everytime we finish with it


# ---------------------------------------- Login Function ---------------------------------------- #
def login():                        # this function is for admin/user login
    admin_username = "admin"
    admin_password = "admin123123"  # we define the admin username and password
    attempt_count = 5

    while attempt_count > 0:             # to keep track of admin login attempt we use a while loop
        username = input("Username : ")

        if username == admin_username:         # we ask for the password if the username in an admin
            password = input("Password : ")

            if password == admin_password:      # username and password match the admin we log in with admin access
                print("Welcome! you have admin access.")
                return admin_username
            else:
                # when the attempt_count reaches 1 it will pass threw the admin username and password first
                # if it did not match it will be the last attempt
                if attempt_count == 1:
                    print("maximum attempts to login reach! try again later.")
                    return
                else:
                    attempt_count -= 1  # each time we have a wrong combination we subtract an attempt
                    print(f"Incorrect Username and/or Password.{attempt_count} attempt(s) remaining.")
        elif username == "":
            print("Please enter Username.")
        else:
            print(f"welcome {username} log in successful. ")
            return username  # if any username is entered beside admin the system will log in to the user account


# ---------------------------------------- Menu-choice functions ---------------------------------------- #


def adminMenu():           # a function to print admin Menu
    print("""
    1. Display Statistics
    2. Book a Ticket
    3. Display all Tickets
    4. Change Ticket’s Priority
    5. Disable Ticket
    6. Run Events
    7. Exit
    """)


def userMenu():           # a function to print user Menu
    print("""
    1. Book a Ticket
    2. Exit
    """)


def choiceInput():   # we make sure the admin/user inputs a positive integer as the choice
    while True:
        try:
            n = input("---> choose a number : ")
            num = int(n)
            return num

        except ValueError:
            print("this is not a number !")


# ---------------------------------------- Main function ---------------------------------------- #
def main():
    # we assign the login username (admin/user) to a variable to use it in main()
    user_type = login()
    # we assign 4 key for sorting the list the way we want
    key1, key2, key3, key4 = "timestamp", "event_id", "priority", "ticket_id"

    if user_type == "admin":

        adminMenu()
        choice = choiceInput()   # for each choice the right function will take place

        while choice != 7:

            if choice == 1:

                print(displayStatistics(ticketSort(tickets_list, key2, key1, key3, key4)))

            elif choice == 2:
                adminBookTicketInput(ticketSort(tickets_list, key4, key2, key3, key1))

            elif choice == 3:
                displayTickets(ticketSort(tickets_list, key1, key2, key3, key4))

            elif choice == 4:
                print(changePriority(ticketSort(tickets_list, key1, key2, key3, key4)))

            elif choice == 5:
                print(delTicket(tickets_list))

            elif choice == 6:
                RunEvents(tickets_list)

            else:
                print("this is an INVALID choice")

            adminMenu()            # after each choice the menu and choice functions will repeat until the choice is 7
            choice = choiceInput()

        save_changes = saveChangesInput()  # we ask the admin if he/she wants to save the changes
        if save_changes == "y":
            saveChanges(ticketSort(tickets_list, key4, key2, key3, key1))   # if yes it will be saved
            print("All changes have been saved.")
        else:
            print("NO changes are saved.")  # if not the program will exit with the proper message
        print("Exiting program...")
    # after 5 failed attempts login() will return "None" as username, so we make sure the program exit properly
    elif user_type is None:
        print("Exiting program...")

    else:

        userMenu()
        choice = choiceInput()    # if the username is not admin login as user which can only book a ticket or exit

        while choice != 2:
            if choice == 1:

                print(userBookTicket(ticketSort(tickets_list, key4, key2, key3, key1), user_type))
            else:
                print("this is an INVALID choice")

            userMenu()
            choice = choiceInput()
        # and upon exiting if there is a newly booked ticket it will be automatically saved to file
        saveChanges(ticketSort(tickets_list, key4, key2, key3, key1))
        print("Exiting program...")


main()
