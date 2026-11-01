# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calc_inorder(node: TreeNode) -> list[int]:
  if node == None:
    return []
  
  return calc_inorder(node.left) + [node.val] + calc_inorder(node.right)

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
      n = len(preorder)
      root = TreeNode(val=inorder[0])
      prev_node = root

      for i in range(1, n):
        prev_node.left = TreeNode(val=preorder[i])

        if calc_inorder(root) == inorder[:i+1]:
          prev_node = prev_node.left
          continue

        prev_node.left = None
        prev_node.right = TreeNode(val=preorder[i])

        if calc_inorder(root) != inorder[:i+1]:
          print(i)
          raise Exception("This algorithm looks wrong")

      answer = []
      to_check = [root]
      while(len(to_check)):
        current_node = to_check[0]

        if current_node == None:
          answer.append(null)
        else:
          answer.append(current_node.val)
          to_check.append(current_node.left)
          to_check.append(current_node.right)

        to_check.pop()

      return answer
