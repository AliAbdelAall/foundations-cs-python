from datetime import date

today = str(date.today()).replace("-", "")

# ---------------------------------------- File Opening ---------------------------------------- #

file_path = "E:/PyCharm/PyCharm Community Edition 2023.1/Coding/foundations-cs-python/mid-term_2023_Ali_Abdelaal/" \
            "tickets.txt"
# https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy
with open(file_path, 'r+') as file:
    lines = file.readlines()

tickets_list = []

for line in lines:
    line_list = line.split(", ")
    tickets_list.append({"ticket_id": line_list[0], "event_id": line_list[1], "username": line_list[2],
                         "timestamp": line_list[3], "priority": int(line_list[4])})

file.close()


# ---------------------------------------- tickets Sort ---------------------------------------- #
def ticketSort(tickets, key1, key2, key3, key4):
    if len(tickets) <= 1:
        return tickets  # when we have 1 element in the list it will be automatically sorted, so we return it

    middle = len(tickets) // 2  # we divide the list into 2 half's

    left_half = ticketSort(tickets[:middle], key1, key2, key3, key4)  # we use recursion to divide the list again and
    # again until we have 1 element in the list
    right_half = ticketSort(tickets[middle:], key1, key2, key3, key4)  # using the split lists as arguments

    return merge(left_half, right_half, key1, key2, key3, key4)  # we use another function for merging to sort the
    # divided  lists


def merge(left, right, key1, key2, key3, key4):
    merged_list = []  # we assign an empty list
    left_index = 0  # we assign 2 indices 1 for each half list, and we set it to 0, so we can always access the firs
    right_index = 0  # item in the list

    while left_index < len(left) and right_index < len(
            right):  # here we use a while loop to compare the 2 lists there is elements in 1 of the lists

        if key1 == "ticket_id":

            if left[left_index][key1] < right[right_index][key1]:
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1

        elif left[left_index][key1] < right[right_index][key1]:
            merged_list.append(left[left_index])
            left_index += 1  # for each time we append a number from the left list we move to the next element by
            # increasing the index by 1

        elif left[left_index][key1] == right[right_index][key1]:

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

    merged_list.extend(left[left_index:])  # if by any chance the list still have an element inside it that we did not
    # append to the list
    merged_list.extend(right[right_index:])  # we append it here since the item left is the bigger one

    return merged_list


# ---------------- ticket ID Input ---------------- #
def ticketIdInput():
    while True:
        try:
            ticket_id = input("Enter ticket ID : ")
            ticket_num = ticket_id[4:]

            if not ticket_id.startswith("tick") or not int(ticket_num) or len(ticket_num) != 3:
                raise ValueError

            return ticket_id

        except ValueError:
            print("Invalid Ticket-ID. ticket-ID should be in 'tickXXX' format, XXX as 3-digit number.")


# ---------------- Event ID Input ---------------- #
def eventIdInput():
    while True:
        try:
            event_id = input("Enter event ID : ")
            event_num = event_id[2:]

            if not event_id.startswith("ev") or not int(event_num) or len(event_num) != 3:
                raise ValueError

            return event_id

        except ValueError:
            print("Invalid Event-ID. Event-ID should be in 'evXXX' format, XXX as 3-digit number.")


# ---------------- Priority Input ---------------- #
def intPriorityInput():
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
def timestampInput():
    while True:
        try:
            len_date = 8
            timestamp = input("Enter event date as (YYYYMMDD) : ")
            if not timestamp.isdigit():
                raise ValueError

            if len(timestamp) != len_date:
                print("enter the full/correct date format plz!")

            elif len(timestamp) == 8:
                year = int(timestamp[:4])
                month = int(timestamp[4:6])
                day = int(timestamp[6:])

                if year < 2023:
                    print("you cant book a ticket in the past.")
                elif year > 2070:
                    print("booking date limit exceeded!")
                elif month < 0 or month > 12:
                    print("there is only 12 months in a year!")
                elif month in [4, 6, 9, 11] and (day < 0 or day > 30):
                    print("in this month day must be between 1--30.")
                elif month == 2:

                    if year % 2 == 0 and (day < 0 or day > 29):
                        print("in this year february is 29 days.")
                    elif year % 2 != 0 and (day < 0 or day > 28):
                        print("in this year february is 28 days.")
                    else:
                        return timestamp
                elif day < 0 or day > 31:
                    print("in this month day must be between 1--31.")
                else:
                    return timestamp

        except ValueError:
            print("this is not a date.")


