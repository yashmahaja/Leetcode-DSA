
class Node:
    def __init__(self,left=None,right=None,val=None):
        self.val = val
        self.left = left
        self.right = right

def display(root):
    if root is None:
        return
    print(root.val, " -> ", end=' ')
    if root.left is not None:
        print(root.left.val, end=' ')
    if root.right is not None:
        print(root.right.val)
    print()
    display(root.left)
    display(root.right)

def size(count, root):
    if not root:
        return count
    return 1 + size(count,root.left) + size(count,root.right)

def Sum(sum, root):
    if not root:
        return sum
    return root.val + Sum(sum, root.left) + Sum(sum,root.right)

def Height(height, root):
    if not root:
        return height
    return 1

def Max(maxtree, root):
    if not root:
        return maxtree
    return max(root.val,Max(maxtree,root.left), Max(maxtree,root.right))

def main():
    root = Node(val=10)
    # root.val = 1
    a = Node(val=8)
    b = Node(val=12)
    root.left = a
    root.right = b
    c = Node(val=6)
    d = Node(val=90)
    a.left = c
    a.right = d
    e = Node(val=11)
    b.left = e
    display(root)
    count = size(0, root)
    print(count)
    sum = Sum(0, root)
    print(sum)
    height = Height(0, root)
    print(height)
    max = Max(0, root)
    print(max)

if __name__ == "__main__":
    main()