from iterator import Iterator

class Selection(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.column = self.args[0]
		self.operator = self.args[1]
		self.value = self.args[2]

		## Question
		# How should I be thinking about schemas?
		# I guess this will change once we start reading actual bytes
		# But even then, this node is gonna have to know what byte offsets to keep
		self.column_map = {"id": 0, "title": 1, "genres": 2}

	def next(self):
		next_from_child = self.child.next()
		while next_from_child:
			if self.__row_is_match(next_from_child):
				break
			else:
				next_from_child = self.child.next()

		return next_from_child

	def __row_is_match(self, row):
		if self.operator == "EQUALS":
			return row[self.column_map[self.column]] == self.value
		else:
			raise(f"{self.operator} selection operator not yet implemented")