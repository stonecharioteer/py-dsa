from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class TwoPointersExercises:
    """
    Two Pointers technique exercises with progressive difficulty.
    
    Two pointers is a technique where we use two pointers to traverse data structures.
    Common patterns:
    1. Opposite direction: Start from both ends and move towards center
    2. Same direction: Fast and slow pointers (Floyd's algorithm)
    3. Different arrays: One pointer for each array
    """
    
    # BASIC EXERCISES - Opposite direction two pointers
    
    def pair_with_target_sum(self, arr: List[int], target: int) -> List[int]:
        """
        Basic: Find pair of numbers that sum to target in sorted array.
        
        Example:
        Input: arr = [1, 2, 3, 4, 6], target = 6
        Output: [1, 3] (indices of numbers 2 and 4)
        
        TODO: Use two pointers from start and end
        """
        pass
    
    def remove_duplicates_sorted_array(self, nums: List[int]) -> int:
        """
        Basic: Remove duplicates from sorted array in-place.
        
        Example:
        Input: nums = [1, 1, 2, 3, 3, 3, 4, 4]
        Output: 4 (unique length), nums = [1, 2, 3, 4, ...]
        
        TODO: Use two pointers to track unique elements
        """
        pass
    
    def move_zeros_to_end(self, nums: List[int]) -> None:
        """
        Basic: Move all zeros to end while maintaining relative order.
        
        Example:
        Input: nums = [0, 1, 0, 3, 12]
        Output: nums = [1, 3, 12, 0, 0]
        
        TODO: Use two pointers to swap non-zero elements
        """
        pass
    
    def reverse_string(self, s: List[str]) -> None:
        """
        Basic: Reverse string in-place using two pointers.
        
        Example:
        Input: s = ["h","e","l","l","o"]
        Output: s = ["o","l","l","e","h"]
        
        TODO: Use two pointers from both ends
        """
        pass
    
    def valid_palindrome(self, s: str) -> bool:
        """
        Basic: Check if string is palindrome (ignore non-alphanumeric).
        
        Example:
        Input: s = "A man, a plan, a canal: Panama"
        Output: True
        
        TODO: Use two pointers with character filtering
        """
        pass
    
    # INTERMEDIATE EXERCISES - Same direction and array merging
    
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Intermediate: Find all unique triplets that sum to zero.
        
        Example:
        Input: nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
        
        TODO: Sort array and use two pointers for each element
        """
        pass
    
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Intermediate: Find sum of three numbers closest to target.
        
        Example:
        Input: nums = [-1, 2, 1, -4], target = 1
        Output: 2 (sum of -1, 2, 1)
        
        TODO: Sort and use two pointers to minimize difference
        """
        pass
    
    def container_with_most_water(self, height: List[int]) -> int:
        """
        Intermediate: Find container that can hold most water.
        
        Example:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        
        TODO: Use two pointers from both ends, move smaller height
        """
        pass
    
    def merge_sorted_arrays(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Intermediate: Merge nums2 into nums1 in-place.
        
        Example:
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: nums1 = [1,2,2,3,5,6]
        
        TODO: Use two pointers starting from end of both arrays
        """
        pass
    
    def intersect_two_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Intermediate: Find intersection of two sorted arrays.
        
        Example:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        
        TODO: Use two pointers to traverse both arrays
        """
        pass
    
    # ADVANCED EXERCISES - Fast and slow pointers (Floyd's algorithm)
    
    def linked_list_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Advanced: Detect if linked list has a cycle.
        
        Example:
        Input: head = [3,2,0,-4] with cycle at position 1
        Output: True
        
        TODO: Use fast and slow pointers (Floyd's algorithm)
        """
        pass
    
    def find_duplicate_number(self, nums: List[int]) -> int:
        """
        Advanced: Find duplicate number in array (Floyd's algorithm on array).
        
        Example:
        Input: nums = [1,3,4,2,2]
        Output: 2
        
        TODO: Treat array as linked list and use Floyd's algorithm
        """
        pass
    
    def linked_list_cycle_start(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Advanced: Find the start of cycle in linked list.
        
        Example:
        Input: head = [3,2,0,-4] with cycle starting at node with value 2
        Output: Node with value 2
        
        TODO: Use Floyd's algorithm and mathematical relationship
        """
        pass
    
    def happy_number(self, n: int) -> bool:
        """
        Advanced: Determine if number is happy (Floyd's algorithm for cycle detection).
        
        Example:
        Input: n = 19
        Output: True (1² + 9² = 82, 8² + 2² = 68, 6² + 8² = 100, 1² + 0² + 0² = 1)
        
        TODO: Use fast and slow pointers to detect cycle in sum sequence
        """
        pass
    
    def middle_of_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Advanced: Find middle node of linked list.
        
        Example:
        Input: head = [1,2,3,4,5]
        Output: Node with value 3
        
        TODO: Use fast and slow pointers
        """
        pass
    
    def palindromic_linked_list(self, head: Optional[ListNode]) -> bool:
        """
        Advanced: Check if linked list is palindrome.
        
        Example:
        Input: head = [1,2,2,1]
        Output: True
        
        TODO: Find middle, reverse second half, compare with first half
        """
        pass
    
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Advanced: Find all unique quadruplets that sum to target.
        
        Example:
        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        
        TODO: Extend three sum with additional outer loop
        """
        pass