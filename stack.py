class stack(object):
	def __init__(self):
		self.s = []

	def push(self, data):
		self.s.append(data)

	def display(self):
		print(self.s)

	def pop(self):
		self.s.pop()

s = stack()
s.push('A')
s.push('F')
s.push('V')
s.push('D')

s.display()

s.pop()

s.display()
