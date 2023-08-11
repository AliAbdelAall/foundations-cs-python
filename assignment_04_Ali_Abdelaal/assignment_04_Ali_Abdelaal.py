users = [
    "John",
    "Emma",
    "Michael",
    "Olivia",
    "William",
    "Ava",
    "James",
    "Sophia",
    "David",
    "Isabella",
]

users_indicies = {}
for i in range(len(users)):
    users_indicies[users[i]] = i

print(users_indicies)


# ____________________________ queue class ____________________________ #
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        else:
            self.queue.pop()


# ______________________________ Node class _____________________________ #
class Node:
    def __init__(self, vertex):
        self.data = vertex
        self.next = None


# __________________________ linked list class __________________________ #
class userAccount:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def displayFriends(self):
        if self.isEmpty():
            print("the user have no friends yet!")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

    def friendList(self, data):
        if data not in users_indicies:
            print("this user does not exist.")
            return
        else:
            friend_list = []
            current = self.head
            while current is not None:
                friend_list.append(current.data)
                current = current.next
            return friend_list

    def addFriend(self, data):
        node_to_add = Node(data)
        if self.isEmpty():
            self.head = node_to_add

        else:
            node_to_add.next = self.head
            self.head = node_to_add

    def removeFriend(self, data):
        if data not in users_indicies:
            print("User does not exist.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next

        print("Friend not found.")


class graph:
    def __init__(self):
        self.graph = []

    def addUsersList(self, userlist):
        for user in users:
            self.graph.append(userAccount())

    def addUser(self, vertex):
        if vertex in users_indicies:
            print("this user already exist")
        else:
            users.append(vertex)
            users_indicies[vertex] = len(users) - 1
            self.graph.append(userAccount(vertex))

    def removeUser(self, vertex):
        if vertex not in users:
            print("this user does not exist")
            return

        else:
            del_user = self.graph[users_indicies[vertex]]
            del_user_from_friends = del_user.friendList(vertex)
            self.graph.remove(del_user)
            users.pop(users_indicies[vertex])
            users_indicies.pop(vertex)

            if del_user.isEmpty():
                return
            else:
                for del_friend in del_user_from_friends:
                    self.graph[users_indicies[del_friend]].removeFriend(vertex)
            print(f"User {vertex} successfully removed.")

    def friendRequest(self):
        user1 = input("Enter first username : ")
        user2 = input("Enter second username : ")

        if user1 or user2 not in users:
            print("user(s) does not exist.")
            return

        else:
            self.graph[users_indicies[user1]].addFriend(user2)
            self.graph[users_indicies[user2]].addFriend(user1)

        print(f"Connection added between {user1} and {user2}.")

    def removeFriends(self):
        user1 = input("Enter first username : ")
        user2 = input("Enter second username : ")

        if user1 or user2 not in users:
            print("user(s) does not exist.")
            return

        else:
            self.graph[users_indicies[user1]].removeFriend(user2)
            self.graph[users_indicies[user2]].removeFriend(user1)

    def DisplayFriendList(self, vertex):
        if vertex not in users:
            print("this user does not exist")
            return
        else:
            self.graph[users_indicies[vertex]].displayFriends(vertex)
            return

    def displayAllUsers(self, starting_vertex):
        visited = [False] * len(self.graph)
        queue = Queue()
        queue.enqueue(users_indicies[starting_vertex])

        while False in visited:
            if queue.isEmpty():
                for i in range(len(visited)):
                    if not visited[i]:
                        queue.enqueue(i)

            v = queue.dequeue()
            if not visited[v]:
                visited[v] = True
                print(v, end=" ")

                for w in range(len(self.graph[v])):
                    if self.graph[v][w] == 1 and not visited[w]:
                        queue.enqueue(w)


platform = graph().addUsersList()


def usernameInput():
    username = input("Enter username : ")
    return username


def choiceInput():  # we make sure the admin/user inputs a positive integer as the choice
    while True:
        try:
            n = input("---> choose a number : ")
            num = int(n)
            return num

        except ValueError:
            print("this is not a number !")


def Menu():  # a function to print admin Menu
    print(
        """
    1. Add a user to the platform. 
    2. Remove a user from the platform. 
    3. Send a friend request to another user. 
    4. Remove a friend from your list. 
    5. View your list of friends. 
    6. View the list of users on the platform. 
    7. Exit 

    """
    )


def main():
    Menu()
    choice = choiceInput()  # for each choice the right function will take place

    while choice != 7:
        if choice == 1:
            platform.addUser(usernameInput())

        elif choice == 2:
            platform.removeUser(usernameInput())

        elif choice == 3:
            platform.friendRequest

        elif choice == 4:
            print("Not ready yet")

        elif choice == 5:
            print("not ready yet")

        elif choice == 6:
            platform.displayAllUsers(users_indicies[users[0]])

        else:
            print("this is an INVALID choice")

        Menu()  # after each choice the menu and choice functions will repeat until the choice is 7
        choice = choiceInput()

    print("Exiting....")


main()
