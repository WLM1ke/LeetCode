source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def to_tree(nodes):
    tree = {}

    for node in nodes:
        add_node_to_tree(tree, node)

    return tree


def add_node_to_tree(tree, node):
    parent, child = node
    if parent is None:
        tree[child] = {}

        return True

    if parent in tree:
        tree[parent][child] = {}

        return True

    for child in tree:
        if add_node_to_tree(tree[child], node):
            return True

    return False


assert to_tree(source) == expected
