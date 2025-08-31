class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        """Depth-first search to find a node with the given id."""
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node['id'] == target_id:
                return node
            # DFS: add children to the beginning
            nodes_to_visit = node['children'] + nodes_to_visit

        return None

    pass
