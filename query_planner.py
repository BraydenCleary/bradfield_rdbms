from filescan import Filescan
from sort import Sort
from distinct import Distinct
from projection import Projection
from selection import Selection
from sort import Sort
from limit import Limit
from average import Average
from count import Count

class QueryPlanner:
    def __init__(self, query):
        self.nodes = []
        self.root = self.__build_query_tree(query, 0)

    def __build_query_tree(self, tree, depth_from_root):
        node = eval(tree['name'])(tree['lambda'], depth_from_root)
  
        self.nodes.append(node)
  
        depth_from_root += 1

        if tree['children']:
            for child_node in tree['children']:
                node.add_child(self.__build_query_tree(child_node, depth_from_root))

        return node

    def __str__(self):
        print('')
        for node in self.nodes:
            print(node)
        return ''
