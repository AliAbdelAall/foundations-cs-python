def tupleLenInput(): #handling user input to input only pisitive intrgers
    while True:
        # try and except will try to input the code if there was an error the code will not terminate combining it with the while True loop
        # the programm will ask for the input agai and agai till it meets the condition required to terminate the function after returning
        #the right value we want
        try:
            n = input("enter the length of the tuples : ")
            tuple_len = int(n)
            if tuple_len < 0:
                print("This is a negative number")
            else:
                return tuple_len
        except ValueError:
            print("this is not a number.")


def tupleSumInput(tuple_len):
    while True:
        try:
            tuple_input = input("enter the numbers you want separated by spaces : ")
            tuple_input = tuple(map(int, tuple_input.split()))
            if tuple_len == len(tuple_input):
                return tuple_input
            else:
                print("you entered", len(tuple_input), "numbers, they must be", tuple_len, "numbers !")
        except ValueError:
            print("all elements must be numbers !")


def tupleSum(len, tuple1, tuple2):
    lst_sum = []
    for i in range(len):
        lst_sum.append(tuple1[i] + tuple2[i])
    tuples_sum = tuple(lst_sum)
    return tuples_sum


def menu():
    print("1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit")


def choiceInput():
    while True:
        try:
            n = input("Enter a choice : ")
            choice = int(n)
            if choice >= 0:
                return choice
            else:
                print("this is a negative number !")
        except ValueError:
            print("This is not a number!")


def ExportJson(data, indent=0):
    if isinstance(data, dict):
        json_str = "{\n"
        for key, value in data.items():
            json_str += f'{" " * (indent + 4)} "{key}" : {ExportJson(value,indent + 4)},\n'
            json_str = json_str.rstrip(',\n') + '\n' + f'{" " * indent}}}'
        return json_str
    elif isinstance(data, list):
        json_str = '[\n'
        for item in data:
            json_str += f'{" " * (indent + 4)}{ExportJson(item, indent + 4)},\n'
            json_str = json_str.rstrip(',\n') + '/n' + f'{" " * indent}]'
        return json_str
    elif isinstance(data, str):
        escaped_str = data .replace('"', '//"').replace('\n', '\\n').replace('\t', '\\t')
        return f"{escaped_str}"
    elif isinstance(data, bool):
        if data:
            return "true"
        return "false"
    else:
        return str(data)


def writeJsonFile(data, filename):
    try:
        with open(filename, 'w') as file:
            json_file = ExportJson(data, indent=0)
            file.write(json_file)
            print(f"you have successfully converted data to a JSON as {filename}!")
    except ValueError as e :
        print(f"Error : {e}")




def main():
    menu()
    choice = choiceInput()
    while choice != 4:
        if choice == 1:
            tuple_len_input = tupleLenInput()
            print("the sum of the tuples you entered is", tupleSum(tuple_len_input, tupleSumInput(tuple_len_input), tupleSumInput(tuple_len_input)))
        elif choice == 2:
            data = {
                "name": "John Doe",
                "age": 30,
                "email": "john.doe@example.com",
                "address": {
                    "street": "123 Main Street",
                    "city": "New York",
                    "zipcode": "10001",
                    "country": "United States"
                },
                "hobbies": ["Reading", "Gardening", "Cooking"],
                "is_student": False
            }

            filename = "data.json"
            writeJsonFile(data, filename)

        elif choice == 3:
            print("not ready yet !!")
        else:
            print("this is an INVALID choice !")

        menu()
        choice = choiceInput()

    print("Thank YOU !!")


main()
