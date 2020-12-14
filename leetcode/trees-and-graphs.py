from typing import List
from collections import deque
from heapq import *
import string

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root: return result

        def traverse(node):
            if not node:
                return

            if node.left:
                traverse(node.left)
            result.append(node.val)

            if node.right:
                traverse(node.right)
        traverse(root)
        return result

    def inorderTraversal_iterative(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root: return result

        def traverse(node: TreeNode, depth: int, direction: int):
            if not node:
                return

            if len(result) < depth + 1:
                result.append(deque([node.val]))
                # if depth > 0:
                #     result[depth-1] = list(result[depth-1])
            else:
                if direction == 1:
                    result[depth].append(node.val)
                else:
                    result[depth].appendleft(node.val)

            if direction == 1:
                traverse(node.right, depth+1, -1)
                traverse(node.left, depth+1, -1)
            else:
                traverse(node.left, depth+1, 1)
                traverse(node.right, depth+1, 1)
        traverse(root, 0, 1)
        result[-1] = list(result[-1])
        return result

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk = []
        cntr = 0
        while root or stk:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            cntr += 1

            if cntr == k:
                return root.val
            else:
                root = root.right

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        stk = []
        p_found = False
        while root or stk:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            if p_found:
                return root
            elif root == p:
                p_found = True

            root = root.right

    def numIslands(self, grid: List[List[str]]) -> int:
        LAND, WATER = '1', '0'
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def sink_island(row, col):
            if not(0 <= row < rows) or not(0 <= col < cols) or grid[row][col] == WATER:
                return

            grid[row][col] = WATER
            sink_island(row, col+1)
            sink_island(row, col-1)
            sink_island(row+1, col)
            sink_island(row-1, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    cnt += 1
                    sink_island(r, c)

        for row in grid:
            print(row)

        return cnt

    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        results = []

        def dfs(curr_str, digit_index):
            if len(curr_str) == len(digits):
                results.append(curr_str)
            else:
                for letter in phone[digits[digit_index]]:
                    dfs(curr_str + letter, digit_index+1)

        dfs('', 0)
        return results

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n <= 0: return result

        def add_parenthesis(curr_str, open_cnt, closed_cnt):
            if closed_cnt == n:
                result.append(curr_str)
            else:
                if open_cnt < n:
                    add_parenthesis(curr_str + '(', open_cnt+1, closed_cnt)
                if closed_cnt < open_cnt:
                    add_parenthesis(curr_str + ')', open_cnt, closed_cnt+1)
        add_parenthesis('', 0, 0)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 1: return []

        res = []
        q = deque([[]])
        for i in range(0, len(nums)):
            curr = q.popleft()
            for j in range(len(curr)+1):
                copy_curr = curr.copy()
                copy_curr.insert(j, nums[i])

                if len(copy_curr) < len(nums):
                    q.append(copy_curr)
                else:
                    res.append(copy_curr)
        return res


print(Solution().permute([1,2,3]))
