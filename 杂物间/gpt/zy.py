class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(edges):
    nodes = {}
    for x, y in edges:
        if x not in nodes:
            nodes[x] = TreeNode(x)
        if y not in nodes:
            nodes[y] = TreeNode(y)
        nodes[x].children.append(nodes[y])
    return nodes

def find_root(tree):
    for node in tree.values():
        if not any(n.children.count(node) > 0 for n in tree.values()):
            return node

def find_leaves(tree):
    return [node for node in tree.values() if not node.children]

def find_depth(node):
    if not node.children:
        return 0
    return 1 + max(find_depth(child) for child in node.children)

edges = [("e", "i"), ("b", "e"), ("b", "d"), ("a", "b"), ("g", "j"), ("c", "g"), ("c", "f"), ("h", "l"), ("c", "h"), ("a", "c")]

tree = build_tree(edges)
root = find_root(tree)
leaves = find_leaves(tree)
depth = find_depth(root)

print("根结点:", root.value)
print("叶子结点:", [leaf.value for leaf in leaves])
print("树的深度:", depth)
             a
            / \
           b   c
          /   /|\
         e   h f g
        /   /     \ 
       i   l       j
