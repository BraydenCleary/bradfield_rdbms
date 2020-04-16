import csv
from iterator import Iterator

class Filescan(Iterator):
    def __init__(self, func, depth_from_root=0):
        super().__init__(func, depth_from_root)
        self.__table_name = self.func()
        self.__rows = self.__read_table()
        self.__current_row = 0
        self.__num_rows = len(self.rows)
        self.__schema = []

    def __read_table(self):
        rows = []
        with open('./ml-20m/' + self.__table_name + '.csv', newline='') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    self.__schema = row
                    continue
                rows.append(dict(zip(self.__schema, row)))
        return rows

    def next(self):
        if self.__current_row == self.__num_rows:
            return None
        else:
            row = self.__rows[self.__current_row]
            self.__current_row += 1

            return row
