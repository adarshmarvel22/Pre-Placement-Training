class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructTree(s):
    if not s:
        return None

    opening = s.find('(')

    if opening == -1:
        return TreeNode(int(s))

    value = int(s[:opening])
    root = TreeNode(value)

    closing = findClosingParenthesis(s, opening)

    root.left = constructTree(s[opening+1:closing])
    root.right = constructTree(s[closing+2:-1])

    return root


def findClosingParenthesis(s, opening):
    count = 1
    closing = opening + 1

    while count > 0:
        if s[closing] == '(':
            count += 1
        elif s[closing] == ')':
            count -= 1
        closing += 1

    return closing - 1


# Test the function with the given example
s = "4(2(3)(1))(6(5))"
root = constructTree(s)

# Function to print the values of the tree in in-order traversal
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

# Print the tree in in-order traversal
inorderTraversal(root)
