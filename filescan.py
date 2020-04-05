import csv
from iterator import Iterator

class Filescan(Iterator):
	def __init__(self, child, args):
		super().__init__(child, args)
		self.table_name = self.args[0]
		self.rows = self.__read_table()
		self.current_row = 0
		self.num_rows = len(self.rows)

	def __read_table(self):
		rows = []
		with open('../ml-20m/' + self.table_name + '.csv', newline='') as f:
			reader = csv.reader(f)
			# skip header, I'm sure there's a more elegant way
			next(reader)

			for row in reader:
				rows.append(row)
		return rows

	def next(self):
		if self.current_row == self.num_rows:
			return None
		else:
			row = self.rows[self.current_row]
			self.current_row += 1

			return row
