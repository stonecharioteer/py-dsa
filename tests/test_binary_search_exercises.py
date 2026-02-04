import pytest
from src.py_dsa.binary_search_exercises import BinarySearchExercises


class TestBinarySearchExercises:
    """
    Tests for binary search exercises covering iterative, recursive, and advanced search techniques.
    Binary search is fundamental for efficient searching in sorted data structures.
    """
    
    def setup_method(self):
        self.binary_search = BinarySearchExercises()
    
    # BASIC BINARY SEARCH TESTS
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_iterative_found(self):
        """Test iterative binary search when target exists."""
        assert self.binary_search.binary_search_iterative([-1, 0, 3, 5, 9, 12], 9) == 4
        assert self.binary_search.binary_search_iterative([5], 5) == 0
        assert self.binary_search.binary_search_iterative([1, 2, 3, 4, 5], 1) == 0
        assert self.binary_search.binary_search_iterative([1, 2, 3, 4, 5], 5) == 4
        assert self.binary_search.binary_search_iterative([1, 2, 3, 4, 5], 3) == 2
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_iterative_not_found(self):
        """Test iterative binary search when target doesn't exist."""
        assert self.binary_search.binary_search_iterative([-1, 0, 3, 5, 9, 12], 2) == -1
        assert self.binary_search.binary_search_iterative([5], 4) == -1
        assert self.binary_search.binary_search_iterative([1, 2, 3, 4, 5], 6) == -1
        assert self.binary_search.binary_search_iterative([1, 2, 3, 4, 5], 0) == -1
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_iterative_empty(self):
        """Test iterative binary search with empty array."""
        assert self.binary_search.binary_search_iterative([], 1) == -1
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_recursive_found(self):
        """Test recursive binary search when target exists."""
        assert self.binary_search.binary_search_recursive([-1, 0, 3, 5, 9, 12], 9) == 4
        assert self.binary_search.binary_search_recursive([5], 5) == 0
        assert self.binary_search.binary_search_recursive([1, 2, 3, 4, 5], 1) == 0
        assert self.binary_search.binary_search_recursive([1, 2, 3, 4, 5], 5) == 4
        assert self.binary_search.binary_search_recursive([1, 2, 3, 4, 5], 3) == 2
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_recursive_not_found(self):
        """Test recursive binary search when target doesn't exist."""
        assert self.binary_search.binary_search_recursive([-1, 0, 3, 5, 9, 12], 2) == -1
        assert self.binary_search.binary_search_recursive([5], 4) == -1
        assert self.binary_search.binary_search_recursive([1, 2, 3, 4, 5], 6) == -1
        assert self.binary_search.binary_search_recursive([1, 2, 3, 4, 5], 0) == -1
    
    @pytest.mark.binary_search
    @pytest.mark.easy
    def test_binary_search_recursive_empty(self):
        """Test recursive binary search with empty array."""
        assert self.binary_search.binary_search_recursive([], 1) == -1
    
    @pytest.mark.binary_search
    @pytest.mark.medium
    def test_first_occurrence_basic(self):
        """Test finding first occurrence of target."""
        assert self.binary_search.first_occurrence([5, 7, 7, 8, 8, 10], 8) == 3
        assert self.binary_search.first_occurrence([1, 1, 1, 1, 1], 1) == 0
        assert self.binary_search.first_occurrence([1, 2, 3, 4, 5], 3) == 2
    
    @pytest.mark.binary_search
    @pytest.mark.medium
    def test_first_occurrence_not_found(self):
        """Test first occurrence when target doesn't exist."""
        assert self.binary_search.first_occurrence([5, 7, 7, 8, 8, 10], 6) == -1
        assert self.binary_search.first_occurrence([1, 2, 3, 4, 5], 6) == -1
        assert self.binary_search.first_occurrence([], 1) == -1