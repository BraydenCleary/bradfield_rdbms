class Iterator:
    def __init__(self, func, depth_from_root):
        self.children = []
        self.func = func
        self.depth_from_root = depth_from_root

    def add_child(self, node):
        self.children.append(node)

        return self.children

    def __str__(self):
        return f"{self.depth_from_root * '  '}{self.__name__}"

    def next(self):
        # implement me in subclass 
        pass