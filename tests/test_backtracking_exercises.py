import pytest
from src.py_dsa.backtracking_exercises import BacktrackingExercises


class TestBacktrackingExercises:
    """
    Tests for backtracking technique exercises with progressive difficulty.
    """
    
    def setup_method(self):
        self.backtracking = BacktrackingExercises()
    
    # BASIC LEVEL TESTS
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_basic
    @pytest.mark.easy
    def test_generate_parentheses_basic(self):
        """Test generating valid parentheses combinations."""
        result1 = self.backtracking.generate_parentheses(3)
        expected1 = ["((()))","(()())","(())()","()(())","()()()"]
        assert sorted(result1) == sorted(expected1)
        
        result2 = self.backtracking.generate_parentheses(1)
        assert result2 == ["()"]
        
        result3 = self.backtracking.generate_parentheses(2)
        expected3 = ["(())","()()"]
        assert sorted(result3) == sorted(expected3)
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_basic
    @pytest.mark.easy
    def test_subsets_basic(self):
        """Test generating all subsets (power set)."""
        result1 = self.backtracking.subsets([1,2,3])
        expected1 = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        assert len(result1) == len(expected1)
        for subset in expected1:
            assert subset in result1 or sorted(subset) in [sorted(x) for x in result1]
        
        result2 = self.backtracking.subsets([0])
        expected2 = [[],[0]]
        assert sorted([sorted(x) for x in result2]) == sorted([sorted(x) for x in expected2])
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_basic
    @pytest.mark.easy
    def test_permutations_basic(self):
        """Test generating all permutations."""
        result1 = self.backtracking.permutations([1,2,3])
        expected1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert len(result1) == len(expected1)
        for perm in expected1:
            assert perm in result1
        
        result2 = self.backtracking.permutations([0,1])
        expected2 = [[0,1],[1,0]]
        assert sorted(result2) == sorted(expected2)
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_basic
    @pytest.mark.easy
    def test_combination_sum_basic(self):
        """Test combination sum problem."""
        result1 = self.backtracking.combination_sum([2,3,6,7], 7)
        expected1 = [[2,2,3],[7]]
        assert len(result1) == len(expected1)
        for combo in expected1:
            assert sorted(combo) in [sorted(x) for x in result1]
        
        result2 = self.backtracking.combination_sum([2,3,5], 8)
        expected2 = [[2,2,2,2],[2,3,3],[3,5]]
        assert len(result2) == len(expected2)
    
    # INTERMEDIATE LEVEL TESTS
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_intermediate
    @pytest.mark.medium
    def test_subsets_ii_basic(self):
        """Test generating subsets with duplicates."""
        result1 = self.backtracking.subsets_ii([1,2,2])
        expected1 = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        assert len(result1) == len(expected1)
        for subset in expected1:
            assert sorted(subset) in [sorted(x) for x in result1]
        
        result2 = self.backtracking.subsets_ii([4,4,4,1,4])
        # Should not have duplicate subsets
        unique_subsets = []
        for subset in result2:
            sorted_subset = sorted(subset)
            if sorted_subset not in unique_subsets:
                unique_subsets.append(sorted_subset)
        assert len(unique_subsets) == len(result2)
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_intermediate
    @pytest.mark.medium
    def test_permutations_ii_basic(self):
        """Test generating unique permutations with duplicates."""
        result1 = self.backtracking.permutations_ii([1,1,2])
        expected1 = [[1,1,2],[1,2,1],[2,1,1]]
        assert len(result1) == len(expected1)
        for perm in expected1:
            assert perm in result1
        
        result2 = self.backtracking.permutations_ii([1,2,1,1])
        # Should not have duplicate permutations
        unique_perms = []
        for perm in result2:
            if perm not in unique_perms:
                unique_perms.append(perm)
        assert len(unique_perms) == len(result2)
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_intermediate
    @pytest.mark.medium
    def test_letter_combinations_phone_basic(self):
        """Test letter combinations from phone digits."""
        result1 = self.backtracking.letter_combinations_phone("23")
        expected1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert sorted(result1) == sorted(expected1)
        
        result2 = self.backtracking.letter_combinations_phone("")
        assert result2 == []
        
        result3 = self.backtracking.letter_combinations_phone("2")
        expected3 = ["a","b","c"]
        assert sorted(result3) == sorted(expected3)
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_intermediate
    @pytest.mark.medium
    def test_palindrome_partitioning_basic(self):
        """Test palindrome partitioning."""
        result1 = self.backtracking.palindrome_partitioning("aab")
        expected1 = [["a","a","b"],["aa","b"]]
        assert len(result1) == len(expected1)
        for partition in expected1:
            assert partition in result1
        
        result2 = self.backtracking.palindrome_partitioning("raceacar")
        # Should include ["r","a","c","e","a","c","a","r"] and ["r","a","cec","a","r"] and ["raceacar"]
        assert len(result2) >= 3
    
    # ADVANCED LEVEL TESTS
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_advanced
    @pytest.mark.hard
    def test_solve_sudoku_basic(self):
        """Test Sudoku solver."""
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        
        self.backtracking.solve_sudoku(board)
        
        # Verify solution is valid (basic check)
        # Check that no empty cells remain
        for row in board:
            for cell in row:
                assert cell != "."
        
        # Check that each row has digits 1-9
        for row in board:
            assert sorted(row) == ["1","2","3","4","5","6","7","8","9"]
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_advanced
    @pytest.mark.hard
    def test_n_queens_basic(self):
        """Test N-Queens problem."""
        result1 = self.backtracking.n_queens(4)
        expected_count = 2  # There are exactly 2 solutions for 4-queens
        assert len(result1) == expected_count
        
        # Verify each solution has exactly one queen per row and column
        for solution in result1:
            assert len(solution) == 4
            queens = []
            for i, row in enumerate(solution):
                queen_col = row.index('Q')
                queens.append((i, queen_col))
            
            # Check no two queens are in same row, column, or diagonal
            for i, (r1, c1) in enumerate(queens):
                for j, (r2, c2) in enumerate(queens):
                    if i != j:
                        assert r1 != r2  # Different rows
                        assert c1 != c2  # Different columns
                        assert abs(r1 - r2) != abs(c1 - c2)  # Different diagonals
        
        result2 = self.backtracking.n_queens(1)
        assert len(result2) == 1
        assert result2[0] == ["Q"]
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_advanced
    @pytest.mark.hard
    def test_word_search_basic(self):
        """Test word search in 2D board."""
        board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        assert self.backtracking.word_search(board1, "ABCCED") == True
        assert self.backtracking.word_search(board1, "SEE") == True
        assert self.backtracking.word_search(board1, "ABCB") == False
        
        board2 = [["A","B"],["C","D"]]
        assert self.backtracking.word_search(board2, "ABCD") == False
        assert self.backtracking.word_search(board2, "ACDB") == True
    
    @pytest.mark.backtracking
    @pytest.mark.backtracking_advanced
    @pytest.mark.hard
    def test_restore_ip_addresses_basic(self):
        """Test restoring IP addresses."""
        result1 = self.backtracking.restore_ip_addresses("25525511135")
        expected1 = ["255.255.11.135","255.255.111.35"]
        assert sorted(result1) == sorted(expected1)
        
        result2 = self.backtracking.restore_ip_addresses("0000")
        expected2 = ["0.0.0.0"]
        assert result2 == expected2
        
        result3 = self.backtracking.restore_ip_addresses("101023")
        # Should include valid IPs like "1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"
        assert len(result3) >= 3