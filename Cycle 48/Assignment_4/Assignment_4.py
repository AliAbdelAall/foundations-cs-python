# ----------- choice_1 ----------- #

# ------- classes ------- #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"New Node with value: {value}, added.")

    def displayNodes(self):
        if self.size == 0:
            print("\nLinked-List is empty!")
        else:
            current = self.head
            print("ll: Head-> ", end="")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def removeNodes(self):
        if self.size == 0:
            print("\nLinked-List is empty!")

        else:
            value = inputInteger()
            current = self.head
            previous = None
            count = 0

            while current:
                if current.data == value:
                    if previous:
                        previous.next = current.next
                        current.next = None
                        current = previous.next
                    else:
                        self.head = current.next
                        current = current.next
                    self.size -= 1
                    count += 1
                else:
                    previous = current
                    current = current.next

            if count:
                print(f"\nRemoved {count} Node(s) with value:", value)
            else:
                print("\nNode with value:", value, ", was not found.")


ll = LinkedList()


# ------- INPUTS ------- #

def inputInteger():
    num = input("Enter a number: ").strip()
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print("This is not a Number!")
            num = input("Enter a number again: ").strip()


# ----------- choice_2 ----------- #

def checkPalindrome():
    s = input("Enter a string: ")
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
        for j in range(len(s)):
            if s[j] == stack[-1]:
                stack.pop()
            else:
                return False
    return True


# ----------- choice_3 ----------- #

# ------- INPUTS ------- #

def inputGrade(grade):
    grade = input(f"Enter student's {grade} Grade(0-100):")
    while not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
        if not grade.isdigit():
            print("This is not a NUMERICAL Grade!")
        else:
            print("Grade must be between 0 and 100.")
        grade = input(f"Enter student's {grade} Grade(0-100) again:")
    return int(grade)


def inputAttitude():
    attitude = input("Good Attitude? y(YES)/n(NO): ")
    while attitude.lower() != "y" and attitude.lower() != "n":
        print("INVALID answer!")
        attitude = input("Good Attitude? y(YES)/n(NO): ")
    return True if attitude == "y" else False


class Student:
    def __init__(self):
        self.name = input("Enter Student Name: ")
        self.midterm_grade = inputGrade("Midterm")
        self.final_grade = inputGrade("Final")
        self.good_attitude = inputAttitude()
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, new_student):
        if not self.size:
            self.head = new_student
        else:
            current = self.head
            previous = None
            inserted = False

            while current and not inserted:
                if new_student.good_attitude and not current.good_attitude:
                    if not previous:
                        new_student.next = self.head
                        self.head = new_student
                    else:
                        previous.next = new_student
                        new_student.next = current
                    inserted = True

                elif new_student.good_attitude == current.good_attitude:
                    if new_student.final_grade > current.final_grade:
                        if not previous:
                            new_student.next = self.head
                            self.head = new_student
                        else:
                            previous.next = new_student
                            new_student.next = current
                        inserted = True
                    elif new_student.final_grade == current.final_grade:
                        if new_student.midterm_grade >= current.midterm_grade:
                            if not previous:
                                new_student.next = self.head
                                self.head = new_student
                            else:
                                previous.next = new_student
                                new_student.next = current
                            inserted = True

                previous = current
                current = current.next

            if not inserted:
                previous.next = new_student

        self.size += 1

        print(f"""
New student added:
Name: {new_student.name}
Midterm grade: {new_student.midterm_grade}/100
Final Grade: {new_student.final_grade}/100
Good attitude: {new_student.good_attitude}
""")

    def dequeue(self):
        if not self.size:
            print("There is no students to interview!")
        else:
            print(f"""
student ready for interview:
Name: {self.head.name}
Midterm grade: {self.head.midterm_grade}/100
Final Grade: {self.head.final_grade}/100
Good attitude: {self.head.good_attitude}
""")
            current = self.head
            self.head = self.head.next
            current.next = None
        self.size -= 1

    def displayQueue(self):
        if not self.size:
            print("Queue is empty!")
        else:
            current = self.head
            print("Head: ", end="")
            while current is not None:
                print(current.name, end=" -> ")
                current = current.next
            print("None")


queue = PriorityQueue()


# ----------- choice_5 ----------- #

# ------- INPUTS ------- #


