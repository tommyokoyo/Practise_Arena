class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def insert_position(self, data, position):
        node = LinkedListNode(data)
        if position == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError('list index out of range')
            current = current.next

        if current is None:
            raise IndexError('list index out of range')

        node.next = current.next
        current.next = node

    def insert_end(self, data):
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        previous = None
        if current is not None:
            if current.data == data:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.data == data:
                break
            previous = current
            current = current.next

        previous.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def print_reverse_list_recursive(self):
        def _inner_recursive(node):
            if node is None:
                return
            _inner_recursive(node.next)
            print(node.data, end=" -> ")
        _inner_recursive(self.head)

    def print_reverse_list_iterative(self):
        current = self.head
        temp_stack = []

        while current:
            temp_stack.append(current)
            current = current.next

        while temp_stack:
            node = temp_stack.pop()
            print(node.data, end=" -> ")

    def reverse_list(self):
        def _inner_reverse(current, previous):
            if current is None:
                return previous
            next_node = current.next
            current.next = previous
            return _inner_reverse(next_node, current)

        list_head = _inner_reverse(self.head, None)
        return list_head.data

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_end(1)
    llist.insert_end(2)
    llist.insert_end(3)
    llist.insert_start(0)

    print("Original List")
    llist.display()

    print("After Deleting node with data 2")
    llist.delete(2)
    llist.display()

    print("Searching for node with data 3: ", llist.search(3))
    print("Searching for node with data 2: ", llist.search(2))

    print("Inserting node with data 22 at position 2")
    llist.insert_position(22, 2)

    print("After Inserting node with data 22")
    llist.display()

    print("After Inserting node with data 22: ", llist.search(22))

    print("Printing the List in reverse using a recursive function")
    llist.print_reverse_list_recursive()

    print("\nPrinting the List in reverse using a iterative method")
    llist.print_reverse_list_recursive()

    print("\n reversed list")
    print(llist.reverse_list())