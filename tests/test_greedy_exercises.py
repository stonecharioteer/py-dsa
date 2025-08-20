import pytest
from src.py_dsa.greedy_exercises import GreedyExercises


class TestGreedyExercises:
    """
    Tests for greedy algorithm exercises covering optimization, scheduling, and pathfinding problems.
    Essential for understanding locally optimal choice strategies.
    """
    
    def setup_method(self):
        self.greedy = GreedyExercises()
    
    # BASIC GREEDY TESTS
    
    @pytest.mark.greedy
    @pytest.mark.easy
    def test_coin_change_greedy_basic(self):
        """Test greedy coin change with standard coins."""
        assert self.greedy.coin_change_greedy([1, 5, 10, 25], 30) == 2  # 25 + 5
        assert self.greedy.coin_change_greedy([1, 5, 10, 25], 18) == 4  # 10 + 5 + 1 + 1 + 1
        assert self.greedy.coin_change_greedy([1, 5, 10, 25], 0) == 0
    
    @pytest.mark.greedy
    @pytest.mark.easy
    def test_coin_change_greedy_edge_cases(self):
        """Test greedy coin change edge cases."""
        assert self.greedy.coin_change_greedy([1], 5) == 5
        assert self.greedy.coin_change_greedy([5], 1) == -1  # Cannot make change
        assert self.greedy.coin_change_greedy([1, 5, 10], 11) == 2  # 10 + 1
    
    @pytest.mark.greedy
    @pytest.mark.easy
    def test_fractional_knapsack_basic(self):
        """Test fractional knapsack basic cases."""
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = self.greedy.fractional_knapsack(weights, values, capacity)
        assert result == 240.0  # Take items 2 (120), 1 (100), partial item 0 (20)
    
    @pytest.mark.greedy
    @pytest.mark.easy
    def test_fractional_knapsack_edge_cases(self):
        """Test fractional knapsack edge cases."""
        # Can take all items
        result = self.greedy.fractional_knapsack([10, 20], [60, 100], 50)
        assert result == 160.0
        
        # Can take no items
        result = self.greedy.fractional_knapsack([50, 60], [60, 100], 40)
        assert result == 0.0
    
    @pytest.mark.greedy
    @pytest.mark.easy
    def test_activity_selection_basic(self):
        """Test basic activity selection."""
        start = [1, 3, 0, 5, 8, 5]
        end = [2, 4, 6, 7, 9, 9]
        result = self.greedy.activity_selection(start, end)
        
        # Should select non-overlapping activities
        assert len(result) >= 3  # At least 3 activities can be selected
        # Verify selected activities don't overlap
        selected_intervals = [(start[i], end[i]) for i in result]
        for i in range(len(selected_intervals) - 1):
            assert selected_intervals[i][1] <= selected_intervals[i + 1][0]
    
    # INTERVAL TESTS
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_minimum_meeting_rooms_basic(self):
        """Test minimum meeting rooms calculation."""
        intervals = [[0, 30], [5, 10], [15, 20]]
        assert self.greedy.minimum_meeting_rooms(intervals) == 2
        
        intervals = [[7, 10], [2, 4]]
        assert self.greedy.minimum_meeting_rooms(intervals) == 1
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_minimum_meeting_rooms_edge_cases(self):
        """Test meeting rooms edge cases."""
        assert self.greedy.minimum_meeting_rooms([]) == 0
        assert self.greedy.minimum_meeting_rooms([[1, 2]]) == 1
        assert self.greedy.minimum_meeting_rooms([[1, 2], [3, 4]]) == 1
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_merge_intervals_basic(self):
        """Test interval merging."""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.greedy.merge_intervals(intervals)
        expected = [[1, 6], [8, 10], [15, 18]]
        assert result == expected
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_merge_intervals_edge_cases(self):
        """Test interval merging edge cases."""
        # Single interval
        assert self.greedy.merge_intervals([[1, 4]]) == [[1, 4]]
        
        # No overlaps
        assert self.greedy.merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
        
        # All merge into one
        assert self.greedy.merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_non_overlapping_intervals_basic(self):
        """Test minimum intervals to remove."""
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        assert self.greedy.non_overlapping_intervals(intervals) == 1  # Remove [1,3]
        
        intervals = [[1, 2], [1, 2], [1, 2]]
        assert self.greedy.non_overlapping_intervals(intervals) == 2
    
    # OPTIMIZATION TESTS
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_jump_game_basic(self):
        """Test jump game reachability."""
        assert self.greedy.jump_game([2, 3, 1, 1, 4]) == True
        assert self.greedy.jump_game([3, 2, 1, 0, 4]) == False
        assert self.greedy.jump_game([0]) == True
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_jump_game_edge_cases(self):
        """Test jump game edge cases."""
        assert self.greedy.jump_game([1]) == True
        assert self.greedy.jump_game([0, 1]) == False
        assert self.greedy.jump_game([2, 0, 0]) == True
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_jump_game_2_basic(self):
        """Test minimum jumps to reach end."""
        assert self.greedy.jump_game_2([2, 3, 1, 1, 4]) == 2
        assert self.greedy.jump_game_2([2, 3, 0, 1, 4]) == 2
        assert self.greedy.jump_game_2([1, 1, 1, 1]) == 3
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_gas_station_basic(self):
        """Test gas station circular tour."""
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        assert self.greedy.gas_station(gas, cost) == 3
        
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        assert self.greedy.gas_station(gas, cost) == -1
    
    @pytest.mark.greedy
    @pytest.mark.hard
    def test_candy_distribution_basic(self):
        """Test candy distribution problem."""
        assert self.greedy.candy_distribution([1, 0, 2]) == 5  # [2,1,2]
        assert self.greedy.candy_distribution([1, 2, 2]) == 4  # [1,2,1]
        assert self.greedy.candy_distribution([1, 3, 2, 2, 1]) == 7
    
    # ADVANCED TESTS
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_partition_labels_basic(self):
        """Test string partitioning."""
        result = self.greedy.partition_labels("ababcbacadefegdehijhklij")
        assert result == [9, 7, 8]
        
        result = self.greedy.partition_labels("eccbbbbdec")
        assert result == [10]
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_minimum_cost_connect_sticks_basic(self):
        """Test minimum cost to connect sticks."""
        assert self.greedy.minimum_cost_to_connect_sticks([2, 4, 3]) == 14
        assert self.greedy.minimum_cost_to_connect_sticks([1, 8, 3, 5]) == 30
        assert self.greedy.minimum_cost_to_connect_sticks([5]) == 0
    
    @pytest.mark.greedy
    @pytest.mark.medium
    def test_task_scheduler_basic(self):
        """Test task scheduler with cooling."""
        tasks = ["A", "A", "A", "B", "B", "B"]
        assert self.greedy.task_scheduler(tasks, 2) == 8
        
        tasks = ["A", "A", "A", "B", "B", "B"]
        assert self.greedy.task_scheduler(tasks, 0) == 6
        
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        assert self.greedy.task_scheduler(tasks, 2) == 16