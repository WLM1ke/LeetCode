class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


def reverse(node: Node | None) -> Node | None:
    if not Node:
        return None

    prev = None

    while node:
        prev, node.next, node.prev, node = node, node.prev, node.next, node.next

    return prev
