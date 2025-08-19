from collections import deque
from typing import List, Set, Optional, Dict, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors: List['GraphNode'] = []


class BFSExercises:
    """
    Breadth First Search (BFS) exercises with progressive difficulty.
    
    BFS is a graph traversal algorithm that explores vertices level by level,
    visiting all neighbors before moving to the next depth level.
    """
    
    # BASIC EXERCISES - Understanding BFS fundamentals
    # NOTE: Complete fundamentals_exercises.py before attempting these!
    
    def binary_tree_level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Basic: Return level order traversal of a binary tree.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        
        TODO: Implement this function using BFS
        """
        pass
    
    def binary_tree_right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Basic: Return the values of nodes you can see from the right side of a binary tree.
        
        Example:
        Input: root = [1,2,3,null,5,null,4]
        Output: [1,3,4]
        
        TODO: Implement this function using BFS
        """
        pass
    
    def minimum_depth_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        """
        Basic: Find the minimum depth of a binary tree.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: 2
        
        TODO: Implement this function using BFS
        """
        pass
    
    # INTERMEDIATE EXERCISES - Applying BFS to different problems
    
    def zigzag_level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intermediate: Return zigzag level order traversal (alternate left-to-right and right-to-left).
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        
        TODO: Implement this function using BFS with alternating direction
        """
        pass
    
    def perfect_squares(self, n: int) -> int:
        """
        Intermediate: Find the minimum number of perfect squares that sum to n.
        
        Example:
        Input: n = 12
        Output: 3 (12 = 4 + 4 + 4)
        
        TODO: Implement this function using BFS
        """
        pass
    
    def rotting_oranges(self, grid: List[List[int]]) -> int:
        """
        Intermediate: Find minimum time for all oranges to rot.
        0 = empty, 1 = fresh orange, 2 = rotten orange
        
        Example:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        
        TODO: Implement this function using multi-source BFS
        """
        pass
    
    # ADVANCED EXERCISES - Complex BFS applications
    
    def word_ladder(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Advanced: Find the shortest transformation sequence from begin_word to end_word.
        
        Example:
        Input: begin_word = "hit", end_word = "cog", word_list = ["hot","dot","dog","lot","log","cog"]
        Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
        
        TODO: Implement this function using BFS
        """
        pass
    
    def open_the_lock(self, deadends: List[str], target: str) -> int:
        """
        Advanced: Find minimum steps to open a lock with 4 wheels (0000 to 9999).
        
        Example:
        Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
        Output: 6
        
        TODO: Implement this function using BFS
        """
        pass