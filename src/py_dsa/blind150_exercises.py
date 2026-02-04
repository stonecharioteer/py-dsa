from typing import List, Optional, Dict
from collections import defaultdict, deque
import heapq


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Blind150Exercises:
    """
    Blind 150 LeetCode problems - Essential for coding interviews.
    
    This collection covers the most important algorithmic patterns and problems
    commonly asked in FAANG and other top tech companies. Organized by topic
    for systematic practice.
    
    Categories:
    - Array & Hashing
    - Two Pointers  
    - Sliding Window
    - Stack
    - Binary Search
    - Linked List
    - Trees
    - Tries
    - Heap/Priority Queue
    - Backtracking
    - Graphs
    - Advanced Graphs
    - 1-D Dynamic Programming
    - 2-D Dynamic Programming
    - Greedy
    - Intervals
    - Math & Geometry
    - Bit Manipulation
    """
    
    # ARRAY & HASHING (9 problems)
    
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Easy: Check if array contains duplicates.
        
        Example:
        Input: nums = [1,2,3,1]
        Output: True
        
        Approaches: Set, sorting, or hashmap
        Time: O(n), Space: O(n)
        
        TODO: Use set to detect duplicates efficiently
        """
        pass
    
    def valid_anagram(self, s: str, t: str) -> bool:
        """
        Easy: Check if two strings are anagrams.
        
        Example:
        Input: s = "anagram", t = "nagaram"
        Output: True
        
        Approaches: Sort, frequency count, or character array
        Time: O(n), Space: O(1)
        
        TODO: Compare character frequencies
        """
        pass
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Easy: Find two numbers that add up to target.
        
        Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        
        Approach: Hash map for O(n) solution
        Time: O(n), Space: O(n)
        
        TODO: Use hashmap to store complements
        """
        pass
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Medium: Group strings that are anagrams.
        
        Example:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        Approach: Use sorted string as key
        Time: O(n * k log k), Space: O(n * k)
        
        TODO: Group by sorted character order
        """
        pass
    
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Medium: Find k most frequent elements.
        
        Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        
        Approaches: Heap, bucket sort, or quickselect
        Time: O(n log k), Space: O(n)
        
        TODO: Use heap or bucket sort for efficient solution
        """
        pass
    
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Medium: Product of array except self without division.
        
        Example:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
        Approach: Left and right prefix products
        Time: O(n), Space: O(1) extra
        
        TODO: Calculate left products, then right products in-place
        """
        pass
    
    def valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Medium: Validate Sudoku board.
        
        Approach: Check rows, columns, and 3x3 boxes
        Time: O(1), Space: O(1) (fixed 9x9 board)
        
        TODO: Use sets to track seen numbers in each region
        """
        pass
    
    def encode_decode_strings(self, strs: List[str]) -> List[str]:
        """
        Medium: Encode and decode list of strings.
        
        Design algorithm to encode/decode strings with any characters
        
        Approach: Length-prefixed encoding
        
        TODO: Handle strings with special characters properly
        """
        pass
    
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Medium: Longest consecutive elements sequence.
        
        Example:
        Input: nums = [100,4,200,1,3,2]
        Output: 4 (sequence [1,2,3,4])
        
        Approach: Set for O(n) lookup, only start counting from sequence start
        Time: O(n), Space: O(n)
        
        TODO: Use set and only start sequences from their beginning
        """
        pass
    
    # TWO POINTERS (5 problems)
    
    def valid_palindrome(self, s: str) -> bool:
        """
        Easy: Check if string is palindrome (alphanumeric only).
        
        Example:
        Input: s = "A man, a plan, a canal: Panama"
        Output: True
        
        Approach: Two pointers from ends, skip non-alphanumeric
        Time: O(n), Space: O(1)
        
        TODO: Use two pointers and character filtering
        """
        pass
    
    def two_sum_sorted(self, numbers: List[int], target: int) -> List[int]:
        """
        Medium: Two sum on sorted array.
        
        Example:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2] (1-indexed)
        
        Approach: Two pointers from ends
        Time: O(n), Space: O(1)
        
        TODO: Use left and right pointers moving inward
        """
        pass
    
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Medium: Find all unique triplets that sum to zero.
        
        Example:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        
        Approach: Sort + two pointers for each element
        Time: O(n²), Space: O(1)
        
        TODO: Sort array, then use two pointers for each fixed element
        """
        pass
    
    def container_with_most_water(self, height: List[int]) -> int:
        """
        Medium: Find two lines that contain most water.
        
        Example:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        
        Approach: Two pointers, move pointer with smaller height
        Time: O(n), Space: O(1)
        
        TODO: Use two pointers and greedy movement strategy
        """
        pass
    
    def trapping_rain_water(self, height: List[int]) -> int:
        """
        Hard: Calculate trapped rainwater.
        
        Example:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        
        Approaches: Two pointers, stack, or precompute max heights
        Time: O(n), Space: O(1)
        
        TODO: Use two pointers tracking max heights from both sides
        """
        pass
    
    # SLIDING WINDOW (6 problems)
    
    def best_time_to_buy_sell_stock(self, prices: List[int]) -> int:
        """
        Easy: Maximum profit from buying and selling stock once.
        
        Example:
        Input: prices = [7,1,5,3,6,4]
        Output: 5 (buy at 1, sell at 6)
        
        Approach: Track minimum price and maximum profit
        Time: O(n), Space: O(1)
        
        TODO: Track min price seen so far and max profit
        """
        pass
    
    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Medium: Longest substring without repeating characters.
        
        Example:
        Input: s = "abcabcbb"
        Output: 3 ("abc")
        
        Approach: Sliding window with character frequency
        Time: O(n), Space: O(min(m,n))
        
        TODO: Use sliding window with set or frequency map
        """
        pass
    
    def longest_repeating_character_replacement(self, s: str, k: int) -> int:
        """
        Medium: Longest substring with same character after k replacements.
        
        Example:
        Input: s = "ABAB", k = 2
        Output: 4 (replace both A's or both B's)
        
        Approach: Sliding window tracking max frequency
        Time: O(n), Space: O(1)
        
        TODO: Use sliding window with character frequency count
        """
        pass
    
    def permutation_in_string(self, s1: str, s2: str) -> bool:
        """
        Medium: Check if s1's permutation is substring of s2.
        
        Example:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: True
        
        Approach: Sliding window with frequency matching
        Time: O(n), Space: O(1)
        
        TODO: Use sliding window to match character frequencies
        """
        pass
    
    def minimum_window_substring(self, s: str, t: str) -> str:
        """
        Hard: Minimum window substring containing all characters of t.
        
        Example:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        
        Approach: Sliding window with frequency tracking
        Time: O(|s| + |t|), Space: O(|s| + |t|)
        
        TODO: Use two pointers and frequency maps
        """
        pass
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Hard: Maximum in each sliding window of size k.
        
        Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        
        Approach: Deque to maintain decreasing order
        Time: O(n), Space: O(k)
        
        TODO: Use monotonic deque to track maximums
        """
        pass
    
    # STACK (7 problems)
    
    def valid_parentheses(self, s: str) -> bool:
        """
        Easy: Check if parentheses are valid.
        
        Example:
        Input: s = "()[]{}"
        Output: True
        
        Approach: Stack to match opening/closing brackets
        Time: O(n), Space: O(n)
        
        TODO: Use stack to match bracket pairs
        """
        pass
    
    def min_stack(self):
        """
        Medium: Design stack with min() operation in O(1).
        
        Support push, pop, top, and getMin in O(1) time
        
        Approach: Two stacks or single stack with min tracking
        Space: O(n)
        
        TODO: Design data structure with auxiliary min tracking
        """
        pass
    
    def evaluate_reverse_polish_notation(self, tokens: List[str]) -> int:
        """
        Medium: Evaluate expression in postfix notation.
        
        Example:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9 ((2 + 1) * 3)
        
        Approach: Stack for operands
        Time: O(n), Space: O(n)
        
        TODO: Use stack to evaluate postfix expression
        """
        pass
    
    def generate_parentheses(self, n: int) -> List[str]:
        """
        Medium: Generate all valid parentheses combinations.
        
        Example:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        Approach: Backtracking with validity constraints
        Time: O(4^n / √n), Space: O(4^n / √n)
        
        TODO: Use backtracking with open/close count validation
        """
        pass
    
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        Medium: Days until warmer temperature.
        
        Example:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        
        Approach: Monotonic stack
        Time: O(n), Space: O(n)
        
        TODO: Use stack to find next greater element
        """
        pass
    
    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Medium: Count car fleets reaching target.
        
        Approach: Sort by position, calculate arrival times
        Time: O(n log n), Space: O(n)
        
        TODO: Sort cars by position and simulate movement
        """
        pass
    
    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Hard: Largest rectangle area in histogram.
        
        Example:
        Input: heights = [2,1,5,6,2,3]
        Output: 10
        
        Approach: Monotonic stack
        Time: O(n), Space: O(n)
        
        TODO: Use stack to find boundaries for each bar
        """
        pass