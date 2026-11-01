# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n^2)
# Space: O(n)
# 91:28

def dfs(node: TreeNode, preorder: list[int], inorder: list[int]) -> TreeNode:
    preorder_index = preorder.index(node.val)
    inorder_index = inorder.index(node.val)

    inorder_left = inorder[:inorder_index]
    inorder_right = inorder[inorder_index+1:]

    if len(inorder_left):
      for i in range(preorder_index+1, len(preorder)):
        if preorder[i] in inorder_left:
          node.left = dfs(TreeNode(val=preorder[i]), preorder, inorder_left)
          break

    if len(inorder_right):
      for i in range(preorder_index+1, len(preorder)):
        if preorder[i] in inorder_right:
          node.right = dfs(TreeNode(val=preorder[i]), preorder, inorder_right)
          break

    return node

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
      n = len(preorder)
      root = TreeNode(val=preorder[0])

      return dfs(root, preorder, inorder)
