import pytest
from src.py_dsa.stack_queue_exercises import StackQueueExercises


class TestStackQueueExercises:
    """
    Tests for stack and queue data structure exercises.
    Essential for understanding LIFO and FIFO principles and their applications.
    """
    
    def setup_method(self):
        self.stack_queue = StackQueueExercises()
    
    # STACK OPERATION TESTS
    
    @pytest.mark.stack_queue
    @pytest.mark.easy
    def test_valid_parentheses_basic(self):
        """Test valid parentheses with basic cases."""
        assert self.stack_queue.valid_parentheses("()") == True
        assert self.stack_queue.valid_parentheses("()[]{}") == True
        assert self.stack_queue.valid_parentheses("(]") == False
        assert self.stack_queue.valid_parentheses("([)]") == False
        assert self.stack_queue.valid_parentheses("{[]}") == True
    
    @pytest.mark.stack_queue
    @pytest.mark.easy
    def test_valid_parentheses_edge_cases(self):
        """Test valid parentheses edge cases."""
        assert self.stack_queue.valid_parentheses("") == True
        assert self.stack_queue.valid_parentheses("(") == False
        assert self.stack_queue.valid_parentheses(")") == False
        assert self.stack_queue.valid_parentheses("((") == False
        assert self.stack_queue.valid_parentheses("))") == False
    
    @pytest.mark.stack_queue
    @pytest.mark.medium
    def test_daily_temperatures_basic(self):
        """Test daily temperatures basic cases."""
        assert self.stack_queue.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
        assert self.stack_queue.daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
        assert self.stack_queue.daily_temperatures([30, 60, 90]) == [1, 1, 0]
    
    @pytest.mark.stack_queue
    @pytest.mark.medium
    def test_daily_temperatures_edge_cases(self):
        """Test daily temperatures edge cases."""
        assert self.stack_queue.daily_temperatures([100, 90, 80, 70]) == [0, 0, 0, 0]
        assert self.stack_queue.daily_temperatures([30]) == [0]
        assert self.stack_queue.daily_temperatures([30, 30, 30]) == [0, 0, 0]
    
    # QUEUE OPERATION TESTS
    
    @pytest.mark.stack_queue
    @pytest.mark.medium
    def test_sliding_window_maximum_basic(self):
        """Test sliding window maximum basic cases."""
        assert self.stack_queue.sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
        assert self.stack_queue.sliding_window_maximum([1], 1) == [1]
        assert self.stack_queue.sliding_window_maximum([1, -1], 1) == [1, -1]
    
    @pytest.mark.stack_queue
    @pytest.mark.medium
    def test_sliding_window_maximum_edge_cases(self):
        """Test sliding window maximum edge cases."""
        assert self.stack_queue.sliding_window_maximum([9, 11], 2) == [11]
        assert self.stack_queue.sliding_window_maximum([4, -2], 2) == [4]
        assert self.stack_queue.sliding_window_maximum([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]