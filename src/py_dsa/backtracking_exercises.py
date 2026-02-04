from typing import List, Set, Optional, Tuple


class BacktrackingExercises:
    """
    Backtracking algorithm exercises with progressive difficulty.
    
    Backtracking is a systematic method for solving problems by trying
    partial solutions and abandoning them ("backtracking") if they
    cannot lead to a valid solution.
    
    Key pattern:
    1. Choose a path/decision
    2. Explore that path recursively
    3. If it doesn't work, undo the choice and try another
    """
    
    # BASIC EXERCISES - Understanding backtracking pattern
    
    def generate_parentheses(self, n: int) -> List[str]:
        """
        Basic: Generate all valid combinations of n pairs of parentheses.
        
        Example:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        TODO: Use backtracking with open/close counters
        """
        pass
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Basic: Generate all possible subsets (power set) of the input set.
        
        Example:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        TODO: Use backtracking to include/exclude each element
        """
        pass
    
    def permutations(self, nums: List[int]) -> List[List[int]]:
        """
        Basic: Generate all permutations of a list of numbers.
        
        Example:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        
        TODO: Use backtracking with visited tracking
        """
        pass
    
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Basic: Find all unique combinations where candidates sum to target.
        
        Example:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        
        TODO: Use backtracking with remaining sum tracking
        """
        pass
    
    # INTERMEDIATE EXERCISES - More complex decision spaces
    
    def subsets_ii(self, nums: List[int]) -> List[List[int]]:
        """
        Intermediate: Generate subsets from array that may contain duplicates.
        
        Example:
        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        
        TODO: Sort first, then skip duplicates during backtracking
        """
        pass
    
    def permutations_ii(self, nums: List[int]) -> List[List[int]]:
        """
        Intermediate: Generate unique permutations from array with duplicates.
        
        Example:
        Input: nums = [1,1,2]
        Output: [[1,1,2],[1,2,1],[2,1,1]]
        
        TODO: Sort and use frequency counting or smart skipping
        """
        pass
    
    def combination_sum_ii(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Intermediate: Each number in candidates can only be used once.
        
        Example:
        Input: candidates = [10,1,2,7,6,1,5], target = 8
        Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
        
        TODO: Sort first, skip duplicates, each number used once
        """
        pass
    
    def letter_combinations_phone(self, digits: str) -> List[str]:
        """
        Intermediate: Generate letter combinations from phone number digits.
        
        Example:
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        
        TODO: Use backtracking with digit-to-letters mapping
        """
        pass
    
    def palindrome_partitioning(self, s: str) -> List[List[str]]:
        """
        Intermediate: Partition string so every substring is a palindrome.
        
        Example:
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        
        TODO: Use backtracking with palindrome checking
        """
        pass
    
    # ADVANCED EXERCISES - Complex constraint satisfaction
    
    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Advanced: Solve Sudoku puzzle in-place.
        
        Example:
        Input: board = 9x9 grid with some numbers filled
        Output: Complete valid Sudoku solution
        
        TODO: Use backtracking with constraint checking
        """
        pass
    
    def n_queens(self, n: int) -> List[List[str]]:
        """
        Advanced: Place n queens on nxn chessboard so none attack each other.
        
        Example:
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        
        TODO: Use backtracking with attack pattern checking
        """
        pass
    
    def word_search(self, board: List[List[str]], word: str) -> bool:
        """
        Advanced: Find if word exists in 2D board of characters.
        
        Example:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: True
        
        TODO: Use backtracking with visited tracking and path exploration
        """
        pass
    
    def word_search_ii(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Advanced: Find all words from word list that exist in board.
        
        Example:
        Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]
        
        TODO: Use Trie + backtracking for efficient multi-word search
        """
        pass
    
    def restore_ip_addresses(self, s: str) -> List[str]:
        """
        Advanced: Generate all possible valid IP addresses from string.
        
        Example:
        Input: s = "25525511135"
        Output: ["255.255.11.135","255.255.111.35"]
        
        TODO: Use backtracking with IP validation constraints
        """
        pass
    
    def expression_add_operators(self, num: str, target: int) -> List[str]:
        """
        Advanced: Add operators (+, -, *) to make expression equal target.
        
        Example:
        Input: num = "232", target = 8
        Output: ["2*3+2","2+3*2"]
        
        TODO: Use backtracking with expression evaluation and precedence
        """
        pass
    
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        """
        Advanced: Remove minimum invalid parentheses to make string valid.
        
        Example:
        Input: s = "()())"
        Output: ["(())","()()"]
        
        TODO: Use backtracking with minimum removal counting
        """
        pass