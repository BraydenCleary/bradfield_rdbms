class QueryExecutor:
    def __init__(self, root):
        self.__root = root
        self.__result = self.__execute()

    def get_root(self):
        return self.__root

    def get_result(self):
        return self.__result

    def __execute(self):
        result = []
        next_from_root = self.__root.next()
        while next_from_root:
            result.append(next_from_root)
            next_from_root = self.__root.next()
        return result
