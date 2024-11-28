class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Function to build a binary tree from level-order input
def build_tree(level_order):
    if not level_order or level_order[0] == -1:
        return None
    root = TreeNode(level_order.pop(0))
    queue = [root]
    while level_order:
        node = queue.pop(0)
        if not node:
            continue
        left_val = level_order.pop(0) if level_order else -1
        right_val = level_order.pop(0) if level_order else -1
        if left_val != -1:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        if right_val != -1:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root

# Function to calculate the diameter of the binary tree (in terms of nodes)
def diameter_of_binary_tree(root):
    def helper(node):
        if not node:
            return 0, 0  # (depth, diameter)
        left_depth, left_diameter = helper(node.left)
        right_depth, right_diameter = helper(node.right)
        # Current diameter at this node (in terms of nodes)
        current_diameter = left_depth + right_depth + 1
        # Maximum diameter
        max_diameter = max(left_diameter, right_diameter, current_diameter)
        # Return (depth, maximum diameter)
        return max(left_depth, right_depth) + 1, max_diameter

    return helper(root)[1]

# Input data from the user
level_order_input = input("Enter the level-order traversal (comma-separated, -1 for null): ")
level_order = list(map(int, level_order_input.split(',')))

# Build the binary tree from the input
root = build_tree(level_order)

# Calculate and print the diameter of the binary tree (in terms of nodes)
print("Diameter of the Binary Tree (number of nodes):", diameter_of_binary_tree(root))

