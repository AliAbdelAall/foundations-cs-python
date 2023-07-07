# Q_1

print("-------------- Question 1 --------------")

def factorialClac(num):
    factorial = 1
    if num < 0:
        return None
    else:
        for i in range(1, num + 1):
            factorial *= i
        return factorial


while True:
    try:
        n = input("Enter a number : ")
        num = int(n)
        result = factorialClac(num)
        if result is None:
            print("factorial does not exist for negative numbers.")
        else:
            print(result)
            break
    except ValueError:
        print("this is not a number")


# # Q_2

print("-------------- Question 2 --------------")

def divisorsCalc():

    try:
        n = input("Enter a number : ")
        num = int(n)
        div_list = []
        if num < 0:
            print("this number is negative.")
            divisorsCalc()
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    div_list.append(i)
            print(div_list)
    except ValueError:
        print("This is not a number.")
        divisorsCalc()


divisorsCalc()


# #Q_3

print("-------------- Question 3 --------------")


def reverseString(s):
    reverse = ""
    for i in range(len(s) - 1, -1, -1):
        reverse += s[i]
    return reverse


s = input("type here : ")
print(reverseString(s))


#Q_4

print("-------------- Question 4 --------------")

def evenNums():
    try:
        user_input = list(map(int, input("enter a list of numbers separated by spaces : ").split()))
        even_list = []
        for i in user_input:
            if i % 2 == 0:
                even_list.append(i)
        print(even_list)
    except ValueError:
        print("this list elements must be all numbers")
        evenNums()


evenNums()


 #Q_5

print("-------------- Question 5 --------------")

def passwordChecker(s):
    upper = False
    lower = False
    special = False
    digit = False
    for i in s:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i == "#" or i == "?" or i == "!" or i == "$":
            special = True
        elif i.isdigit():
            digit = True
    if len(s) >= 8 and upper and lower and special and digit:
        result = "Strong password"
    else:
        result = "Weak password"
    return result


s = input("please enter you password : ")
print(passwordChecker(s))


#Q_6 (BONUS)

print("-------------- Question 6 (Bonus) --------------")
def ipv4Checker(ipv4):
    for item in ipv4:
        if (int(item[0]) == 0 and len(item) != 1) or len(ipv4) != 4 or int(item) < 0 or int(item) > 255 or item == '':
            return False
    return True


while True:
    try:
        ip = input("enter your IPv4 : ").split(".")
        result = ipv4Checker(ip)
        if result:
            print("your IPv4 is VALID.")
            break
        else:
            print("your IPv4 is INVALID. Please try AGAIN.")
    except ValueError:
        print("this is not an IPv4! Please try AGAIN.")
