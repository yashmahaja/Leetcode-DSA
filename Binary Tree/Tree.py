from collections import deque

class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, left=None, right=None, val=None):
        self.val = val
        self.left = left
        self.right = right


def display(root):
    """Display the binary tree in a readable format."""
    if root is None:
        return
    print(f"{root.val} -> ", end="")
    if root.left is not None:
        print(f"{root.left.val} ", end="")
    if root.right is not None:
        print(f"{root.right.val}", end="")
    print()
    display(root.left)
    display(root.right)


def size(root):
    """Return the number of nodes in the tree."""
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


def tree_sum(root):
    """Return the sum of all node values in the tree."""
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def product_of_tree(root):
    """Return the product of all node values in the tree."""
    if not root:
        return 1
    return root.val * product_of_tree(root.left) * product_of_tree(root.right)


def height(root):
    """Return the height of the tree."""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def max_value(root):
    """Return the maximum value in the tree."""
    if not root:
        return float("-inf")
    return max(root.val, max_value(root.left), max_value(root.right))


def min_value(root):
    """Return the minimum value in the tree."""
    if not root:
        return float("inf")
    return min(root.val, min_value(root.left), min_value(root.right))


def preorder(root):
    """Traverse the tree in preorder and print values."""
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    """Traverse the tree in inorder and print values."""
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def postorder(root):
    """Traverse the tree in postorder and print values."""
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


def nth_level_order(root, n):
    """Print all nodes at the nth level of the tree."""
    if not root:
        return
    if n == 1:
        print(root.val, end=" ")
        return
    nth_level_order(root.left, n - 1)
    nth_level_order(root.right, n - 1)


def all_levels(root):
    """Print all levels of the tree."""
    h = height(root)
    for i in range(1, h + 1):
        print(f"Level {i}:", end=" ")
        nth_level_order(root, i)
        print()


def bfs(root):
    """Perform Breadth-First Search (Level Order Traversal) on the tree."""
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_iterative(root):
    """Perform Depth-First Search using an iterative approach."""
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def dfs_recursive(root):
    """Perform Depth-First Search using recursion."""
    if not root:
        return
    print(root.val, end=" ")
    dfs_recursive(root.left)
    dfs_recursive(root.right)


def main():
    # Create the tree
    root = Node(val=10)
    a = Node(val=8)
    b = Node(val=12)
    root.left = a
    root.right = b
    c = Node(val=6)
    d = Node(val=90)
    a.left = c
    a.right = d
    f = Node(val=7)
    g = Node(val=92)
    c.left = f
    e = Node(val=11)
    b.left = e
    e.right = g

    # Display the tree
    print("Tree Structure:")
    display(root)

    # Perform tree operations
    print("\nTree Properties:")
    print(f"Count of Nodes: {size(root)}")
    print(f"Sum of Values: {tree_sum(root)}")
    print(f"Product of Values: {product_of_tree(root)}")
    print(f"Height of Tree: {height(root)}")
    print(f"Max Value: {max_value(root)}")
    print(f"Min Value: {min_value(root)}")

    # Traversals
    print("\nTree Traversals:")
    print("Preorder:", end=" ")
    preorder(root)
    print("\nInorder:", end=" ")
    inorder(root)
    print("\nPostorder:", end=" ")
    postorder(root)

    # Perform BFS
    print("\n\nBFS Traversal:")
    bfs(root)

    # Perform DFS (Iterative)
    print("\nDFS Traversal (Iterative):")
    dfs_iterative(root)

    # Perform DFS (Recursive)
    print("\nDFS Traversal (Recursive):")
    dfs_recursive(root)


if __name__ == "__main__":
    main()
