from iterator import Iterator

class Selection(Iterator):
	def __init__(self, func, depth_from_root):
		super().__init__(func, depth_from_root)

	def next(self):
		child = self.children[0] if self.children else None
		
		if child:
			next_from_child = child.next()
			while next_from_child:
				if self.func(next_from_child):
					break
				else:
					next_from_child = child.next()

			return next_from_child
