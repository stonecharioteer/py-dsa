import pytest
from src.py_dsa.two_pointers_exercises import TwoPointersExercises, ListNode


class TestTwoPointersExercises:
    """
    Tests for two pointers technique exercises with progressive difficulty.
    """
    
    def setup_method(self):
        self.two_pointers = TwoPointersExercises()
    
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
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_pair_with_target_sum_basic(self):
        """Test pair with target sum in sorted array."""
        assert self.two_pointers.pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
        assert self.two_pointers.pair_with_target_sum([2, 5, 9, 11], 11) == [0, 2]
        assert self.two_pointers.pair_with_target_sum([1, 2, 3, 4], 7) == [2, 3]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_pair_with_target_sum_edge_cases(self):
        """Test pair with target sum edge cases."""
        assert self.two_pointers.pair_with_target_sum([1, 2], 3) == [0, 1]
        assert self.two_pointers.pair_with_target_sum([1, 3], 5) == []
        assert self.two_pointers.pair_with_target_sum([-1, 0, 1, 2], 1) == [2, 3]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_remove_duplicates_sorted_array_basic(self):
        """Test remove duplicates from sorted array."""
        nums1 = [1, 1, 2, 3, 3, 3, 4, 4]
        result1 = self.two_pointers.remove_duplicates_sorted_array(nums1)
        assert result1 == 4
        assert nums1[:result1] == [1, 2, 3, 4]
        
        nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result2 = self.two_pointers.remove_duplicates_sorted_array(nums2)
        assert result2 == 5
        assert nums2[:result2] == [0, 1, 2, 3, 4]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_move_zeros_to_end_basic(self):
        """Test moving zeros to end."""
        nums1 = [0, 1, 0, 3, 12]
        self.two_pointers.move_zeros_to_end(nums1)
        assert nums1 == [1, 3, 12, 0, 0]
        
        nums2 = [0, 0, 1]
        self.two_pointers.move_zeros_to_end(nums2)
        assert nums2 == [1, 0, 0]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_reverse_string_basic(self):
        """Test reverse string in-place."""
        s1 = ["h","e","l","l","o"]
        self.two_pointers.reverse_string(s1)
        assert s1 == ["o","l","l","e","h"]
        
        s2 = ["H","a","n","n","a","h"]
        self.two_pointers.reverse_string(s2)
        assert s2 == ["h","a","n","n","a","H"]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_basic
    @pytest.mark.easy
    def test_valid_palindrome_basic(self):
        """Test valid palindrome check."""
        assert self.two_pointers.valid_palindrome("A man, a plan, a canal: Panama") == True
        assert self.two_pointers.valid_palindrome("race a car") == False
        assert self.two_pointers.valid_palindrome("") == True
    
    # INTERMEDIATE LEVEL TESTS
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_intermediate
    @pytest.mark.medium
    def test_three_sum_basic(self):
        """Test three sum problem."""
        result1 = self.two_pointers.three_sum([-1, 0, 1, 2, -1, -4])
        expected1 = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(result1) == sorted(expected1)
        
        assert self.two_pointers.three_sum([0, 1, 1]) == []
        assert self.two_pointers.three_sum([0, 0, 0]) == [[0, 0, 0]]
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_intermediate
    @pytest.mark.medium
    def test_three_sum_closest_basic(self):
        """Test three sum closest to target."""
        assert self.two_pointers.three_sum_closest([-1, 2, 1, -4], 1) == 2
        assert self.two_pointers.three_sum_closest([0, 0, 0], 1) == 0
        assert self.two_pointers.three_sum_closest([1, 1, 1, 0], -100) == 2
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_intermediate
    @pytest.mark.medium
    def test_container_with_most_water_basic(self):
        """Test container with most water."""
        assert self.two_pointers.container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49
        assert self.two_pointers.container_with_most_water([1,1]) == 1
        assert self.two_pointers.container_with_most_water([1,2,1]) == 2
    
    # ADVANCED LEVEL TESTS
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_advanced
    @pytest.mark.hard
    def test_linked_list_cycle_basic(self):
        """Test linked list cycle detection."""
        # Create cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
        head = ListNode(3)
        node2 = ListNode(2)
        node0 = ListNode(0)
        node4 = ListNode(-4)
        
        head.next = node2
        node2.next = node0
        node0.next = node4
        node4.next = node2  # Create cycle
        
        assert self.two_pointers.linked_list_cycle(head) == True
        
        # No cycle
        head2 = ListNode(1)
        head2.next = ListNode(2)
        assert self.two_pointers.linked_list_cycle(head2) == False
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_advanced
    @pytest.mark.hard
    def test_find_duplicate_number_basic(self):
        """Test finding duplicate number using Floyd's algorithm."""
        assert self.two_pointers.find_duplicate_number([1,3,4,2,2]) == 2
        assert self.two_pointers.find_duplicate_number([3,1,3,4,2]) == 3
        assert self.two_pointers.find_duplicate_number([1,1]) == 1
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_advanced
    @pytest.mark.hard
    def test_happy_number_basic(self):
        """Test happy number detection."""
        assert self.two_pointers.happy_number(19) == True
        assert self.two_pointers.happy_number(2) == False
        assert self.two_pointers.happy_number(1) == True
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_advanced
    @pytest.mark.hard
    def test_middle_of_linked_list_basic(self):
        """Test finding middle of linked list."""
        head1 = self.create_linked_list([1,2,3,4,5])
        middle1 = self.two_pointers.middle_of_linked_list(head1)
        assert middle1.val == 3
        
        head2 = self.create_linked_list([1,2,3,4,5,6])
        middle2 = self.two_pointers.middle_of_linked_list(head2)
        assert middle2.val == 4
    
    @pytest.mark.two_pointers
    @pytest.mark.two_pointers_advanced
    @pytest.mark.hard
    def test_four_sum_basic(self):
        """Test four sum problem."""
        result1 = self.two_pointers.four_sum([1,0,-1,0,-2,2], 0)
        expected1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        assert len(result1) == len(expected1)
        for triplet in expected1:
            assert triplet in result1 or sorted(triplet) in [sorted(x) for x in result1]