# LINKED LIST - ADDING

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
tail = None

print("=== LINKED LIST ADDING ===")

letters = ["M", "E", "S", "I", "N", "A"]

for letter in letters:
    new_node = Node(letter)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

print("Adding completed.\n")

# LINKED LIST - REMOVING

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
tail = None

letters = ["M", "E", "S", "I", "N", "A"]
for letter in letters:
    new_node = Node(letter)

for letter in letters:
    new_node = Node(letter)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


print("=== LINKED LIST REMOVING ===")

while head is not None:
    print("Removed:", head.data)
    head = head.next

    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

print("Linked List is empty. Stop.")