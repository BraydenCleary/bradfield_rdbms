from iterator import Iterator

class Limit(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.row_limit = int(self.args[0])
		self.current_row = 0

	def next(self):
		if self.current_row == self.row_limit:
			return None
		else:
			self.current_row += 1
			return self.child.next()
