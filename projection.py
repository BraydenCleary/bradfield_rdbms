from iterator import Iterator

class Projection(Iterator):
	def __init__(self, func, depth_from_root):
		super().__init__(func, depth_from_root)
		self.columns_to_keep = self.func()

	def next(self):
		child = self.children[0] if self.children else None

		if child:
			next_from_child = child.next()
			if next_from_child:
				return {col: next_from_child[col] for col in self.columns_to_keep}
