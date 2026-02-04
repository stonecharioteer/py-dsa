import pytest
from src.py_dsa.dp_exercises import DPExercises


class TestDPExercises:
    """
    Comprehensive tests for Dynamic Programming exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.dp = DPExercises()
    
    # PREREQUISITE TESTS
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_simple_recursion_fibonacci_base_cases(self):
        """Test recursive fibonacci base cases."""
        assert self.dp.simple_recursion_fibonacci(0) == 0
        assert self.dp.simple_recursion_fibonacci(1) == 1
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_simple_recursion_fibonacci_small(self):
        """Test recursive fibonacci with small numbers."""
        assert self.dp.simple_recursion_fibonacci(2) == 1
        assert self.dp.simple_recursion_fibonacci(3) == 2
        assert self.dp.simple_recursion_fibonacci(4) == 3
        assert self.dp.simple_recursion_fibonacci(5) == 5
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_simple_recursion_fibonacci_medium(self):
        """Test recursive fibonacci with medium numbers (will be slow)."""
        assert self.dp.simple_recursion_fibonacci(6) == 8
        assert self.dp.simple_recursion_fibonacci(7) == 13
        assert self.dp.simple_recursion_fibonacci(8) == 21
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_count_recursive_calls_small(self):
        """Test counting recursive calls for small inputs."""
        # This helps students understand the exponential nature of naive recursion
        calls_3 = self.dp.count_recursive_calls(3)
        calls_4 = self.dp.count_recursive_calls(4)
        calls_5 = self.dp.count_recursive_calls(5)
        
        # The number of calls should increase significantly
        assert calls_4 > calls_3
        assert calls_5 > calls_4
        # For fibonacci(5), there should be many recursive calls
        assert calls_5 >= 9  # At least 9 calls for fib(5)
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_memoized_fibonacci_base_cases(self):
        """Test memoized fibonacci base cases."""
        assert self.dp.memoized_fibonacci(0) == 0
        assert self.dp.memoized_fibonacci(1) == 1
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_memoized_fibonacci_medium(self):
        """Test memoized fibonacci with medium numbers (should be fast)."""
        assert self.dp.memoized_fibonacci(10) == 55
        assert self.dp.memoized_fibonacci(15) == 610
        assert self.dp.memoized_fibonacci(20) == 6765
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_memoized_fibonacci_large(self):
        """Test memoized fibonacci with larger numbers."""
        assert self.dp.memoized_fibonacci(30) == 832040
        assert self.dp.memoized_fibonacci(35) == 9227465
    
    # BASIC LEVEL TESTS
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_climbing_stairs_base_cases(self):
        """Test climbing stairs base cases."""
        assert self.dp.climbing_stairs(1) == 1
        assert self.dp.climbing_stairs(2) == 2
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_climbing_stairs_small(self):
        """Test climbing stairs with small inputs."""
        assert self.dp.climbing_stairs(3) == 3
        assert self.dp.climbing_stairs(4) == 5
        assert self.dp.climbing_stairs(5) == 8
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_climbing_stairs_medium(self):
        """Test climbing stairs with medium inputs."""
        assert self.dp.climbing_stairs(10) == 89
        assert self.dp.climbing_stairs(15) == 987
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_house_robber_simple_empty(self):
        """Test house robber with empty array."""
        assert self.dp.house_robber_simple([]) == 0
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_house_robber_simple_single(self):
        """Test house robber with single house."""
        assert self.dp.house_robber_simple([5]) == 5
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_house_robber_simple_two_houses(self):
        """Test house robber with two houses."""
        assert self.dp.house_robber_simple([2, 7]) == 7
        assert self.dp.house_robber_simple([5, 1]) == 5
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_house_robber_simple_multiple(self):
        """Test house robber with multiple houses."""
        assert self.dp.house_robber_simple([1, 2, 3, 1]) == 4
        assert self.dp.house_robber_simple([2, 7, 9, 3, 1]) == 12
        assert self.dp.house_robber_simple([2, 1, 1, 2]) == 4
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_min_cost_climbing_stairs_small(self):
        """Test min cost climbing stairs with small inputs."""
        assert self.dp.min_cost_climbing_stairs([10, 15, 20]) == 15
        assert self.dp.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    
    @pytest.mark.dp
    @pytest.mark.dp_basic
    @pytest.mark.easy
    def test_min_cost_climbing_stairs_edge_cases(self):
        """Test min cost climbing stairs edge cases."""
        assert self.dp.min_cost_climbing_stairs([0, 0]) == 0
        assert self.dp.min_cost_climbing_stairs([1, 2]) == 1
        assert self.dp.min_cost_climbing_stairs([0, 1, 2, 2]) == 2
    
    # INTERMEDIATE LEVEL TESTS
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_unique_paths_base_cases(self):
        """Test unique paths base cases."""
        assert self.dp.unique_paths(1, 1) == 1
        assert self.dp.unique_paths(1, 2) == 1
        assert self.dp.unique_paths(2, 1) == 1
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_unique_paths_small(self):
        """Test unique paths with small grids."""
        assert self.dp.unique_paths(2, 2) == 2
        assert self.dp.unique_paths(3, 2) == 3
        assert self.dp.unique_paths(2, 3) == 3
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_unique_paths_medium(self):
        """Test unique paths with medium grids."""
        assert self.dp.unique_paths(3, 7) == 28
        assert self.dp.unique_paths(7, 3) == 28
        assert self.dp.unique_paths(4, 4) == 20
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_coin_change_impossible(self):
        """Test coin change when impossible."""
        assert self.dp.coin_change([2], 3) == -1
        assert self.dp.coin_change([3, 5], 1) == -1
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_coin_change_base_cases(self):
        """Test coin change base cases."""
        assert self.dp.coin_change([1], 0) == 0
        assert self.dp.coin_change([1], 1) == 1
        assert self.dp.coin_change([1, 2], 2) == 1
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_coin_change_normal(self):
        """Test coin change normal cases."""
        assert self.dp.coin_change([1, 3, 4], 6) == 2
        assert self.dp.coin_change([2, 3, 5], 9) == 3
        assert self.dp.coin_change([1, 2, 5], 11) == 3
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_longest_increasing_subsequence_small(self):
        """Test LIS with small arrays."""
        assert self.dp.longest_increasing_subsequence([1, 3, 2, 4]) == 3
        assert self.dp.longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1
        assert self.dp.longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_longest_increasing_subsequence_medium(self):
        """Test LIS with medium arrays."""
        assert self.dp.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert self.dp.longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_longest_increasing_subsequence_edge_cases(self):
        """Test LIS edge cases."""
        assert self.dp.longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1
        assert self.dp.longest_increasing_subsequence([1]) == 1
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_triangle_min_path_sum_small(self):
        """Test triangle min path sum with small triangles."""
        triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        assert self.dp.triangle_min_path_sum(triangle1) == 11
        
        triangle2 = [[1], [2, 3]]
        assert self.dp.triangle_min_path_sum(triangle2) == 3
    
    @pytest.mark.dp
    @pytest.mark.dp_intermediate
    @pytest.mark.medium
    def test_triangle_min_path_sum_single(self):
        """Test triangle min path sum with single element."""
        assert self.dp.triangle_min_path_sum([[-1]]) == -1
        assert self.dp.triangle_min_path_sum([[5]]) == 5
    
    # ADVANCED LEVEL TESTS
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_knapsack_0_1_empty(self):
        """Test 0/1 knapsack with empty inputs."""
        assert self.dp.knapsack_0_1([], [], 10) == 0
        assert self.dp.knapsack_0_1([1, 2], [1, 2], 0) == 0
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_knapsack_0_1_single_item(self):
        """Test 0/1 knapsack with single item."""
        assert self.dp.knapsack_0_1([5], [10], 4) == 0  # Item too heavy
        assert self.dp.knapsack_0_1([5], [10], 5) == 10  # Exact fit
        assert self.dp.knapsack_0_1([3], [7], 10) == 7  # Item fits with room
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_knapsack_0_1_multiple_items(self):
        """Test 0/1 knapsack with multiple items."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        assert self.dp.knapsack_0_1(weights, values, 7) == 9
        
        weights2 = [2, 3, 4, 5]
        values2 = [3, 4, 5, 6]
        assert self.dp.knapsack_0_1(weights2, values2, 5) == 7
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_edit_distance_empty_strings(self):
        """Test edit distance with empty strings."""
        assert self.dp.edit_distance("", "") == 0
        assert self.dp.edit_distance("abc", "") == 3
        assert self.dp.edit_distance("", "abc") == 3
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_edit_distance_identical_strings(self):
        """Test edit distance with identical strings."""
        assert self.dp.edit_distance("abc", "abc") == 0
        assert self.dp.edit_distance("hello", "hello") == 0
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_edit_distance_different_strings(self):
        """Test edit distance with different strings."""
        assert self.dp.edit_distance("horse", "ros") == 3
        assert self.dp.edit_distance("intention", "execution") == 5
        assert self.dp.edit_distance("abc", "def") == 3
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_longest_common_subsequence_empty(self):
        """Test LCS with empty strings."""
        assert self.dp.longest_common_subsequence("", "") == 0
        assert self.dp.longest_common_subsequence("abc", "") == 0
        assert self.dp.longest_common_subsequence("", "abc") == 0
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_longest_common_subsequence_identical(self):
        """Test LCS with identical strings."""
        assert self.dp.longest_common_subsequence("abc", "abc") == 3
        assert self.dp.longest_common_subsequence("hello", "hello") == 5
    
    @pytest.mark.dp
    @pytest.mark.dp_advanced
    @pytest.mark.hard
    def test_longest_common_subsequence_different(self):
        """Test LCS with different strings."""
        assert self.dp.longest_common_subsequence("abcde", "ace") == 3
        assert self.dp.longest_common_subsequence("abc", "abc") == 3
        assert self.dp.longest_common_subsequence("abc", "def") == 0
        assert self.dp.longest_common_subsequence("AGGTAB", "GXTXAYB") == 4