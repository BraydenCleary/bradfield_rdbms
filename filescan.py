import csv
from iterator import Iterator

class Filescan(Iterator):
	def __init__(self, func, depth_from_root):
		super().__init__(func, depth_from_root)
		self.table_name = self.func()
		self.rows = self.__read_table()
		self.current_row = 0
		self.num_rows = len(self.rows)
		self.schema = []

	def __read_table(self):
		rows = []
		with open('./ml-20m/' + self.table_name + '.csv', newline='') as f:
			reader = csv.reader(f)
			# skip header, I'm sure there's a more elegant way
			

			for idx, row in enumerate(reader):
				if idx == 0:
					self.schema = row
					continue
				rows.append(dict(zip(self.schema, row)))
		return rows

	def next(self):
		if self.current_row == self.num_rows:
			return None
		else:
			row = self.rows[self.current_row]
			self.current_row += 1

			return row
