from typing import List, Dict, Set, Optional
from collections import defaultdict, deque


class SlidingWindowExercises:
    """
    Sliding Window technique exercises with progressive difficulty.
    
    Sliding window is an optimization technique for solving problems that involve
    arrays/strings where we need to find subarrays that satisfy certain conditions.
    
    Two main types:
    1. Fixed-size window: Window size is constant
    2. Variable-size window: Window size changes based on conditions
    """
    
    # BASIC EXERCISES - Fixed size sliding window
    
    def maximum_sum_subarray_of_size_k(self, arr: List[int], k: int) -> int:
        """
        Basic: Find maximum sum of subarray of size k.
        
        Example:
        Input: arr = [2, 1, 5, 1, 3, 2], k = 3
        Output: 9 (subarray [5, 1, 3])
        
        TODO: Use sliding window to find maximum sum
        """
        pass
    
    def average_of_subarrays_size_k(self, arr: List[int], k: int) -> List[float]:
        """
        Basic: Find average of all subarrays of size k.
        
        Example:
        Input: arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
        Output: [2.2, 2.8, 2.4, 3.6, 2.8]
        
        TODO: Calculate averages using sliding window
        """
        pass
    
    def first_negative_in_window_size_k(self, arr: List[int], k: int) -> List[int]:
        """
        Basic: Find first negative number in every window of size k.
        
        Example:
        Input: arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
        Output: [-1, -1, -7, -15, -15, 0]
        
        TODO: Use sliding window with queue to track negatives
        """
        pass
    
    # INTERMEDIATE EXERCISES - Variable size sliding window
    
    def longest_substring_with_k_distinct_chars(self, s: str, k: int) -> int:
        """
        Intermediate: Find length of longest substring with exactly k distinct characters.
        
        Example:
        Input: s = "araaci", k = 2
        Output: 4 (substring "araa")
        
        TODO: Use variable size sliding window with hash map
        """
        pass
    
    def smallest_subarray_with_sum_greater_than_s(self, arr: List[int], target_sum: int) -> int:
        """
        Intermediate: Find length of smallest subarray with sum >= target_sum.
        
        Example:
        Input: arr = [2, 1, 2, 3, 3, 1, 1, 1], target_sum = 7
        Output: 2 (subarray [3, 3])
        
        TODO: Use variable size sliding window
        """
        pass
    
    def longest_substring_without_repeating_chars(self, s: str) -> int:
        """
        Intermediate: Find length of longest substring without repeating characters.
        
        Example:
        Input: s = "abcabcbb"
        Output: 3 (substring "abc")
        
        TODO: Use sliding window with set/hash map
        """
        pass
    
    def max_fruits_in_baskets(self, fruits: List[int]) -> int:
        """
        Intermediate: Pick maximum fruits with only 2 types of fruits.
        (Equivalent to longest substring with at most 2 distinct characters)
        
        Example:
        Input: fruits = [1, 2, 1, 2, 3, 1, 2]
        Output: 5 (fruits [1, 2, 1, 2] or [2, 3, 1, 2])
        
        TODO: Use sliding window with hash map
        """
        pass
    
    # ADVANCED EXERCISES - Complex sliding window problems
    
    def minimum_window_substring(self, s: str, t: str) -> str:
        """
        Advanced: Find minimum window substring that contains all characters of t.
        
        Example:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        
        TODO: Use sliding window with two hash maps
        """
        pass
    
    def longest_substring_with_same_letters_after_k_replacements(self, s: str, k: int) -> int:
        """
        Advanced: Find length of longest substring with same letters after replacing at most k characters.
        
        Example:
        Input: s = "AABABBA", k = 1
        Output: 4 (replace one A to get "AABBB" -> "BBBB")
        
        TODO: Use sliding window with frequency map
        """
        pass
    
    def max_consecutive_ones_after_k_flips(self, nums: List[int], k: int) -> int:
        """
        Advanced: Find max consecutive 1s after flipping at most k zeros.
        
        Example:
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6 (flip two 0s to get 6 consecutive 1s)
        
        TODO: Use sliding window counting zeros
        """
        pass
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Advanced: Find maximum element in every sliding window of size k.
        
        Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        
        TODO: Use sliding window with deque (monotonic queue)
        """
        pass
    
    def permutation_in_string(self, s1: str, s2: str) -> bool:
        """
        Advanced: Check if any permutation of s1 is a substring of s2.
        
        Example:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: True (s2 contains "ba" which is a permutation of "ab")
        
        TODO: Use sliding window with character frequency matching
        """
        pass
    
    def find_all_anagrams(self, s: str, p: str) -> List[int]:
        """
        Advanced: Find all start indices of anagrams of p in s.
        
        Example:
        Input: s = "abab", p = "ab"
        Output: [0, 2] (anagrams "ab" at index 0 and "ba" at index 2)
        
        TODO: Use sliding window with frequency matching
        """
        pass