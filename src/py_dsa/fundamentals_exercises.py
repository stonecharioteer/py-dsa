from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class FundamentalsExercises:
    """
    Fundamental data structures and algorithms exercises.
    
    This module covers essential concepts:
    - Queues (FIFO data structure)
    - Trees (hierarchical data structure)
    - Recursion (function calling itself)
    - Memoization (caching results)
    - Basic array operations
    
    Complete these before attempting BFS and DP exercises.
    """
    
    # QUEUE EXERCISES - Essential for BFS
    
    def implement_queue_with_list(self) -> 'SimpleQueue':
        """
        Create a simple Queue class using Python list.
        Understand FIFO (First In, First Out) principle.
        
        TODO: Implement a Queue class with:
        - enqueue(item): Add item to rear
        - dequeue(): Remove and return item from front
        - is_empty(): Check if queue is empty
        - size(): Return number of items
        """
        pass
    
    def implement_queue_with_deque(self) -> None:
        """
        Practice using collections.deque for queue operations.
        This is more efficient than using list for queue operations.
        
        TODO: Practice using deque.append() and deque.popleft()
        """
        pass
    
    def queue_simulation(self, operations: List[str]) -> List[int]:
        """
        Simulate queue operations and return results.
        
        Example:
        Input: ["enqueue 1", "enqueue 2", "dequeue", "enqueue 3", "dequeue"]
        Output: [1, 2] (results of dequeue operations)
        
        TODO: Process operations and return dequeue results
        """
        pass
    
    # TREE EXERCISES - Essential for BFS tree problems
    
    def tree_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Implement iterative tree traversal using a queue.
        This is fundamental for understanding BFS on trees.
        
        Example:
        Input: root = [1,2,3,4,5]
        Output: [1,2,3,4,5] (breadth-first order)
        
        TODO: Traverse tree level by level using a queue
        """
        # Starter implementation - returns empty list
        # Students should implement the full BFS traversal
        return []
    
    def count_tree_nodes(self, root: Optional[TreeNode]) -> int:
        """
        Count total nodes in a binary tree using iterative approach.
        
        Example:
        Input: root = [1,2,3,4,5]
        Output: 5
        
        TODO: Use queue to count all nodes
        """
        pass
    
    def find_tree_height(self, root: Optional[TreeNode]) -> int:
        """
        Find height of binary tree using level-order traversal.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
        
        TODO: Use BFS approach to find height
        """
        pass
    
    def create_tree_from_list(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Create binary tree from level-order list representation.
        
        Example:
        Input: [1,2,3,null,null,4,5]
        Output: TreeNode representing the tree
        
        TODO: Build tree using queue for level-order construction
        """
        pass
    
    # RECURSION EXERCISES - Essential for DP
    
    def simple_recursion_factorial(self, n: int) -> int:
        """
        Implement factorial using recursion.
        Understand base case and recursive case.
        
        Example:
        Input: n = 5
        Output: 120 (5! = 5*4*3*2*1)
        
        TODO: Implement factorial recursively
        """
        pass
    
    def simple_recursion_fibonacci(self, n: int) -> int:
        """
        Implement naive recursive Fibonacci.
        This will be inefficient but helps understand recursion.
        
        Example:
        Input: n = 5
        Output: 5 (0,1,1,2,3,5)
        
        TODO: Implement recursive Fibonacci
        """
        pass
    
    def count_recursive_calls(self, n: int) -> int:
        """
        Count how many recursive calls are made for fibonacci(n).
        This demonstrates why we need optimization.
        
        TODO: Modify fibonacci to count and return number of calls
        """
        pass
    
    def understand_call_stack(self, n: int) -> List[int]:
        """
        Trace the call stack for a simple recursive function.
        
        Example:
        Input: n = 3
        Output: [3, 2, 1, 0] (order of function calls)
        
        TODO: Create a function that tracks its call sequence
        """
        pass
    
    # MEMOIZATION EXERCISES - Bridge to DP
    
    def memoized_fibonacci(self, n: int, memo: Optional[dict] = None) -> int:
        """
        Implement memoized Fibonacci using top-down approach.
        
        Example:
        Input: n = 50
        Output: 12586269025 (computed efficiently)
        
        TODO: Use dictionary to cache results
        """
        pass
    
    def compare_fibonacci_performance(self, n: int) -> dict:
        """
        Compare performance of recursive vs memoized fibonacci.
        
        TODO: Measure time taken for both approaches
        """
        pass
    
    # ARRAY EXERCISES - Essential for both BFS and DP
    
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target (brute force).
        
        Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1] (indices of 2 and 7)
        
        TODO: Use nested loops to find the pair
        """
        pass
    
    def two_sum_hash_map(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target (optimized with hash map).
        
        TODO: Use dictionary to optimize the search
        """
        pass
    
    def max_subarray_sum_brute_force(self, nums: List[int]) -> int:
        """
        Find maximum subarray sum using brute force.
        
        Example:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6 (subarray [4,-1,2,1])
        
        TODO: Check all possible subarrays
        """
        pass


# Helper class for queue implementation
class SimpleQueue:
    """
    Simple queue implementation using Python list.
    Students should implement this as part of the exercises.
    """
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to the rear of the queue."""
        pass  # TODO: Implement this
    
    def dequeue(self):
        """Remove and return item from the front of the queue."""
        pass  # TODO: Implement this
    
    def is_empty(self):
        """Check if the queue is empty."""
        pass  # TODO: Implement this
    
    def size(self):
        """Return the number of items in the queue."""
        pass  # TODO: Implement this