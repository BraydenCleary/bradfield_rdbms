class MockIterator:
    def __init__(self, rows):
        self.rows = rows
        self.row_counter = 0

    def next(self):
        if self.row_counter < len(self.rows):
            row = self.rows[self.row_counter]
            self.row_counter += 1
            return row
