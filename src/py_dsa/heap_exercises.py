import heapq
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class HeapExercises:
    """
    Heap and Priority Queue exercises with progressive difficulty.
    
    Heaps are complete binary trees that maintain heap property:
    - Min Heap: parent ≤ children (root is minimum)
    - Max Heap: parent ≥ children (root is maximum)
    
    Python's heapq implements min heap. For max heap, negate values.
    """
    
    # BASIC EXERCISES - Understanding heap operations
    
    def kth_largest_element(self, nums: List[int], k: int) -> int:
        """
        Basic: Find the kth largest element in an array.
        
        Example:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5
        
        TODO: Use min heap of size k to track largest elements
        """
        return 0
    
    def kth_smallest_element(self, nums: List[int], k: int) -> int:
        """
        Basic: Find the kth smallest element in an array.
        
        Example:
        Input: nums = [7,10,4,3,20,15], k = 3
        Output: 7
        
        TODO: Use max heap of size k or min heap with all elements
        """
        return 0
    
    def last_stone_weight(self, stones: List[int]) -> int:
        """
        Basic: Simulate stone smashing game using max heap.
        
        Example:
        Input: stones = [2,7,4,1,8,1]
        Output: 1
        
        TODO: Use max heap to always get heaviest stones
        """
        return 0
    
    def merge_k_sorted_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Basic: Merge k sorted linked lists using heap.
        
        Example:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        
        TODO: Use min heap to track smallest current elements
        """
        return None
    
    # INTERMEDIATE EXERCISES - Heap with additional data structures
    
    def top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        """
        Intermediate: Find k most frequent elements.
        
        Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        
        TODO: Use frequency map + min heap of size k
        """
        return []
    
    def k_closest_points_to_origin(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Intermediate: Find k closest points to origin (0,0).
        
        Example:
        Input: points = [[1,1],[2,2],[3,3]], k = 1
        Output: [[1,1]]
        
        TODO: Use max heap of size k with distance as key
        """
        return []
    
    def task_scheduler(self, tasks: List[str], n: int) -> int:
        """
        Intermediate: Schedule tasks with cooldown period.
        
        Example:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8 (A -> B -> idle -> A -> B -> idle -> A -> B)
        
        TODO: Use max heap with frequency + cooldown tracking
        """
        return 0
    
    def reorganize_string(self, s: str) -> str:
        """
        Intermediate: Reorganize string so no two same chars are adjacent.
        
        Example:
        Input: s = "aab"
        Output: "aba"
        
        TODO: Use max heap with character frequencies
        """
        return ""
    
    # ADVANCED EXERCISES - Complex heap applications
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Advanced: Find maximum in every sliding window of size k.
        
        Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        
        TODO: Use max heap with lazy deletion or deque
        """
        return []
    
    def find_median_from_data_stream(self) -> 'MedianFinder':
        """
        Advanced: Design data structure to find median from stream.
        
        Example:
        addNum(1), addNum(2) -> findMedian() = 1.5
        addNum(3) -> findMedian() = 2.0
        
        TODO: Use two heaps (max heap for smaller half, min heap for larger)
        """
        return MedianFinder()
    
    def merge_k_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        """
        Advanced: Merge k sorted arrays efficiently.
        
        Example:
        Input: arrays = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        
        TODO: Use min heap with array indices tracking
        """
        return []
    
    def smallest_range_covering_elements(self, nums: List[List[int]]) -> List[int]:
        """
        Advanced: Find smallest range that includes at least one from each array.
        
        Example:
        Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        Output: [20,24]
        
        TODO: Use min heap with range tracking
        """
        return []
    
    def ipo_maximize_capital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Advanced: IPO problem - maximize capital with k projects.
        
        Example:
        Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
        Output: 4
        
        TODO: Use two heaps for available and profitable projects
        """
        return 0


class MedianFinder:
    """
    Helper class for finding median from data stream.
    Students should implement this as part of the exercise.
    """
    
    def __init__(self):
        """Initialize data structure."""
        # TODO: Initialize two heaps
        pass
    
    def addNum(self, num: int) -> None:
        """Add a number to the data structure."""
        # TODO: Add number and rebalance heaps
        pass
    
    def findMedian(self) -> float:
        """Return median of all elements."""
        # TODO: Calculate median from heap tops
        return 0.0