from typing import List, Dict, Optional, Tuple


class DPExercises:
    """
    Dynamic Programming (DP) exercises with progressive difficulty.
    
    DP is an optimization technique that solves complex problems by breaking them
    down into simpler subproblems and storing results to avoid redundant calculations.
    """
    
    # BASIC EXERCISES - Understanding DP fundamentals
    # NOTE: Complete fundamentals_exercises.py before attempting these!
    
    def climbing_stairs(self, n: int) -> int:
        """
        Basic: Count ways to climb n stairs (can take 1 or 2 steps at a time).
        
        Example:
        Input: n = 3
        Output: 3 (ways: 1+1+1, 1+2, 2+1)
        
        TODO: Solve using bottom-up DP approach
        """
        pass
    
    def house_robber_simple(self, nums: List[int]) -> int:
        """
        Basic: Rob houses in a line without robbing adjacent houses.
        
        Example:
        Input: nums = [2,7,9,3,1]
        Output: 12 (rob houses with values 2, 9, 1)
        
        TODO: Use DP to find maximum money that can be robbed
        """
        pass
    
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        """
        Basic: Find minimum cost to reach the top of stairs.
        
        Example:
        Input: cost = [10,15,20]
        Output: 15 (start at index 1, cost 15, one step to top)
        
        TODO: Use DP to find minimum cost path
        """
        pass
    
    # INTERMEDIATE EXERCISES - 2D DP and more complex problems
    
    def unique_paths(self, m: int, n: int) -> int:
        """
        Intermediate: Count unique paths in m x n grid (can only move right or down).
        
        Example:
        Input: m = 3, n = 7
        Output: 28
        
        TODO: Use 2D DP to count all possible paths
        """
        pass
    
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Intermediate: Find minimum coins needed to make amount.
        
        Example:
        Input: coins = [1,3,4], amount = 6
        Output: 2 (6 = 3 + 3)
        
        TODO: Use DP to find minimum coins needed
        """
        pass
    
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        """
        Intermediate: Find length of longest increasing subsequence.
        
        Example:
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4 (subsequence: [2,3,7,18])
        
        TODO: Use DP to find LIS length
        """
        pass
    
    def triangle_min_path_sum(self, triangle: List[List[int]]) -> int:
        """
        Intermediate: Find minimum path sum from top to bottom of triangle.
        
        Example:
        Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        Output: 11 (path: 2 + 3 + 5 + 1)
        
        TODO: Use DP to find minimum path sum
        """
        pass
    
    # ADVANCED EXERCISES - Complex DP patterns
    
    def knapsack_0_1(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        Advanced: Solve 0/1 Knapsack problem.
        
        Example:
        Input: weights = [1,3,4,5], values = [1,4,5,7], capacity = 7
        Output: 9 (take items with weights 3,4 and values 4,5)
        
        TODO: Use 2D DP to solve knapsack problem
        """
        pass
    
    def edit_distance(self, word1: str, word2: str) -> int:
        """
        Advanced: Find minimum edit distance between two strings.
        
        Example:
        Input: word1 = "horse", word2 = "ros"
        Output: 3 (horse -> rorse -> rose -> ros)
        
        TODO: Use 2D DP to find minimum edit operations
        """
        pass
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Advanced: Find length of longest common subsequence.
        
        Example:
        Input: text1 = "abcde", text2 = "ace"
        Output: 3 (LCS is "ace")
        
        TODO: Use 2D DP to find LCS length
        """
        pass