class Node:
    def __init__(self, key) -> None:
        self.data = key
        self.left = self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def levelorder(root):
    if root is None:
        return
    q = [root]
    while q:
        c_level = []
        n = len(q)
        for jhb in range(n):
            p = q.pop(0)
            c_level.append(p.data)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        print(*c_level, sep=" ", end=" ")


def is_full(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left != None and root.right != None:
        return is_full(root.left) and is_full(root.right)
    return False


def is_perfect(root, d=0, l=0):
    if root == None:
        return True
    if root.left != None and root.right != None:
        return d == l+1
    if root.left != None or root.right != None:
        return False
    return is_perfect(root.left, d, l+1) and is_perfect(root.right, d, l+1)


def is_balanced(root):
    if root == None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    return abs(left_height-right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def height(root):
    if root == None:
        return 0
    return 1+max(height(root.left), height(root.right))


# drivercode
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inorder(root)
    print("/n")
    preorder(root)
    print("/n")
    postorder(root)
    print("/n")
    levelorder(root)
