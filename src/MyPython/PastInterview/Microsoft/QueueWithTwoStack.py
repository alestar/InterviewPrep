
class QueueStack:
	def __init__(self):
		self.stack_enqueue = []
		self.stack_dequeue = []

	def __repr__(self):
		return f"{'stack_enqueue:' + str(self.stack_enqueue) + ' stack_dequeue: ' + str(self.stack_dequeue)}"

	def enqueue(self, val):
		self.stack_enqueue.append(val)
		return val

	def deque(self):
		if not self.stack_dequeue and not self.stack_enqueue:
			return None

		if self.stack_dequeue:
			return self.stack_dequeue.pop()

		else:
			while self.stack_enqueue:
				curr_val = self.stack_enqueue.pop()
				self.stack_dequeue.append(curr_val)

		return self.stack_dequeue.pop()


q = QueueStack()
print(q.deque())  # None, because there is no elements in the list
print("enqueuing: " + str(q.enqueue(1)))
print("enqueuing: " + str(q.enqueue(2)))
print("enqueuing: " + str(q.enqueue(3)))
print(q)
print("dequeuing: " + str(q.deque()))  # 1
print(q)
print("enqueuing: " + str(q.enqueue(4)))
print(q)
print("dequeuing : " + str(q.deque()))  # 2
print(q)
print("enqueuing: " + str(q.enqueue(5)))
print(q)
print("dequeuing : " + str(q.deque()))  # 3
print(q)
print("dequeuing : " + str(q.deque()))  # 4
print(q)
print("dequeuing : " + str(q.deque()))  # 5
print(q)
