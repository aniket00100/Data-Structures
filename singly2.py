class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class singlylist:
	def __init__(self):
		self.head = None

	def display(self):
		llist = []
		curNode = self.head
		while curNode:
			llist.append(curNode.data)
			curNode = curNode.next
			
		print(llist)

	def append(self, data):
		newNode = node(data)

		if self.head is None:
			self.head = newNode
			return

		last_node = self.head
		while last_node.next != None:
			last_node = last_node.next
		last_node.next = newNode
	
	def prepend(self, value):
		newNode = node(value)
		newNode.next = self.head
		self.head = newNode


o = singlylist()

o.append(1)
o.append(2)
o.append(3)
o.append(4)
o.append(5)
o.append(6)

o.display()

#o.prepend(98)

o.display()