# ---------------------------------------- 1. Display statistics ---------------------------------------- #
def displayStatistics(tickets):
    event_tickets = {}

    for ticket in tickets:
        event_id = ticket["event_id"]

        if event_id in event_tickets:
            event_tickets[event_id] += 1
        else:
            event_tickets[event_id] = 1

    highest_value = 0
    result = ""
    highest_events = []
    for key, value in event_tickets.items():
        print(key, ":", value, "tickets")

        if highest_value < value:
            highest_value = value
            highest_events = []
            highest_events.append(key)
            result = f"{key} has the most tickets, {highest_value} tickets."
        elif highest_value == value:
            highest_events.append(key)

    if len(highest_events) == 1 and len(highest_events) != 0:
        return result
    elif len(highest_events) > 1:
        result = ", ".join(highest_events)
        return f"{result} have the most tickets, {highest_value} tickets each."


# ---------------------------------------- 2. book a ticket ---------------------------------------- #
def adminBookTicketInput(tickets):
    username = input("Enter username : ")
    event_id = eventIdInput()
    timestamp = timestampInput()
    priority = intPriorityInput()
    last_ticket = int(tickets[-1]["ticket_id"][4:])
    new_ticket = "tick" + str(last_ticket + 1)

    if last_ticket >= 999:
        print("maximum ticket counter reached")

    else:

        tickets_list.append(
            {"ticket_id": new_ticket,
             "event_id": event_id,
             "username": username,
             "timestamp": timestamp,
             "priority": priority})

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
    n = 1
    if len(tickets) > 0:

        for i in range(len(tickets) - 1):
            if tickets[i]["timestamp"] >= '20230801':
                ticket_id = tickets[i]['ticket_id']
                event_id = tickets[i]['event_id']
                username = tickets[i]['username']
                timestamp = tickets[i]['timestamp']
                priority = tickets[i]['priority']

                print(
                    f"{n}_{ticket_id}, {timestamp}, {event_id}, {username}, {priority}")
                n += 1
        return "This are the tickets in queue "

    else:
        return "No tickets found."


# ---------------------------------------- 4. Change Priority ---------------------------------------- #
def changePriority(tickets):
    ticket_id = ticketIdInput()

    for i in range(len(tickets) - 1):

        if tickets[i]["ticket_id"] == ticket_id:
            print(f"""
Ticket found: 

    Ticket ID  : {tickets[i]["ticket_id"]}
    Event ID   : {tickets[i]["event_id"]}
    Username   : {tickets[i]["username"]}
    Event Date : {tickets[i]["timestamp"]}
    Priority   : {tickets[i]["priority"]}
            """)

            priority = intPriorityInput()
            old_priority = tickets[i]["priority"]
            tickets[i]["priority"] = priority
            return f"priority for this ticket has changed from '{old_priority}' to '{priority}'"

    return f"{ticket_id} does not exist."


# ---------------------------------------- 5. del Ticket ---------------------------------------- #
def delTicket(tickets):
    ticket_id = ticketIdInput()

    for i in range(len(tickets)):
        if tickets[i]["ticket_id"] == ticket_id:
            tickets.pop(i)
            return f"Ticket _{ticket_id}_ has been removed"

    return f'{ticket_id} does not exist.'


# ---------------------------------------- 6. Run Events ---------------------------------------- #
def RunEvents(tickets):
    today_event_index = []
    ticket_count = 1

    print("today's event tickets:")

    for i in range(len(tickets) - 1):

        if tickets[i]["timestamp"] == "20230801":
            today_event_index.insert(0, i)
            print(f"""
  {ticket_count}-Ticket ID  : {tickets[i]["ticket_id"]}
    Event ID   : {tickets[i]["event_id"]}
    Username   : {tickets[i]["username"]}
    Event Date : {tickets[i]["timestamp"]}
    Priority   : {tickets[i]["priority"]}""")
            ticket_count += 1

    if len(today_event_index) != 0:
        for index in today_event_index:
            tickets.pop(index)

    else:
        print("No Tickets Found.")


