class DoublyListNode:
    """Represents a single node in a doubly linked list."""

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    """Represents the doubly linked list structure managing head and tail references."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val: int) -> None:
        """Appends a new node with the given value to the end of the list."""
        new_node = DoublyListNode(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)

    # Forward traversal: 10 -> 20 -> 30 -> None
    print("Forward traversal:")
    curr = dll.head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

    # Backward traversal: 30 -> 20 -> 10 -> None
    print("Backward traversal:")
    curr = dll.tail
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.prev
    print("None")