from iterator import Iterator

class Count(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)

	def next(self):
		self.count = 0

		next_from_child = self.child.next()
		while next_from_child:
			self.count += 1
			next_from_child = self.child.next()
		
		if self.count > 0:
			return self.count