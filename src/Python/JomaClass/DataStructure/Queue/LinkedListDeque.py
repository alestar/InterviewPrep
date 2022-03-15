from DoubleLinkedListNode import DoubleLinkedListNode


class LinkedListDequeue:
    def __init__(self, front_node=None, back_node=None):
        self.front = front_node
        self.rear = back_node
        self.size = 0

    def __iter__(self):
        current = self.front
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
        return self.size == 0  # return self.front not None

    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty queue")
        return self.front.value

    def rear_enqueue(self, value):
        new_node = DoubleLinkedListNode(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
        self.rear = new_node
        self.size += 1

    def rear_dequeue(self):
        if self.is_empty():
            raise Exception("Popping from an empty queue")
        else:
            value = self.rear.value
            self.rear = self.rear.prev
            self.rear.next = None
            self.size -= 1
        return value

    def front_dequeue(self):
        if self.is_empty():
            raise Exception("Popping from an empty queue")
        else:
            value = self.front.value
            self.front = self.front.next
            self.size -= 1
            return value

    def front_enqueue(self, value):
        new_node = DoubleLinkedListNode(value)
        if self.is_empty():
            self.front = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

# Driver Code
if __name__ == '__main__':
    q = LinkedListDequeue()
    q.rear_enqueue(10)
    print(q)
    q.front_enqueue(20)
    print(q)
    q.rear_enqueue(30)
    print(q)
    q.front_enqueue(40)
    print(q)
    q.rear_enqueue(50)
    print(q)
    q.front_dequeue()
    print(q)
    q.front_dequeue()
    print(q)
    q.rear_dequeue()
    print(q)
    q.rear_dequeue()
    print(q)
