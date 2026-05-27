# A TreeNode stores data and references to its LEFT and RIGHT children.
# In a BST: everything in the left subtree is SMALLER than the node,
#           everything in the right subtree is LARGER.
class TreeNode:
    def __init__(self, data):
        self.data = data        # value stored in this node
        self.left = None        # left child (smaller values go here)
        self.right = None       # right child (larger values go here)


class BST:
    def __init__(self):
        self.root = None        # empty tree has no root

    # insert() adds a value into the correct position in the tree
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)    # first insert becomes the root
        else:
            self._insert_recursive(self.root, data)

    # _insert_recursive() walks down the tree to find the right spot
    def _insert_recursive(self, node, data):
        if data < node.data:
            # value is smaller → go LEFT
            if node.left is None:
                node.left = TreeNode(data)     # empty spot found, insert here
            else:
                self._insert_recursive(node.left, data)   # keep going left
        else:
            # value is larger or equal → go RIGHT
            if node.right is None:
                node.right = TreeNode(data)    # empty spot found, insert here
            else:
                self._insert_recursive(node.right, data)  # keep going right

    # search() checks if a value exists in the tree
    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        # base case: node is None means we fell off the tree — not found
        if node is None:
            return False

        if data == node.data:
            return True           # found it!
        elif data < node.data:
            return self._search_recursive(node.left, data)   # look left
        else:
            return self._search_recursive(node.right, data)  # look right

    # inorder() traversal visits nodes: LEFT → ROOT → RIGHT
    # For a BST this always prints values in SORTED (ascending) order
    def inorder(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node is None:
            return
        self._inorder_recursive(node.left)    # visit left subtree first
        print(node.data, end=" ")             # then print this node
        self._inorder_recursive(node.right)   # then visit right subtree


# --- main program ---
tree = BST()

# insert values — the BST will automatically place them in the right spots
tree.insert(50)   # becomes the root
tree.insert(30)   # 30 < 50, goes LEFT of root
tree.insert(70)   # 70 > 50, goes RIGHT of root
tree.insert(20)   # 20 < 50, then 20 < 30 → LEFT of 30
tree.insert(40)   # 40 < 50, then 40 > 30 → RIGHT of 30

print("Inorder traversal (should print sorted):")
tree.inorder()    # Output: 20 30 40 50 70

print("Search for 40:", tree.search(40))   # True
print("Search for 99:", tree.search(99))   # False