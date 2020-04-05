class Iterator:
	def __init__(self, child, args):
		self.child = child
		self.args = args

	def next(self):
		# implement me in subclass
		pass

	def close(self):
		# implement me in subclass
		pass
