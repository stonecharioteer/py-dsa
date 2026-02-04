import pytest
from src.py_dsa.sliding_window_exercises import SlidingWindowExercises


class TestSlidingWindowExercises:
    """
    Tests for sliding window technique exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.sliding_window = SlidingWindowExercises()
    
    # BASIC LEVEL TESTS - Fixed size sliding window
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_maximum_sum_subarray_of_size_k_basic(self):
        """Test maximum sum subarray basic cases."""
        assert self.sliding_window.maximum_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9
        assert self.sliding_window.maximum_sum_subarray_of_size_k([2, 3, 4, 1, 5], 2) == 7
        assert self.sliding_window.maximum_sum_subarray_of_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_maximum_sum_subarray_edge_cases(self):
        """Test maximum sum subarray edge cases."""
        assert self.sliding_window.maximum_sum_subarray_of_size_k([5], 1) == 5
        assert self.sliding_window.maximum_sum_subarray_of_size_k([-1, -2, -3], 1) == -1
        assert self.sliding_window.maximum_sum_subarray_of_size_k([-1, -2, -3], 2) == -3
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_average_of_subarrays_size_k_basic(self):
        """Test average of subarrays basic cases."""
        result = self.sliding_window.average_of_subarrays_size_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
        expected = [2.2, 2.8, 2.4, 3.6, 2.8]
        assert len(result) == len(expected)
        for i in range(len(result)):
            assert abs(result[i] - expected[i]) < 0.01
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_average_of_subarrays_edge_cases(self):
        """Test average of subarrays edge cases."""
        result = self.sliding_window.average_of_subarrays_size_k([1, 2, 3], 3)
        assert len(result) == 1
        assert abs(result[0] - 2.0) < 0.01
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_first_negative_in_window_basic(self):
        """Test first negative in window basic cases."""
        result = self.sliding_window.first_negative_in_window_size_k([12, -1, -7, 8, -15, 30, 16, 28], 3)
        expected = [-1, -1, -7, -15, -15, 0]
        assert result == expected
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_basic
    @pytest.mark.easy
    def test_first_negative_in_window_edge_cases(self):
        """Test first negative in window edge cases."""
        assert self.sliding_window.first_negative_in_window_size_k([1, 2, 3, 4, 5], 2) == [0, 0, 0, 0]
        assert self.sliding_window.first_negative_in_window_size_k([-1, -2, -3], 1) == [-1, -2, -3]
        assert self.sliding_window.first_negative_in_window_size_k([1, -1, 2], 2) == [-1, -1]
    
    # INTERMEDIATE LEVEL TESTS - Variable size sliding window
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_longest_substring_k_distinct_basic(self):
        """Test longest substring with k distinct characters."""
        assert self.sliding_window.longest_substring_with_k_distinct_chars("araaci", 2) == 4
        assert self.sliding_window.longest_substring_with_k_distinct_chars("araaci", 1) == 2
        assert self.sliding_window.longest_substring_with_k_distinct_chars("cbbebi", 3) == 5
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_longest_substring_k_distinct_edge_cases(self):
        """Test longest substring k distinct edge cases."""
        assert self.sliding_window.longest_substring_with_k_distinct_chars("", 2) == 0
        assert self.sliding_window.longest_substring_with_k_distinct_chars("a", 1) == 1
        assert self.sliding_window.longest_substring_with_k_distinct_chars("abcdef", 10) == 6
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_smallest_subarray_sum_basic(self):
        """Test smallest subarray with sum >= target."""
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([2, 1, 2, 3, 3, 1, 1, 1], 7) == 2
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([2, 1, 2, 3, 3, 1, 1, 1], 8) == 3
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([3, 4, 1, 1, 6], 8) == 3
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_smallest_subarray_sum_edge_cases(self):
        """Test smallest subarray sum edge cases."""
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([1, 2, 3], 10) == 0
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([10], 5) == 1
        assert self.sliding_window.smallest_subarray_with_sum_greater_than_s([1, 1, 1, 1], 3) == 3
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_longest_substring_without_repeating_basic(self):
        """Test longest substring without repeating characters."""
        assert self.sliding_window.longest_substring_without_repeating_chars("abcabcbb") == 3
        assert self.sliding_window.longest_substring_without_repeating_chars("bbbbb") == 1
        assert self.sliding_window.longest_substring_without_repeating_chars("pwwkew") == 3
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_longest_substring_without_repeating_edge_cases(self):
        """Test longest substring without repeating edge cases."""
        assert self.sliding_window.longest_substring_without_repeating_chars("") == 0
        assert self.sliding_window.longest_substring_without_repeating_chars("a") == 1
        assert self.sliding_window.longest_substring_without_repeating_chars("abcdef") == 6
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_max_fruits_in_baskets_basic(self):
        """Test max fruits in baskets (at most 2 types)."""
        assert self.sliding_window.max_fruits_in_baskets([1, 2, 1, 2, 3, 1, 2]) == 5
        assert self.sliding_window.max_fruits_in_baskets([0, 1, 2, 2]) == 3
        assert self.sliding_window.max_fruits_in_baskets([1, 2, 3, 2, 2]) == 4
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_intermediate
    @pytest.mark.medium
    def test_max_fruits_in_baskets_edge_cases(self):
        """Test max fruits in baskets edge cases."""
        assert self.sliding_window.max_fruits_in_baskets([1]) == 1
        assert self.sliding_window.max_fruits_in_baskets([1, 1, 1, 1]) == 4
        assert self.sliding_window.max_fruits_in_baskets([1, 2]) == 2
    
    # ADVANCED LEVEL TESTS - Complex sliding window problems
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_minimum_window_substring_basic(self):
        """Test minimum window substring containing all characters."""
        assert self.sliding_window.minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"
        assert self.sliding_window.minimum_window_substring("a", "a") == "a"
        assert self.sliding_window.minimum_window_substring("a", "aa") == ""
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_minimum_window_substring_edge_cases(self):
        """Test minimum window substring edge cases."""
        assert self.sliding_window.minimum_window_substring("", "abc") == ""
        assert self.sliding_window.minimum_window_substring("abc", "") == ""
        assert self.sliding_window.minimum_window_substring("ab", "ba") == "ab"
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_longest_substring_same_letters_after_k_replacements_basic(self):
        """Test longest substring with same letters after k replacements."""
        assert self.sliding_window.longest_substring_with_same_letters_after_k_replacements("AABABBA", 1) == 4
        assert self.sliding_window.longest_substring_with_same_letters_after_k_replacements("ABAB", 2) == 4
        assert self.sliding_window.longest_substring_with_same_letters_after_k_replacements("AABABBA", 2) == 6
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_max_consecutive_ones_after_k_flips_basic(self):
        """Test max consecutive 1s after flipping at most k zeros."""
        assert self.sliding_window.max_consecutive_ones_after_k_flips([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
        assert self.sliding_window.max_consecutive_ones_after_k_flips([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
        assert self.sliding_window.max_consecutive_ones_after_k_flips([1,1,1,1], 0) == 4
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_sliding_window_maximum_basic(self):
        """Test sliding window maximum."""
        assert self.sliding_window.sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
        assert self.sliding_window.sliding_window_maximum([1], 1) == [1]
        assert self.sliding_window.sliding_window_maximum([1,2,3,4], 2) == [2,3,4]
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_permutation_in_string_basic(self):
        """Test if permutation of s1 exists in s2."""
        assert self.sliding_window.permutation_in_string("ab", "eidbaooo") == True
        assert self.sliding_window.permutation_in_string("ab", "eidboaoo") == False
        assert self.sliding_window.permutation_in_string("adc", "dcda") == True
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_permutation_in_string_edge_cases(self):
        """Test permutation in string edge cases."""
        assert self.sliding_window.permutation_in_string("a", "a") == True
        assert self.sliding_window.permutation_in_string("a", "b") == False
        assert self.sliding_window.permutation_in_string("ab", "a") == False
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_find_all_anagrams_basic(self):
        """Test finding all anagram indices."""
        assert self.sliding_window.find_all_anagrams("abab", "ab") == [0, 2]
        assert self.sliding_window.find_all_anagrams("abcabc", "abc") == [0, 3]
        assert self.sliding_window.find_all_anagrams("abacabad", "aaab") == []
    
    @pytest.mark.sliding_window
    @pytest.mark.sliding_window_advanced
    @pytest.mark.hard
    def test_find_all_anagrams_edge_cases(self):
        """Test find all anagrams edge cases."""
        assert self.sliding_window.find_all_anagrams("aa", "bb") == []
        assert self.sliding_window.find_all_anagrams("a", "a") == [0]
        assert self.sliding_window.find_all_anagrams("aaaa", "aa") == [0, 1, 2]