class Graph:
    def __init__(self):
        self.graph = {}
        self.vertex_num = "0"

    def addVertex(self):
        self.graph[str(self.vertex_num)](LinkedList())
        self.vertex_num += 1

    def inputVertex(self, vertex, _):
        vertex = input(f"Enter {_} vertex: ")
        while not vertex.isdigit():
            print("vertex must be numeric!")
            vertex = input(f"Enter {_} vertex again: ")
        return vertex

    def checkVertices(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            print(f"Added an Edge between {v1} and {v2}.\n")

        elif v1 not in self.graph or v2 not in self.graph:
            if v1 not in self.graph:
                print(f"Vertex {v1} does not exist!\n")
            elif v2 not in self.graph:
                print(f"Vertex {v2} does not exist!\n")
            else:
                print(f"Both vertices {v1} and {v2} does not exist!\n")
        else:
            return [v1, v2]
    def addEdge(self, vertices):
        v1 = vertices[0]
        v2 = vertices[1]
        self.graph[v1].addNode(v2)
        self.graph[v2].addNode(v1)

    def removeVertex(self, vertex):
        if vertex not in self.graph:
            print(f"Vertex {vertex} does not exist")

        else:
            current = self.graph[vertex].head
            while current:
                v = current.data
                current_v = self.graph[v].head
                previous_v = None
                removed = False
                while current_v and not removed:
                    if current_v.data == vertex:
                        if not previous_v:
                            self.graph[v].head = self.graph[v].head.next
                            current_v.next = None

                        else:
                            previous_v.next = current_v.next
                            current_v.next = None

                        removed = True

                current = current.next


# ----------- MENUS ----------- #

def displayMainMenu():
    print("""
1. Singly Linked List
2. Check if Palindrome
3. Priority Queue
4. Evaluate an Infix Expression
5. Graph
6. Exit
""")


def displayLinkedListMenu():
    print("""
    a. Add Node
    b. Display Nodes
    c. Search for & Delete Node
    d. Return to main menu
    """)


def displayStudentMenu():
    print("""
    a. Add a student
    b. Interview a student
    c. Return to main menu
    """)


def displayGraphMenu():
    print("""
    a. Add vertex
    b. Add edge
    c. Remove vertex
    d. Remove edge
    e. Display vertices with a degree of X or more.
    f. Return to main menu
    """)


# ----------- CHOICE ----------- #

def inputIntChoice():
    choice = input("Enter a number as your choice: ").strip()
    while not choice.isdigit():
        print("this is not a number!")
        choice = input("Enter a number as your choice again: ").strip()
    return int(choice)


def inputStrChoice():
    choice = input("Enter a letter as your choice: ").strip()
    while len(choice) != 1:
        print("your choice must be one letter!")
        choice = input("Enter a letter as your choice again: ").strip()
    return choice


# ----------- User Greeting ----------- #

def greetUser():
    name = input("Enter your name: ").strip()
    if name == "":
        name = "Anonymous"
    print(f"Welcome, {name}!")


# ----------- MAIN ----------- #

def main():
    greetUser()
    displayMainMenu()
    choice = inputIntChoice()
    error_count = 0

    while choice != 6 and error_count != 4:
        if choice > 6 or choice < 1:
            print("this choice is INVALID!")
            print(f"you still have {4 - error_count} attempts")
            error_count += 1

        else:
            error_count = 0
            if choice == 1:
                displayLinkedListMenu()
                choice_ll = inputStrChoice()

                while choice_ll != "d":
                    if choice_ll == "a":
                        ll.addNode(inputInteger())
                    elif choice_ll == "b":
                        ll.displayNodes()
                    elif choice_ll == "c":
                        ll.removeNodes()
                    else:
                        print("this choice is INVALID!")

                    displayLinkedListMenu()
                    choice_ll = inputStrChoice()

            elif choice == 2:
                print(checkPalindrome())
            elif choice == 3:
                displayStudentMenu()
                choice_s = inputStrChoice()

                while choice_s != "c":
                    if choice_s == "a":
                        queue.enqueue(Student())
                    elif choice_s == "b":
                        queue.dequeue()
                    elif choice_s == "d":
                        queue.displayQueue()
                    else:
                        print("this choice is INVALID!")

                    displayStudentMenu()
                    choice_s = inputStrChoice()

            elif choice == 4:
                pass
            elif choice == 5:
                displayGraphMenu()
                choice_g = inputStrChoice()

                while choice_g != "f":
                    if choice_g == "a":
                        pass
                    elif choice_g == "b":
                        pass
                    elif choice_g == "c":
                        pass
                    elif choice_g == "d":
                        pass
                    elif choice_g == "e":
                        pass
                    else:
                        print("this choice is INVALID!")

                    displayGraphMenu()
                    choice_g = inputStrChoice()

        displayMainMenu()
        choice = inputIntChoice()


main()
