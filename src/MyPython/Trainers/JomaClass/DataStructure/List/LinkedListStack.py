from JomaClass.DataStructure.List.LinkedListNode import LinkedListNode


class LinkedListStack:
    def __init__(self, head_node=None):
        self.head = head_node
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    # Get the current size of the stack
    def size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.value

    def push(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        else:
            val = self.head.value
            self.head = self.head.next
            self.size -= 1
            return val


# Driver Code
if __name__ == "__main__":
    stack = LinkedListStack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")