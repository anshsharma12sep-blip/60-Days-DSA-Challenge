class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Print Linked List
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse Linked List (Iterative)
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   # Store next node
            current.next = prev       # Reverse pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        self.head = prev


# -------------------- Main Function --------------------

if __name__ == "__main__":
    ll = LinkedList()

    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original Linked List:")
    ll.print_list()

    ll.reverse()

    print("Reversed Linked List:")
    ll.print_list()