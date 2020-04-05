from iterator import Iterator

class Distinct(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.last = None

	def next(self):
		next_from_child = self.child.next()
		while next_from_child:
			if next_from_child == self.last:
				next_from_child = self.child.next()
			else:
				self.last = next_from_child
				break
		return next_from_child
