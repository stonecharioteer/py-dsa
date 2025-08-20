from typing import List


class BitManipulationExercises:
    """
    Bit Manipulation exercises with progressive difficulty.
    
    Bit manipulation is essential for:
    - Optimizing space and time complexity  
    - Low-level programming
    - Cryptography and hashing
    - System design (bit flags, permissions)
    
    Key operations: AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>)
    """
    
    # BASIC EXERCISES - Understanding bit operations
    
    def count_set_bits(self, n: int) -> int:
        """
        Basic: Count number of 1s in binary representation.
        
        Example:
        Input: n = 11 (1011 in binary)
        Output: 3
        
        Approaches:
        1. Brian Kernighan's algorithm: n & (n-1) removes rightmost set bit
        2. Built-in: bin(n).count('1')
        
        Time: O(number of set bits), Space: O(1)
        
        TODO: Implement using bit manipulation tricks
        """
        pass
    
    def is_power_of_two(self, n: int) -> bool:
        """
        Basic: Check if number is power of 2.
        
        Example:
        Input: n = 16
        Output: True (16 = 2^4)
        
        Key insight: Power of 2 has exactly one bit set
        Trick: n > 0 and (n & (n-1)) == 0
        
        Time: O(1), Space: O(1)
        
        TODO: Use the power of 2 bit trick
        """
        pass
    
    def single_number(self, nums: List[int]) -> int:
        """
        Basic: Find number that appears once when others appear twice.
        
        Example:
        Input: nums = [2,2,1]
        Output: 1
        
        Key insight: XOR of identical numbers is 0, XOR with 0 returns the number
        Property: a ^ a = 0, a ^ 0 = a
        
        Time: O(n), Space: O(1)
        
        TODO: Use XOR properties to find the unique number
        """
        pass
    
    def get_bit(self, num: int, i: int) -> int:
        """
        Basic: Get the ith bit of a number.
        
        Example:
        Input: num = 5 (101), i = 1
        Output: 0 (middle bit is 0)
        
        Approach: Shift 1 to position i, then AND with num
        
        TODO: Implement using bit shifting and AND
        """
        pass
    
    def set_bit(self, num: int, i: int) -> int:
        """
        Basic: Set the ith bit to 1.
        
        Example:
        Input: num = 5 (101), i = 1
        Output: 7 (111)
        
        Approach: OR with (1 << i)
        
        TODO: Implement using bit shifting and OR
        """
        pass
    
    def clear_bit(self, num: int, i: int) -> int:
        """
        Basic: Clear the ith bit (set to 0).
        
        Example:
        Input: num = 7 (111), i = 1
        Output: 5 (101)
        
        Approach: AND with NOT of (1 << i)
        
        TODO: Implement using bit shifting, NOT, and AND
        """
        pass
    
    # INTERMEDIATE EXERCISES - XOR patterns and bit tricks
    
    def single_number_2(self, nums: List[int]) -> int:
        """
        Medium: Find number appearing once when others appear 3 times.
        
        Example:
        Input: nums = [2,2,3,2]
        Output: 3
        
        Approach: Use two variables to track bits appearing 1 or 2 times
        Complex XOR state machine
        
        Time: O(n), Space: O(1)
        
        TODO: Implement 3-state bit counting using two variables
        """
        pass
    
    def single_number_3(self, nums: List[int]) -> List[int]:
        """
        Medium: Find two numbers appearing once when others appear twice.
        
        Example:
        Input: nums = [1,2,1,3,2,5]
        Output: [3,5]
        
        Approach: XOR all numbers, then partition by differing bit
        
        Time: O(n), Space: O(1)
        
        TODO: Use XOR and bit partitioning to separate the two numbers
        """
        pass
    
    def missing_number(self, nums: List[int]) -> int:
        """
        Easy: Find missing number in range [0,n].
        
        Example:
        Input: nums = [3,0,1]
        Output: 2
        
        Approaches:
        1. XOR all numbers and indices
        2. Sum formula: n*(n+1)/2 - sum(nums)
        
        Time: O(n), Space: O(1)
        
        TODO: Use XOR or mathematical approach
        """
        pass
    
    def find_duplicate(self, nums: List[int]) -> int:
        """
        Medium: Find duplicate in array where nums[i] is in [1,n].
        
        Example:
        Input: nums = [1,3,4,2,2]
        Output: 2
        
        Bit manipulation approach: Count bits at each position
        
        Time: O(n log n), Space: O(1)
        
        TODO: Count bits or use Floyd's cycle detection
        """
        pass
    
    # ADVANCED EXERCISES - Complex bit manipulation
    
    def reverse_bits(self, n: int) -> int:
        """
        Easy: Reverse bits of a 32-bit unsigned integer.
        
        Example:
        Input: n = 43261596 (00000010100101000001111010011100)
        Output: 964176192 (00111001011110000010100101000000)
        
        Approaches:
        1. Process bit by bit
        2. Divide and conquer (swap chunks)
        
        Time: O(1), Space: O(1)
        
        TODO: Reverse bits using bit operations
        """
        pass
    
    def number_of_1_bits(self, n: int) -> int:
        """
        Easy: Count 1-bits in unsigned integer (Hamming weight).
        
        Example:
        Input: n = 11 (00000000000000000000000000001011)
        Output: 3
        
        Optimized: n & (n-1) eliminates rightmost 1-bit
        
        TODO: Use Brian Kernighan's algorithm
        """
        pass
    
    def bitwise_and_range(self, left: int, right: int) -> int:
        """
        Medium: Bitwise AND of all numbers in range [left, right].
        
        Example:
        Input: left = 5, right = 7
        Output: 4 (5 & 6 & 7 = 4)
        
        Key insight: Find common prefix of left and right
        
        Time: O(log n), Space: O(1)
        
        TODO: Find longest common binary prefix
        """
        pass
    
    def maximum_xor(self, nums: List[int]) -> int:
        """
        Medium: Find maximum XOR of any two numbers in array.
        
        Example:
        Input: nums = [3,10,5,25,2,8]
        Output: 28 (5 XOR 25 = 28)
        
        Approach: Build trie of binary representations, find max XOR
        
        Time: O(n * 32), Space: O(n * 32)
        
        TODO: Use bit trie or greedy bit-by-bit approach
        """
        pass
    
    def counting_bits(self, n: int) -> List[int]:
        """
        Easy: Count bits for all numbers from 0 to n.
        
        Example:
        Input: n = 5
        Output: [0,1,1,2,1,2] (bits in 0,1,2,3,4,5)
        
        DP relation: dp[i] = dp[i >> 1] + (i & 1)
        
        Time: O(n), Space: O(1) extra
        
        TODO: Use dynamic programming with bit operations
        """
        pass
    
    # BIT MANIPULATION PATTERNS
    
    def gray_code(self, n: int) -> List[int]:
        """
        Medium: Generate n-bit Gray code sequence.
        
        Example:
        Input: n = 2
        Output: [0,1,3,2] (00,01,11,10)
        
        Pattern: G(n) = G(n-1) + reverse(G(n-1)) with MSB set
        
        Time: O(2^n), Space: O(1) extra
        
        TODO: Use recursive Gray code generation
        """
        pass
    
    def sum_without_arithmetic(self, a: int, b: int) -> int:
        """
        Medium: Add two integers without using +/- operators.
        
        Example:
        Input: a = 1, b = 2
        Output: 3
        
        Approach: XOR for sum, AND + shift for carry
        
        Time: O(1), Space: O(1)
        
        TODO: Use XOR and carry propagation
        """
        pass
    
    def divide_without_division(self, dividend: int, divisor: int) -> int:
        """
        Medium: Divide without using multiplication, division, mod.
        
        Example:
        Input: dividend = 10, divisor = 3
        Output: 3
        
        Approach: Bit shifting to multiply divisor by powers of 2
        
        Time: O(log n), Space: O(1)
        
        TODO: Use bit shifting and subtraction
        """
        pass