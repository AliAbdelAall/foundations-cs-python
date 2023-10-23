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

users_indices = {}
for user_index in range(len(users)):
    users_indices[users[user_index]] = user_index

print(users_indices)


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
            return self.queue.pop()


# ______________________________ Node class _____________________________ #
class Node:
    def __init__(self, vertex):
        self.data = vertex
        self.next = None


# __________________________ linked list class __________________________ #
class UserAccount:
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

    def friendList(self, user):
        if user not in users_indices:
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
        if data not in users_indices:
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


# __________________________ Graph class __________________________ #
class Graph:
    def __init__(self, users_list):
        self.graph = []
        for i in range(len(users_list)):
            self.graph.append(UserAccount())

    def addUser(self, vertex):
        if vertex in users_indices:
            print("this user already exist")
        else:
            users.append(vertex)
            users_indices[vertex] = len(users) - 1
            self.graph.append(UserAccount())

    def removeUser(self, vertex):
        if vertex not in users:
            print("this user does not exist")
            return

        else:
            del_user = self.graph[users_indices[vertex]]
            del_user_from_friends = del_user.friendList(vertex)
            self.graph.remove(del_user)
            users.pop(users_indices[vertex])
            users_indices.pop(vertex)

            if del_user.isEmpty():
                return
            else:
                for del_friend in del_user_from_friends:
                    self.graph[users_indices[del_friend]].removeFriend(vertex)
            print(f"User {vertex} successfully removed.")

    def friendRequest(self):
        user1 = usernameInput()
        user2 = usernameInput()

        if (user1 or user2) not in users_indices:
            print("user(s) does not exist.")
            return
        elif user1 in self.graph[users_indices[user1]].friendList(user2):
            print(f"{user1} and {user2} are already friends")
        else:
            self.graph[users_indices[user1]].addFriend(user2)
            print(users_indices[user1])
            print(user1)

            self.graph[users_indices[user2]].addFriend(user1)
            print(users_indices[user2])
            print(user2)

        print(f"Connection added between {user1} and {user2}.")

    def removeFriends(self):
        user1 = usernameInput()
        user2 = usernameInput()

        if user1 or user2 not in users:
            print("user(s) does not exist.")
            return

        else:
            self.graph[users_indices[user1]].removeFriend(user2)
            self.graph[users_indices[user2]].removeFriend(user1)

    def displayFriendList(self, vertex):
        if vertex not in users:
            print("this user does not exist")
            return
        else:
            self.graph[users_indices[vertex]].displayFriends()
            return

    def displayAllUsers(self, starting_vertex):
        visited = [False] * len(self.graph)
        queue = Queue()
        queue.enqueue(users_indices[starting_vertex])

        while False in visited:
            if queue.isEmpty():
                for i in range(len(visited)):
                    if not visited[i]:
                        queue.enqueue(i)
            else:
                v = queue.dequeue()
                if not visited[v]:
                    visited[v] = True
                    print(users[v])
                    user = self.graph[v]
                    for friend in user.friendList(users[v]):
                        v_i = users_indices[friend]
                        if not visited[v_i]:
                            queue.enqueue(v_i)





    """def displayAllUsers(self, starting_vertex):
    visited = [False] * len(self.graph)
    queue = Queue()
    queue.enqueue(users_indices[starting_vertex])
    
    while any(not visited[v] for v in range(len(self.graph))):
        v = queue.dequeue()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")
            
            for w in range(len(self.graph[v])):
                if self.graph[v][w] == 1 and not visited[w]:
                    queue.enqueue(w)"""


platform = Graph(users)


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
            platform.friendRequest()

        elif choice == 4:
            print("Not ready yet")

        elif choice == 5:
            platform.displayFriendList(usernameInput())

        elif choice == 6:
            platform.displayAllUsers(users[0])

        else:
            print("this is an INVALID choice")

        Menu()  # after each choice the menu and choice functions will repeat until the choice is 7
        choice = choiceInput()

    print("Exiting....")


main()
