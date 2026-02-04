import pytest
from src.py_dsa.heap_exercises import HeapExercises, MedianFinder, ListNode


class TestHeapExercises:
    """
    Tests for heap and priority queue exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.heap = HeapExercises()
    
    def create_linked_list(self, values):
        """Helper to create linked list from values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_values(self, head):
        """Helper to convert linked list to values."""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values
    
    # BASIC LEVEL TESTS
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_kth_largest_element_basic(self):
        """Test finding kth largest element."""
        assert self.heap.kth_largest_element([3,2,1,5,6,4], 2) == 5
        assert self.heap.kth_largest_element([3,2,3,1,2,4,5,5,6], 4) == 4
        assert self.heap.kth_largest_element([1], 1) == 1
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_kth_largest_element_edge_cases(self):
        """Test kth largest element edge cases."""
        assert self.heap.kth_largest_element([7,10,4,3,20,15], 3) == 10
        assert self.heap.kth_largest_element([2,1], 1) == 2
        assert self.heap.kth_largest_element([2,1], 2) == 1
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_kth_smallest_element_basic(self):
        """Test finding kth smallest element."""
        assert self.heap.kth_smallest_element([7,10,4,3,20,15], 3) == 7
        assert self.heap.kth_smallest_element([7,10,4,3,20,15], 1) == 3
        assert self.heap.kth_smallest_element([1], 1) == 1
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_last_stone_weight_basic(self):
        """Test last stone weight simulation."""
        assert self.heap.last_stone_weight([2,7,4,1,8,1]) == 1
        assert self.heap.last_stone_weight([1]) == 1
        assert self.heap.last_stone_weight([2,2]) == 0
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_last_stone_weight_edge_cases(self):
        """Test last stone weight edge cases."""
        assert self.heap.last_stone_weight([3,7,2]) == 2
        assert self.heap.last_stone_weight([1,3]) == 2
        assert self.heap.last_stone_weight([10,4,2,10]) == 2
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_merge_k_sorted_lists_basic(self):
        """Test merging k sorted linked lists."""
        # Test case: [[1,4,5],[1,3,4],[2,6]]
        list1 = self.create_linked_list([1,4,5])
        list2 = self.create_linked_list([1,3,4])
        list3 = self.create_linked_list([2,6])
        
        result = self.heap.merge_k_sorted_lists([list1, list2, list3])
        expected = [1,1,2,3,4,4,5,6]
        assert self.linked_list_to_values(result) == expected
    
    @pytest.mark.heap
    @pytest.mark.heap_basic
    @pytest.mark.easy
    def test_merge_k_sorted_lists_edge_cases(self):
        """Test merge k sorted lists edge cases."""
        # Empty lists
        assert self.heap.merge_k_sorted_lists([]) is None
        
        # Single list
        single_list = self.create_linked_list([1,2,3])
        result = self.heap.merge_k_sorted_lists([single_list])
        assert self.linked_list_to_values(result) == [1,2,3]
        
        # Lists with None
        list1 = self.create_linked_list([1,2])
        result = self.heap.merge_k_sorted_lists([list1, None])
        assert self.linked_list_to_values(result) == [1,2]
    
    # INTERMEDIATE LEVEL TESTS
    
    @pytest.mark.heap
    @pytest.mark.heap_intermediate
    @pytest.mark.medium
    def test_top_k_frequent_elements_basic(self):
        """Test finding top k frequent elements."""
        result1 = self.heap.top_k_frequent_elements([1,1,1,2,2,3], 2)
        assert sorted(result1) == sorted([1,2])
        
        result2 = self.heap.top_k_frequent_elements([1], 1)
        assert result2 == [1]
        
        result3 = self.heap.top_k_frequent_elements([1,2], 2)
        assert sorted(result3) == sorted([1,2])
    
    @pytest.mark.heap
    @pytest.mark.heap_intermediate
    @pytest.mark.medium
    def test_k_closest_points_to_origin_basic(self):
        """Test finding k closest points to origin."""
        result1 = self.heap.k_closest_points_to_origin([[1,1],[2,2],[3,3]], 1)
        assert result1 == [[1,1]]
        
        result2 = self.heap.k_closest_points_to_origin([[3,3],[5,-1],[-2,4]], 2)
        # Should return the 2 closest points (exact order may vary)
        assert len(result2) == 2
        distances = [p[0]**2 + p[1]**2 for p in result2]
        assert max(distances) <= 18  # [3,3] has distance 18
    
    @pytest.mark.heap
    @pytest.mark.heap_intermediate
    @pytest.mark.medium
    def test_task_scheduler_basic(self):
        """Test task scheduler with cooldown."""
        assert self.heap.task_scheduler(["A","A","A","B","B","B"], 2) == 8
        assert self.heap.task_scheduler(["A","A","A","B","B","B"], 0) == 6
        assert self.heap.task_scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
    
    @pytest.mark.heap
    @pytest.mark.heap_intermediate
    @pytest.mark.medium
    def test_reorganize_string_basic(self):
        """Test string reorganization to avoid adjacent duplicates."""
        result1 = self.heap.reorganize_string("aab")
        assert result1 in ["aba", "baa"]  # Either is valid
        
        result2 = self.heap.reorganize_string("aaab")
        assert result2 == ""  # Impossible to reorganize
        
        result3 = self.heap.reorganize_string("aabbcc")
        # Should be reorganized (multiple valid solutions)
        assert len(result3) == 6
        # Check no adjacent duplicates
        for i in range(len(result3) - 1):
            assert result3[i] != result3[i + 1]
    
    # ADVANCED LEVEL TESTS
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_sliding_window_maximum_basic(self):
        """Test sliding window maximum using heap."""
        result = self.heap.sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3)
        expected = [3,3,5,5,6,7]
        assert result == expected
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_sliding_window_maximum_edge_cases(self):
        """Test sliding window maximum edge cases."""
        assert self.heap.sliding_window_maximum([1], 1) == [1]
        assert self.heap.sliding_window_maximum([1,2,3,4], 2) == [2,3,4]
        assert self.heap.sliding_window_maximum([9,11], 2) == [11]
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_find_median_from_data_stream(self):
        """Test median finder data structure."""
        median_finder = self.heap.find_median_from_data_stream()
        
        # Test the MedianFinder functionality
        median_finder.addNum(1)
        median_finder.addNum(2)
        assert median_finder.findMedian() == 1.5
        
        median_finder.addNum(3)
        assert median_finder.findMedian() == 2.0
        
        median_finder.addNum(4)
        assert median_finder.findMedian() == 2.5
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_merge_k_sorted_arrays_basic(self):
        """Test merging k sorted arrays."""
        result = self.heap.merge_k_sorted_arrays([[1,4,5],[1,3,4],[2,6]])
        expected = [1,1,2,3,4,4,5,6]
        assert result == expected
        
        # Edge cases
        assert self.heap.merge_k_sorted_arrays([]) == []
        assert self.heap.merge_k_sorted_arrays([[1,2,3]]) == [1,2,3]
        assert self.heap.merge_k_sorted_arrays([[1],[2],[3]]) == [1,2,3]
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_smallest_range_covering_elements_basic(self):
        """Test finding smallest range covering all arrays."""
        result = self.heap.smallest_range_covering_elements([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
        # Expected: [20,24] or similar valid range
        assert len(result) == 2
        assert result[0] <= result[1]
        # Should cover at least one element from each array
    
    @pytest.mark.heap
    @pytest.mark.heap_advanced
    @pytest.mark.hard
    def test_ipo_maximize_capital_basic(self):
        """Test IPO capital maximization."""
        assert self.heap.ipo_maximize_capital(2, 0, [1,2,3], [0,1,1]) == 4
        assert self.heap.ipo_maximize_capital(3, 0, [1,2,3], [0,1,2]) == 6
        
        # Edge cases
        assert self.heap.ipo_maximize_capital(0, 0, [1,2,3], [0,1,1]) == 0
        assert self.heap.ipo_maximize_capital(1, 0, [1], [0]) == 1