# ---------------------------------------- 1. Book a Ticket (user) ---------------------------------------- #
def userBookTicket(tickets, user_type):
    username = user_type
    event_id = eventIdInput()
    timestamp = timestampInput()
    priority = 0

    last_ticket = int(tickets[-1]["ticket_id"][4:])
    new_ticket = "tick" + str(last_ticket + 1)

    tickets_list.append({"ticket_id": new_ticket, "event_id": event_id, "username": username, "timestamp": timestamp,
                         "priority": priority})

    print(f"""
Ticket successfully booked.
    here's your ticket : 

    Ticket ID  : {new_ticket}
    Event ID   : {event_id}
    Username   : {username}
    Event Date : {timestamp}
    Priority   : {priority}
""")


# ---------------------------------------- Save to file ---------------------------------------- #
def saveChangesInput():
    while True:
        answer = input("Do you want to save the changes you made? y(yes)/n(no) : ")
        if answer != "y" and answer != "n":
            print("Pleas answer with y/(yes) and n/(no) : ")
        else:
            return answer


def saveChanges(tickets):
    with open(file_path,
              'w') as file_1:  # https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python

        for ticket in tickets:
            ticket_id = ticket['ticket_id']
            event_id = ticket['event_id']
            username = ticket['username']
            timestamp = ticket['timestamp']
            priority = ticket['priority']

            file_1.write(f"{ticket_id}, {event_id}, {username}, {timestamp}, {priority}")
            file_1.write("\n")
        file_1.close()


# ---------------------------------------- Login Function ---------------------------------------- #
def login():
    admin_username = "admin"
    admin_password = "admin123123"
    attempt_count = 5

    while attempt_count > 0:
        username = input("Username : ")

        if username == admin_username:
            password = input("Password : ")

            if password == admin_password:
                print("Welcome! you have admin access.")
                return admin_username
            else:

                if attempt_count == 1:
                    print("maximum attempts to login reach! try again later.")
                    return
                else:
                    attempt_count -= 1
                    print(f"Incorrect Username and/or Password.{attempt_count} attempt(s) remaining.")

        else:
            print(f"welcome {username} log in successful. ")
            return username


# ---------------------------------------- Menu-choice functions ---------------------------------------- #


def adminMenu():
    print("""
    1. Display Statistics
    2. Book a Ticket
    3. Display all Tickets
    4. Change Ticket’s Priority
    5. Disable Ticket
    6. Run Events
    7. Exit
    """)


def userMenu():
    print("""
    1. Book a Ticket
    2. Exit
    """)


def choiceInput():
    while True:
        try:
            n = input("---> choose a number : ")
            num = int(n)
            return num

        except ValueError:
            print("this is not a number !")


# ---------------------------------------- Main function ---------------------------------------- #
def Main():
    user_type = login()
    key1, key2, key3, key4 = "timestamp", "event_id", "priority", "ticket_id"

    if user_type == "admin":

        adminMenu()
        choice = choiceInput()

        while choice != 7:

            if choice == 1:

                print(displayStatistics(ticketSort(tickets_list, key2, key1, key3, key4)))

            elif choice == 2:
                adminBookTicketInput(ticketSort(tickets_list, key4, key2, key3, key1))

            elif choice == 3:
                print(displayTickets(ticketSort(tickets_list, key1, key2, key3, key4)))

            elif choice == 4:
                print(changePriority(ticketSort(tickets_list, key1, key2, key3, key4)))

            elif choice == 5:
                print(delTicket(tickets_list))

            elif choice == 6:
                RunEvents(tickets_list)

            else:
                print("this is an INVALID choice")

            adminMenu()
            choice = choiceInput()

        save_changes = saveChangesInput()
        if save_changes == "y":
            saveChanges(ticketSort(tickets_list, key4, key2, key3, key1))
            print("All changes have been saved.")
        else:
            print("NO changes are saved.")
        print("Exiting program...")

    elif user_type is None:
        print("Exiting program...")

    else:

        userMenu()
        choice = choiceInput()

        while choice != 2:
            if choice == 1:

                print(userBookTicket(ticketSort(tickets_list, key4, key2, key3, key1), user_type))
            else:
                print("this is an INVALID choice")

            userMenu()
            choice = choiceInput()

        saveChanges(ticketSort(tickets_list, key4, key2, key3, key1))
        print("Exiting program...")


Main()
