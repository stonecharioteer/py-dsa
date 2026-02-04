import pytest
from src.py_dsa.linked_list_exercises import LinkedListExercises, ListNode, RandomListNode


class TestLinkedListExercises:
    """
    Tests for linked list exercises covering reversal, cycle detection, merging, and manipulation.
    Essential for understanding pointer operations and linear data structures.
    """
    
    def setup_method(self):
        self.ll = LinkedListExercises()
    
    # Helper methods for creating test lists
    def create_list(self, values: list) -> ListNode:
        """Create linked list from values."""
        return self.ll.array_to_list(values)
    
    def list_values(self, head: ListNode) -> list:
        """Extract values from linked list."""
        return self.ll.list_to_array(head)
    
    # BASIC OPERATION TESTS
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_reverse_linked_list_basic(self):
        """Test iterative linked list reversal."""
        head = self.create_list([1, 2, 3, 4, 5])
        result = self.ll.reverse_linked_list(head)
        assert self.list_values(result) == [5, 4, 3, 2, 1]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_reverse_linked_list_single(self):
        """Test reversal with single node."""
        head = self.create_list([1])
        result = self.ll.reverse_linked_list(head)
        assert self.list_values(result) == [1]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_reverse_linked_list_empty(self):
        """Test reversal with empty list."""
        result = self.ll.reverse_linked_list(None)
        assert result is None
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_reverse_linked_list_recursive_basic(self):
        """Test recursive linked list reversal."""
        head = self.create_list([1, 2, 3, 4])
        result = self.ll.reverse_linked_list_recursive(head)
        assert self.list_values(result) == [4, 3, 2, 1]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_find_middle_node_odd(self):
        """Test finding middle node with odd length."""
        head = self.create_list([1, 2, 3, 4, 5])
        middle = self.ll.find_middle_node(head)
        assert middle.val == 3
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_find_middle_node_even(self):
        """Test finding middle node with even length."""
        head = self.create_list([1, 2, 3, 4])
        middle = self.ll.find_middle_node(head)
        assert middle.val == 3  # Second middle for even length
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_find_middle_node_single(self):
        """Test finding middle of single node."""
        head = self.create_list([1])
        middle = self.ll.find_middle_node(head)
        assert middle.val == 1
    
    # CYCLE DETECTION TESTS
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_has_cycle_no_cycle(self):
        """Test cycle detection with no cycle."""
        head = self.create_list([1, 2, 3, 4])
        assert self.ll.has_cycle(head) == False
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_has_cycle_with_cycle(self):
        """Test cycle detection with cycle."""
        head = self.create_list([3, 2, 0, -4])
        head = self.ll.create_cycle(head, 1)  # Cycle back to position 1
        assert self.ll.has_cycle(head) == True
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_has_cycle_single_node_cycle(self):
        """Test cycle detection with single node pointing to itself."""
        head = ListNode(1)
        head.next = head
        assert self.ll.has_cycle(head) == True
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_find_cycle_start_basic(self):
        """Test finding cycle start position."""
        head = self.create_list([3, 2, 0, -4])
        head = self.ll.create_cycle(head, 1)
        cycle_start = self.ll.find_cycle_start(head)
        assert cycle_start.val == 2
    
    # MANIPULATION TESTS
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_remove_nth_from_end_basic(self):
        """Test removing nth node from end."""
        head = self.create_list([1, 2, 3, 4, 5])
        result = self.ll.remove_nth_from_end(head, 2)
        assert self.list_values(result) == [1, 2, 3, 5]
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_remove_nth_from_end_first(self):
        """Test removing first node (nth = length)."""
        head = self.create_list([1, 2])
        result = self.ll.remove_nth_from_end(head, 2)
        assert self.list_values(result) == [2]
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_remove_nth_from_end_last(self):
        """Test removing last node (nth = 1)."""
        head = self.create_list([1, 2, 3])
        result = self.ll.remove_nth_from_end(head, 1)
        assert self.list_values(result) == [1, 2]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_remove_duplicates_basic(self):
        """Test removing duplicates from sorted list."""
        head = self.create_list([1, 1, 2, 3, 3])
        result = self.ll.remove_duplicates(head)
        assert self.list_values(result) == [1, 2, 3]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_remove_duplicates_all_same(self):
        """Test removing duplicates when all elements are same."""
        head = self.create_list([1, 1, 1])
        result = self.ll.remove_duplicates(head)
        assert self.list_values(result) == [1]
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_remove_all_duplicates_basic(self):
        """Test removing all duplicate nodes."""
        head = self.create_list([1, 2, 3, 3, 4, 4, 5])
        result = self.ll.remove_all_duplicates(head)
        assert self.list_values(result) == [1, 2, 5]
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_partition_list_basic(self):
        """Test partitioning list around value."""
        head = self.create_list([1, 4, 3, 2, 5, 2])
        result = self.ll.partition_list(head, 3)
        values = self.list_values(result)
        
        # Find partition point
        partition_idx = None
        for i, val in enumerate(values):
            if val >= 3:
                partition_idx = i
                break
        
        # All values before partition should be < 3
        if partition_idx is not None:
            assert all(val < 3 for val in values[:partition_idx])
            assert all(val >= 3 for val in values[partition_idx:])
    
    # MERGING TESTS
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_merge_two_sorted_lists_basic(self):
        """Test merging two sorted lists."""
        l1 = self.create_list([1, 2, 4])
        l2 = self.create_list([1, 3, 4])
        result = self.ll.merge_two_sorted_lists(l1, l2)
        assert self.list_values(result) == [1, 1, 2, 3, 4, 4]
    
    @pytest.mark.linked_list
    @pytest.mark.easy
    def test_merge_two_sorted_lists_empty(self):
        """Test merging with empty lists."""
        l1 = self.create_list([])
        l2 = self.create_list([1, 2, 3])
        result = self.ll.merge_two_sorted_lists(l1, l2)
        assert self.list_values(result) == [1, 2, 3]
    
    @pytest.mark.linked_list
    @pytest.mark.hard
    def test_merge_k_sorted_lists_basic(self):
        """Test merging k sorted lists."""
        lists = [
            self.create_list([1, 4, 5]),
            self.create_list([1, 3, 4]),
            self.create_list([2, 6])
        ]
        result = self.ll.merge_k_sorted_lists(lists)
        assert self.list_values(result) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    @pytest.mark.linked_list
    @pytest.mark.hard
    def test_merge_k_sorted_lists_empty(self):
        """Test merging empty list of lists."""
        result = self.ll.merge_k_sorted_lists([])
        assert result is None
    
    # ADVANCED TESTS
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_add_two_numbers_basic(self):
        """Test adding two numbers represented as linked lists."""
        l1 = self.create_list([2, 4, 3])  # 342
        l2 = self.create_list([5, 6, 4])  # 465
        result = self.ll.add_two_numbers(l1, l2)
        assert self.list_values(result) == [7, 0, 8]  # 807
    
    @pytest.mark.linked_list
    @pytest.mark.medium
    def test_add_two_numbers_with_carry(self):
        """Test addition with carry."""
        l1 = self.create_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.create_list([9, 9, 9, 9])
        result = self.ll.add_two_numbers(l1, l2)
        assert self.list_values(result) == [8, 9, 9, 9, 0, 0, 0, 1]
    
    @pytest.mark.linked_list
    @pytest.mark.hard
    def test_reverse_nodes_in_k_group_basic(self):
        """Test reversing nodes in groups of k."""
        head = self.create_list([1, 2, 3, 4, 5])
        result = self.ll.reverse_nodes_in_k_group(head, 2)
        assert self.list_values(result) == [2, 1, 4, 3, 5]
    
    @pytest.mark.linked_list
    @pytest.mark.hard
    def test_reverse_nodes_in_k_group_exact(self):
        """Test reversing when length is exact multiple of k."""
        head = self.create_list([1, 2, 3, 4, 5, 6])
        result = self.ll.reverse_nodes_in_k_group(head, 3)
        assert self.list_values(result) == [3, 2, 1, 6, 5, 4]