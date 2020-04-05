from filescan import Filescan
from sort import Sort
from distinct import Distinct
from projection import Projection
from selection import Selection
from sort import Sort
from limit import Limit
from average import Average
from count import Count

class QueryExecutor:
	VALID_ITERATOR_NODE_TYPES = ["PROJECTION", "SELECTION", "FILESCAN", "SORT", "DISTINCT", "LIMIT", "AVERAGE", "COUNT"]

	def __init__(self, parsed_query):
		self.__parsed_query = parsed_query
		self.__root = self.__build_iterator_node_linked_list()
		self.__result = self.__execute()

	def get_result(self):
		return self.__result

	def __build_iterator_node_linked_list(self):
		## Question ## 
		# Should this be solved recursively?
		prev = None

		for idx, (iterator_node_type, iterator_node_args) in enumerate(reversed(self.__parsed_query)):
			if iterator_node_type not in self.VALID_ITERATOR_NODE_TYPES:
				raise(f'{iterator_node_type} is not a known iterator node type')

			is_first_node = (idx == 0)
			is_last_node = (idx == (len(self.__parsed_query) - 1))

			if is_first_node:
				prev = eval(iterator_node_type.title())(None, iterator_node_args)
			elif is_last_node:
				return eval(iterator_node_type.title())(prev, iterator_node_args)
			else:
				prev = eval(iterator_node_type.title())(prev, iterator_node_args)

	def __execute(self):
		result = []
		next_from_root = self.__root.next()
		while next_from_root:
			result.append(next_from_root)
			next_from_root = self.__root.next()
		return result

if __name__ == "__main__":
	parsed_query = 	[
		# ["AVERAGE", []],
		# ["LIMIT", ["10"]],
		# ["PROJECTION", ["id"]],
		# ["SORT", ["title"]],
		# ["SELECTION", ["genres", "EQUALS", "Comedy"]],
		["COUNT", []],
		["DISTINCT", []],
		["PROJECTION", ["movieId"]],
		["SORT", ["movieId"]],
		["FILESCAN", ["ratings"]]
	]

	executor = QueryExecutor(parsed_query)
	result = executor.get_result()
	print(result)
