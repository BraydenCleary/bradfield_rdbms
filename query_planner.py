class IteratorNode:
  def __init__(self, node_name, func, depth_from_root):
    self.children = []
    self.node_name = node_name
    self.func = func
    self.depth_from_root = depth_from_root

  def add_child(self, node):
    self.children.append(node)

    return self.children

  def __str__(self):
    return f"{self.depth_from_root * '  '}{self.node_name}"

query_tree = {
  'name': 'AVERAGE',
  'lambda': lambda r: r['ratings.rating'],
  'children': [
    {
      'name': 'PROJECTION',
      'lambda': lambda r: r['ratings.rating'],
      'children': [
        {
          'name': 'NESTED_LOOPS_JOIN',
          'lambda': lambda r, s: r['id'] == s['movie_id'],
          'children': [
            {
              'name': 'SELECTION',
              'lambda': lambda r: r.name == 'Medium Cool (1969)',
              'children': [
                {
                  'name': 'FILESCAN',
                  'lambda': lambda _: 'movies',
                  'children': []
                }
              ]
            },
            {
              'name': 'FILESCAN',
              'lambda': lambda _: 'ratings',
              'children': []
            }
          ]
        }
      ]
    }
  ]
}

all_nodes = []

def build_query_tree(tree, depth_from_root):
  node = IteratorNode(tree['name'], tree['lambda'], depth_from_root)
  
  all_nodes.append(node)
  
  depth_from_root += 1

  if tree['children']:
    for child_node in tree['children']:
      node.add_child(build_query_tree(child_node, depth_from_root))
    
  return node

root_node = build_query_tree(query_tree, 0)

for node in all_nodes:
  print(node)
