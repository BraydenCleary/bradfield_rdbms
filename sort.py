from iterator import Iterator

class Sort(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.input_rows = []
		self.current_row = 0
		self.sorted = False
		## Question
		# How should I be thinking about schemas?
		# I guess this will change once we start reading actual bytes
		# But even then, this node is gonna have to know what byte offsets to keep
		column_map = {"id": 0, "title": 1, "genres": 2}
		self.sort_by = column_map[self.args[0]]


	def next(self):
		if self.sorted:
			if self.current_row == len(self.input_rows):
				return None
			else:
				return_row = self.input_rows[self.current_row]
				self.current_row += 1
		else:
			next_from_child = self.child.next()
			while next_from_child:
				self.input_rows.append(next_from_child)
				next_from_child = self.child.next()
			if self.input_rows:
				self.input_rows = sorted(self.input_rows, key=lambda row: row[self.sort_by])
				self.sorted = True
				return_row = self.input_rows[self.current_row]
				self.current_row += 1

		return return_row