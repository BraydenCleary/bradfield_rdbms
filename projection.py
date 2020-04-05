from iterator import Iterator

class Projection(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.columns_to_keep = self.args
		## Question
		# How should I be thinking about schemas?
		# I guess this will change once we start reading actual bytes
		# But even then, this node is gonna have to know what byte offsets to keep
		column_map = {"userId": 0, "movieId": 1, "rating": 2, "timestamp": 3}
		self.indices_to_keep = [column_map[col] for col in self.columns_to_keep]

	def next(self):
		next_from_child = self.child.next()
		if next_from_child:
			return [next_from_child[i] for i in self.indices_to_keep]
		else:
			return None
