from iterator import Iterator

class Limit(Iterator):
    def __init__(self, func, depth_from_root=0):
        super().__init__(func, depth_from_root)
        self.row_limit = self.func()
        self.current_row = 0

    def next(self):
        child = self.children[0] if self.children else None

        if child:
            if self.current_row < self.row_limit:
                self.current_row += 1
                return child.next()
