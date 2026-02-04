import pytest
from src.py_dsa.fundamentals_exercises import FundamentalsExercises, TreeNode, ListNode, SimpleQueue


def skip_if_not_implemented(result, test_name="Test"):
    """Skip test if function returns None (not implemented yet)."""
    if result is None:
        pytest.skip(f"{test_name} not implemented yet - function returns None")


class TestFundamentalsExercises:
    """
    Tests for fundamental DSA exercises that should be completed before BFS and DP.
    These exercises build fundamental understanding of data structures and algorithms.
    """
    
    def setup_method(self):
        self.fundamentals = FundamentalsExercises()
    
    # Helper methods to create test trees
    def create_simple_tree(self) -> TreeNode:
        """Creates tree: [1,2,3,4,5]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root
    
    def create_unbalanced_tree(self) -> TreeNode:
        """Creates tree: [3,9,20,null,null,15,7]"""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root
    
    # QUEUE EXERCISE TESTS
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_implement_queue_with_list(self):
        """Test queue implementation with basic operations."""
        queue = self.fundamentals.implement_queue_with_list()
        
        # Test that a SimpleQueue is returned
        assert isinstance(queue, SimpleQueue)
        
        # These tests will pass when student implements the methods
        # For now, they test the structure is in place
        assert hasattr(queue, 'enqueue')
        assert hasattr(queue, 'dequeue')
        assert hasattr(queue, 'is_empty')
        assert hasattr(queue, 'size')
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_implement_queue_with_deque(self):
        """Test understanding of deque usage."""
        # This is more of a practice exercise
        result = self.fundamentals.implement_queue_with_deque()
        assert result is None  # Method should practice deque operations
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_queue_simulation_empty(self):
        """Test queue simulation with no operations."""
        result = self.fundamentals.queue_simulation([])
        assert result == []
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_queue_simulation_basic(self):
        """Test queue simulation with basic operations."""
        operations = ["enqueue 1", "enqueue 2", "dequeue", "enqueue 3", "dequeue"]
        result = self.fundamentals.queue_simulation(operations)
        assert result == [1, 2]
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_queue_simulation_complex(self):
        """Test queue simulation with more complex operations."""
        operations = ["enqueue 5", "dequeue", "enqueue 10", "enqueue 15", "dequeue", "dequeue"]
        result = self.fundamentals.queue_simulation(operations)
        assert result == [5, 10, 15]
    
    # TREE EXERCISE TESTS
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_tree_traversal_iterative_empty(self):
        """Test iterative traversal with empty tree."""
        result = self.fundamentals.tree_traversal_iterative(None)
        skip_if_not_implemented(result, "tree_traversal_iterative")
        assert result == []
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_tree_traversal_iterative_single(self):
        """Test iterative traversal with single node."""
        root = TreeNode(42)
        result = self.fundamentals.tree_traversal_iterative(root)
        assert result == [42]
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_tree_traversal_iterative_multiple(self):
        """Test iterative traversal with multiple nodes."""
        root = self.create_simple_tree()
        result = self.fundamentals.tree_traversal_iterative(root)
        # Should be breadth-first order: [1,2,3,4,5]
        assert result == [1, 2, 3, 4, 5]
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_tree_traversal_iterative_unbalanced(self):
        """Test iterative traversal with unbalanced tree."""
        root = self.create_unbalanced_tree()
        result = self.fundamentals.tree_traversal_iterative(root)
        # Should be breadth-first order: [3,9,20,15,7]
        assert result == [3, 9, 20, 15, 7]
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_count_tree_nodes_empty(self):
        """Test counting nodes in empty tree."""
        result = self.fundamentals.count_tree_nodes(None)
        assert result == 0
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_count_tree_nodes_single(self):
        """Test counting nodes in single node tree."""
        root = TreeNode(1)
        result = self.fundamentals.count_tree_nodes(root)
        assert result == 1
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_count_tree_nodes_multiple(self):
        """Test counting nodes in multiple node tree."""
        root = self.create_simple_tree()
        result = self.fundamentals.count_tree_nodes(root)
        assert result == 5
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_find_tree_height_empty(self):
        """Test finding height of empty tree."""
        result = self.fundamentals.find_tree_height(None)
        assert result == 0
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_find_tree_height_single(self):
        """Test finding height of single node tree."""
        root = TreeNode(1)
        result = self.fundamentals.find_tree_height(root)
        assert result == 1
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_find_tree_height_multiple(self):
        """Test finding height of multi-level tree."""
        root = self.create_unbalanced_tree()
        result = self.fundamentals.find_tree_height(root)
        assert result == 3
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_create_tree_from_list_empty(self):
        """Test creating tree from empty list."""
        result = self.fundamentals.create_tree_from_list([])
        assert result is None
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_create_tree_from_list_single(self):
        """Test creating tree from single element."""
        result = self.fundamentals.create_tree_from_list([1])
        assert result.val == 1
        assert result.left is None
        assert result.right is None
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_create_tree_from_list_complete(self):
        """Test creating tree from complete binary tree list."""
        values = [1, 2, 3, 4, 5]
        result = self.fundamentals.create_tree_from_list(values)
        assert result.val == 1
        assert result.left.val == 2
        assert result.right.val == 3
        assert result.left.left.val == 4
        assert result.left.right.val == 5
    
    # RECURSION EXERCISE TESTS
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_simple_recursion_factorial_base_case(self):
        """Test factorial base cases."""
        assert self.fundamentals.simple_recursion_factorial(0) == 1
        assert self.fundamentals.simple_recursion_factorial(1) == 1
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_simple_recursion_factorial_small(self):
        """Test factorial with small numbers."""
        assert self.fundamentals.simple_recursion_factorial(3) == 6
        assert self.fundamentals.simple_recursion_factorial(4) == 24
        assert self.fundamentals.simple_recursion_factorial(5) == 120
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_simple_recursion_fibonacci_base_cases(self):
        """Test fibonacci base cases."""
        assert self.fundamentals.simple_recursion_fibonacci(0) == 0
        assert self.fundamentals.simple_recursion_fibonacci(1) == 1
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_simple_recursion_fibonacci_small(self):
        """Test fibonacci with small numbers."""
        assert self.fundamentals.simple_recursion_fibonacci(2) == 1
        assert self.fundamentals.simple_recursion_fibonacci(3) == 2
        assert self.fundamentals.simple_recursion_fibonacci(4) == 3
        assert self.fundamentals.simple_recursion_fibonacci(5) == 5
        assert self.fundamentals.simple_recursion_fibonacci(6) == 8
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_count_recursive_calls_understanding(self):
        """Test understanding of recursive call counting."""
        # For fibonacci, the number of calls grows exponentially
        calls_3 = self.fundamentals.count_recursive_calls(3)
        calls_4 = self.fundamentals.count_recursive_calls(4)
        calls_5 = self.fundamentals.count_recursive_calls(5)
        
        # Each should be greater than the previous
        assert calls_4 > calls_3
        assert calls_5 > calls_4
        # For fibonacci(5), there should be at least 9 calls
        assert calls_5 >= 9
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_understand_call_stack_small(self):
        """Test understanding of call stack tracing."""
        result = self.fundamentals.understand_call_stack(3)
        # Should trace the sequence of calls
        assert result == [3, 2, 1, 0]
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_understand_call_stack_larger(self):
        """Test call stack tracing with larger input."""
        result = self.fundamentals.understand_call_stack(5)
        assert result == [5, 4, 3, 2, 1, 0]
    
    # MEMOIZATION EXERCISE TESTS
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_memoized_fibonacci_base_cases(self):
        """Test memoized fibonacci base cases."""
        assert self.fundamentals.memoized_fibonacci(0) == 0
        assert self.fundamentals.memoized_fibonacci(1) == 1
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_memoized_fibonacci_medium(self):
        """Test memoized fibonacci with medium numbers."""
        assert self.fundamentals.memoized_fibonacci(10) == 55
        assert self.fundamentals.memoized_fibonacci(15) == 610
        assert self.fundamentals.memoized_fibonacci(20) == 6765
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_memoized_fibonacci_large(self):
        """Test memoized fibonacci with large numbers (should be fast)."""
        assert self.fundamentals.memoized_fibonacci(40) == 102334155
        assert self.fundamentals.memoized_fibonacci(50) == 12586269025
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_compare_fibonacci_performance(self):
        """Test fibonacci performance comparison."""
        result = self.fundamentals.compare_fibonacci_performance(10)
        
        # Should return a dictionary with timing information
        assert isinstance(result, dict)
        assert 'recursive_time' in result
        assert 'memoized_time' in result
        
        # Memoized should be faster (or at least not slower)
        assert result['memoized_time'] <= result['recursive_time']
    
    # ARRAY EXERCISE TESTS
    
    @pytest.mark.fundamentals
    @pytest.mark.easy
    def test_two_sum_brute_force_basic(self):
        """Test two sum brute force basic cases."""
        assert self.fundamentals.two_sum_brute_force([2, 7, 11, 15], 9) == [0, 1]
        assert self.fundamentals.two_sum_brute_force([3, 2, 4], 6) == [1, 2]
        assert self.fundamentals.two_sum_brute_force([3, 3], 6) == [0, 1]
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_two_sum_hash_map_basic(self):
        """Test two sum hash map basic cases."""
        assert self.fundamentals.two_sum_hash_map([2, 7, 11, 15], 9) == [0, 1]
        assert self.fundamentals.two_sum_hash_map([3, 2, 4], 6) == [1, 2]
        assert self.fundamentals.two_sum_hash_map([3, 3], 6) == [0, 1]
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_max_subarray_sum_brute_force_basic(self):
        """Test max subarray sum brute force."""
        assert self.fundamentals.max_subarray_sum_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert self.fundamentals.max_subarray_sum_brute_force([1]) == 1
        assert self.fundamentals.max_subarray_sum_brute_force([5, 4, -1, 7, 8]) == 23
    
    @pytest.mark.fundamentals
    @pytest.mark.medium
    def test_max_subarray_sum_brute_force_negative(self):
        """Test max subarray sum with all negative numbers."""
        assert self.fundamentals.max_subarray_sum_brute_force([-2, -1]) == -1
        assert self.fundamentals.max_subarray_sum_brute_force([-1]) == -1