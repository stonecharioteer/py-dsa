import pytest
from src.py_dsa.string_algorithms_exercises import StringAlgorithmsExercises


class TestStringAlgorithmsExercises:
    """
    Tests for string algorithm exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.string_algos = StringAlgorithmsExercises()
    
    # BASIC LEVEL TESTS - Fundamental string operations
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_count_characters_basic(self):
        """Test character frequency counting basic cases."""
        result = self.string_algos.count_characters("hello")
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        assert result == expected
        
        result = self.string_algos.count_characters("aabcc")
        expected = {'a': 2, 'b': 1, 'c': 2}
        assert result == expected
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_count_characters_edge_cases(self):
        """Test character frequency counting edge cases."""
        assert self.string_algos.count_characters("") == {}
        assert self.string_algos.count_characters("a") == {'a': 1}
        assert self.string_algos.count_characters("aaa") == {'a': 3}
        
        # Test special characters and numbers
        assert self.string_algos.count_characters("a1b2c3") == {'a': 1, '1': 1, 'b': 1, '2': 1, 'c': 1, '3': 1}
        assert self.string_algos.count_characters("!@#$%") == {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1}
        
        # Test unicode characters
        assert self.string_algos.count_characters("αβγ") == {'α': 1, 'β': 1, 'γ': 1}
        
        # Test whitespace
        assert self.string_algos.count_characters("a b c") == {'a': 1, ' ': 2, 'b': 1, 'c': 1}
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_reverse_string_basic(self):
        """Test string reversal basic cases."""
        assert self.string_algos.reverse_string("hello") == "olleh"
        assert self.string_algos.reverse_string("world") == "dlrow"
        assert self.string_algos.reverse_string("abc") == "cba"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_reverse_string_edge_cases(self):
        """Test string reversal edge cases."""
        assert self.string_algos.reverse_string("") == ""
        assert self.string_algos.reverse_string("a") == "a"
        assert self.string_algos.reverse_string("ab") == "ba"
        
        # Test longer strings
        assert self.string_algos.reverse_string("abcdefg") == "gfedcba"
        
        # Test with numbers and special characters
        assert self.string_algos.reverse_string("123!@#") == "#@!321"
        
        # Test with spaces
        assert self.string_algos.reverse_string("a b c") == "c b a"
        
        # Test unicode
        assert self.string_algos.reverse_string("αβγ") == "γβα"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_is_palindrome_simple_basic(self):
        """Test simple palindrome checking basic cases."""
        assert self.string_algos.is_palindrome_simple("racecar") == True
        assert self.string_algos.is_palindrome_simple("hello") == False
        assert self.string_algos.is_palindrome_simple("madam") == True
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_is_palindrome_simple_edge_cases(self):
        """Test simple palindrome checking edge cases."""
        assert self.string_algos.is_palindrome_simple("") == True
        assert self.string_algos.is_palindrome_simple("a") == True
        assert self.string_algos.is_palindrome_simple("aa") == True
        assert self.string_algos.is_palindrome_simple("ab") == False
        
        # Test longer palindromes
        assert self.string_algos.is_palindrome_simple("abccba") == True
        assert self.string_algos.is_palindrome_simple("abcdcba") == True
        assert self.string_algos.is_palindrome_simple("abcddcba") == True
        
        # Test non-palindromes
        assert self.string_algos.is_palindrome_simple("abcde") == False
        assert self.string_algos.is_palindrome_simple("abcdefg") == False
        
        # Test with numbers
        assert self.string_algos.is_palindrome_simple("12321") == True
        assert self.string_algos.is_palindrome_simple("12345") == False
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_is_palindrome_advanced(self):
        """Test advanced palindrome checking with filtering."""
        assert self.string_algos.is_palindrome("A man, a plan, a canal: Panama") == True
        assert self.string_algos.is_palindrome("race a car") == False
        assert self.string_algos.is_palindrome("") == True
        
        # Test various punctuation and spacing
        assert self.string_algos.is_palindrome("Was it a car or a cat I saw?") == True
        assert self.string_algos.is_palindrome("No 'x' in Nixon") == True
        assert self.string_algos.is_palindrome("Mr. Owl ate my metal worm") == True
        
        # Test mixed case with numbers
        assert self.string_algos.is_palindrome("A Santa at NASA") == True
        assert self.string_algos.is_palindrome("Was it a car or a cat I saw?") == True
        
        # Test clearly non-palindromes
        assert self.string_algos.is_palindrome("hello world") == False
        assert self.string_algos.is_palindrome("This is not a palindrome") == False
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_reverse_words_simple_basic(self):
        """Test simple word reversal basic cases."""
        assert self.string_algos.reverse_words_simple("hello world") == "olleh dlrow"
        assert self.string_algos.reverse_words_simple("abc def") == "cba fed"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_reverse_words_basic(self):
        """Test word reversal basic cases."""
        assert self.string_algos.reverse_words("the sky is blue") == "blue is sky the"
        assert self.string_algos.reverse_words("  hello world  ") == "world hello"
        assert self.string_algos.reverse_words("a good   example") == "example good a"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_longest_common_prefix_basic(self):
        """Test longest common prefix basic cases."""
        assert self.string_algos.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
        assert self.string_algos.longest_common_prefix(["dog", "racecar", "car"]) == ""
        assert self.string_algos.longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_longest_common_prefix_edge_cases(self):
        """Test longest common prefix edge cases."""
        assert self.string_algos.longest_common_prefix([]) == ""
        assert self.string_algos.longest_common_prefix(["abc"]) == "abc"
        assert self.string_algos.longest_common_prefix(["", "abc"]) == ""
        
        # Test all same strings
        assert self.string_algos.longest_common_prefix(["abc", "abc", "abc"]) == "abc"
        
        # Test progressively shorter prefixes
        assert self.string_algos.longest_common_prefix(["abcdef", "abcxyz", "abc123"]) == "abc"
        assert self.string_algos.longest_common_prefix(["prefix", "prelude", "prepare"]) == "pre"
        
        # Test no common prefix
        assert self.string_algos.longest_common_prefix(["abc", "def", "ghi"]) == ""
        assert self.string_algos.longest_common_prefix(["zebra", "apple", "banana"]) == ""
        
        # Test case sensitivity
        assert self.string_algos.longest_common_prefix(["ABC", "abc"]) == ""
        assert self.string_algos.longest_common_prefix(["Test", "Testing", "Tester"]) == "Test"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_valid_anagram_basic(self):
        """Test anagram validation basic cases."""
        assert self.string_algos.valid_anagram("anagram", "nagaram") == True
        assert self.string_algos.valid_anagram("rat", "car") == False
        assert self.string_algos.valid_anagram("listen", "silent") == True
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_valid_anagram_edge_cases(self):
        """Test anagram validation edge cases."""
        assert self.string_algos.valid_anagram("", "") == True
        assert self.string_algos.valid_anagram("a", "a") == True
        assert self.string_algos.valid_anagram("a", "b") == False
        assert self.string_algos.valid_anagram("ab", "ba") == True
        
        # Test different lengths
        assert self.string_algos.valid_anagram("abc", "ab") == False
        assert self.string_algos.valid_anagram("a", "aa") == False
        
        # Test case sensitivity
        assert self.string_algos.valid_anagram("Listen", "Silent") == False  # Case matters
        assert self.string_algos.valid_anagram("listen", "silent") == True
        
        # Test with repeated characters
        assert self.string_algos.valid_anagram("aabbcc", "abcabc") == True
        assert self.string_algos.valid_anagram("aabbcc", "abccba") == True
        assert self.string_algos.valid_anagram("aabbcc", "abcdef") == False
        
        # Test longer anagrams
        assert self.string_algos.valid_anagram("conversation", "voices rant on") == False  # Has space
        assert self.string_algos.valid_anagram("astronomer", "moonstarer") == True
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_first_unique_character_basic(self):
        """Test first unique character basic cases."""
        assert self.string_algos.first_unique_character("leetcode") == 0
        assert self.string_algos.first_unique_character("loveleetcode") == 2
        assert self.string_algos.first_unique_character("aabb") == -1
        
        # Test edge cases
        assert self.string_algos.first_unique_character("") == -1
        assert self.string_algos.first_unique_character("a") == 0
        
        # Test all same characters
        assert self.string_algos.first_unique_character("aaaa") == -1
        
        # Test unique at different positions
        assert self.string_algos.first_unique_character("abccba") == -1
        assert self.string_algos.first_unique_character("abcabc") == -1
        assert self.string_algos.first_unique_character("abccbad") == 6  # 'd' at index 6
        
        # Test with numbers and special chars
        assert self.string_algos.first_unique_character("112233!@#") == 6  # '!' at index 6
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_remove_duplicates_basic(self):
        """Test duplicate removal basic cases."""
        assert self.string_algos.remove_duplicates("programming") == "progamin"
        assert self.string_algos.remove_duplicates("hello") == "helo"
        assert self.string_algos.remove_duplicates("aabbcc") == "abc"
        
        # Test edge cases
        assert self.string_algos.remove_duplicates("") == ""
        assert self.string_algos.remove_duplicates("a") == "a"
        assert self.string_algos.remove_duplicates("ab") == "ab"
        
        # Test all same character
        assert self.string_algos.remove_duplicates("aaaa") == "a"
        
        # Test no duplicates
        assert self.string_algos.remove_duplicates("abcdef") == "abcdef"
        
        # Test complex patterns
        assert self.string_algos.remove_duplicates("abcabcabc") == "abc"
        assert self.string_algos.remove_duplicates("aabbccddee") == "abcde"
        
        # Test with spaces and special characters
        assert self.string_algos.remove_duplicates("a b c a b c") == "a bc"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_is_rotation_basic(self):
        """Test string rotation basic cases."""
        assert self.string_algos.is_rotation("waterbottle", "erbottlewat") == True
        assert self.string_algos.is_rotation("abcde", "cdeab") == True
        assert self.string_algos.is_rotation("abcde", "abced") == False
        
        # Test edge cases
        assert self.string_algos.is_rotation("", "") == True
        assert self.string_algos.is_rotation("a", "a") == True
        assert self.string_algos.is_rotation("ab", "ba") == True
        
        # Test different lengths
        assert self.string_algos.is_rotation("abc", "ab") == False
        assert self.string_algos.is_rotation("abc", "abcd") == False
        
        # Test identical strings
        assert self.string_algos.is_rotation("hello", "hello") == True
        
        # Test all rotations of a string
        assert self.string_algos.is_rotation("abc", "bca") == True
        assert self.string_algos.is_rotation("abc", "cab") == True
        
        # Test clearly not rotations
        assert self.string_algos.is_rotation("abc", "def") == False
        assert self.string_algos.is_rotation("abc", "acb") == False
    
    # INTERMEDIATE LEVEL TESTS - String manipulation
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_replace_spaces_basic(self):
        """Test space replacement basic cases."""
        assert self.string_algos.replace_spaces("Mr John Smith    ", 13) == "Mr%20John%20Smith"
        assert self.string_algos.replace_spaces("hello world  ", 11) == "hello%20world"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_string_permutation_basic(self):
        """Test string permutation checking basic cases."""
        assert self.string_algos.string_permutation("abc", "bca") == True
        assert self.string_algos.string_permutation("abc", "def") == False
        assert self.string_algos.string_permutation("aab", "aba") == True
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_one_edit_distance_basic(self):
        """Test one edit distance basic cases."""
        assert self.string_algos.one_edit_distance("pale", "ple") == True
        assert self.string_algos.one_edit_distance("pales", "pale") == True
        assert self.string_algos.one_edit_distance("pale", "bale") == True
        assert self.string_algos.one_edit_distance("pale", "bake") == False
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_compress_string_basic(self):
        """Test string compression basic cases."""
        assert self.string_algos.compress_string("aabcccccaaa") == "a2b1c5a3"
        assert self.string_algos.compress_string("abcdef") == "abcdef"  # Original shorter
        assert self.string_algos.compress_string("aabbcc") == "aabbcc"  # Original shorter
    
    # PATTERN MATCHING TESTS
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_implement_strstr_basic(self):
        """Test basic string search basic cases."""
        assert self.string_algos.implement_strstr("hello", "ll") == 2
        assert self.string_algos.implement_strstr("aaaaa", "bba") == -1
        assert self.string_algos.implement_strstr("", "") == 0
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_advanced
    @pytest.mark.hard
    def test_kmp_pattern_search_basic(self):
        """Test KMP pattern search basic cases."""
        result = self.string_algos.kmp_pattern_search("ababcababa", "abab")
        assert result == [0, 5]
        
        result = self.string_algos.kmp_pattern_search("abcdefg", "def")
        assert result == [3]
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_advanced
    @pytest.mark.hard
    def test_rabin_karp_search_basic(self):
        """Test Rabin-Karp search basic cases."""
        result = self.string_algos.rabin_karp_search("abcdefg", "cde")
        assert result == [2]
        
        result = self.string_algos.rabin_karp_search("ababab", "ab")
        assert result == [0, 2, 4]
    
    # SUBSTRING TESTS
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_find_all_substrings_basic(self):
        """Test finding all substrings basic cases."""
        result = self.string_algos.find_all_substrings("abc")
        expected = ["a", "ab", "abc", "b", "bc", "c"]
        assert set(result) == set(expected)
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_longest_substring_without_repeating_basic(self):
        """Test longest substring without repeating characters."""
        assert self.string_algos.longest_substring_without_repeating("abcabcbb") == 3
        assert self.string_algos.longest_substring_without_repeating("bbbbb") == 1
        assert self.string_algos.longest_substring_without_repeating("pwwkew") == 3
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_longest_substring_k_distinct_basic(self):
        """Test longest substring with k distinct characters."""
        assert self.string_algos.longest_substring_k_distinct("eceba", 2) == 3
        assert self.string_algos.longest_substring_k_distinct("aa", 1) == 2
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_advanced
    @pytest.mark.hard
    def test_minimum_window_substring_basic(self):
        """Test minimum window substring basic cases."""
        assert self.string_algos.minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"
        assert self.string_algos.minimum_window_substring("a", "a") == "a"
        assert self.string_algos.minimum_window_substring("a", "aa") == ""
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_find_all_anagrams_basic(self):
        """Test finding all anagrams basic cases."""
        result = self.string_algos.find_all_anagrams("abab", "ab")
        assert result == [0, 2]
        
        result = self.string_algos.find_all_anagrams("abacabad", "abab")
        assert result == [0, 4]
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_longest_palindromic_substring_basic(self):
        """Test longest palindromic substring basic cases."""
        result = self.string_algos.longest_palindromic_substring("babad")
        assert result in ["bab", "aba"]
        
        assert self.string_algos.longest_palindromic_substring("cbbd") == "bb"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_palindromic_substrings_count_basic(self):
        """Test palindromic substring counting basic cases."""
        assert self.string_algos.palindromic_substrings_count("abc") == 3
        assert self.string_algos.palindromic_substrings_count("aaa") == 6
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_valid_palindrome_ii_basic(self):
        """Test valid palindrome after one deletion."""
        assert self.string_algos.valid_palindrome_ii("aba") == True
        assert self.string_algos.valid_palindrome_ii("abca") == True
        assert self.string_algos.valid_palindrome_ii("abc") == False
    
    # DYNAMIC PROGRAMMING TESTS
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_is_subsequence_basic(self):
        """Test subsequence checking basic cases."""
        assert self.string_algos.is_subsequence("ace", "abcde") == True
        assert self.string_algos.is_subsequence("aec", "abcde") == False
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_advanced
    @pytest.mark.hard
    def test_edit_distance_basic(self):
        """Test edit distance basic cases."""
        assert self.string_algos.edit_distance("horse", "ros") == 3
        assert self.string_algos.edit_distance("intention", "execution") == 5
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_longest_common_subsequence_basic(self):
        """Test longest common subsequence basic cases."""
        assert self.string_algos.longest_common_subsequence("abcde", "ace") == 3
        assert self.string_algos.longest_common_subsequence("abc", "abc") == 3
        assert self.string_algos.longest_common_subsequence("abc", "def") == 0
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_longest_common_substring_basic(self):
        """Test longest common substring basic cases."""
        assert self.string_algos.longest_common_substring("abcdxyz", "xyzabcd") == 4
        assert self.string_algos.longest_common_substring("zxabcdezy", "yzabcdezx") == 6
    
    # COMPRESSION AND ENCODING TESTS
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_run_length_encoding_basic(self):
        """Test run-length encoding basic cases."""
        assert self.string_algos.run_length_encoding("aabcccccaaa") == "a2b1c5a3"
        assert self.string_algos.run_length_encoding("abcdef") == "a1b1c1d1e1f1"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_basic
    @pytest.mark.easy
    def test_run_length_decoding_basic(self):
        """Test run-length decoding basic cases."""
        assert self.string_algos.run_length_decoding("a2b1c5a3") == "aabcccccaaa"
        assert self.string_algos.run_length_decoding("a1b1c1") == "abc"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_string_compression_array_basic(self):
        """Test in-place string compression basic cases."""
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result = self.string_algos.string_compression(chars)
        assert result == 6
        assert chars[:6] == ["a", "2", "b", "2", "c", "3"]
    
    # REAL-WORLD PROBLEMS TESTS
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_validate_ip_address_basic(self):
        """Test IP address validation basic cases."""
        assert self.string_algos.validate_ip_address("192.168.1.1") == "IPv4"
        assert self.string_algos.validate_ip_address("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
        assert self.string_algos.validate_ip_address("256.256.256.256") == "Neither"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_word_break_basic(self):
        """Test word break basic cases."""
        assert self.string_algos.word_break("leetcode", ["leet", "code"]) == True
        assert self.string_algos.word_break("applepenapple", ["apple", "pen"]) == True
        assert self.string_algos.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_advanced
    @pytest.mark.hard
    def test_word_break_ii_basic(self):
        """Test word break II basic cases."""
        result = self.string_algos.word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        expected = ["cats and dog", "cat sand dog"]
        assert set(result) == set(expected)
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_isomorphic_strings_basic(self):
        """Test isomorphic strings basic cases."""
        assert self.string_algos.isomorphic_strings("egg", "add") == True
        assert self.string_algos.isomorphic_strings("foo", "bar") == False
        assert self.string_algos.isomorphic_strings("paper", "title") == True
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_group_anagrams_basic(self):
        """Test group anagrams basic cases."""
        result = self.string_algos.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Convert to sets for comparison since order doesn't matter
        result_sets = [set(group) for group in result]
        expected_sets = [{"eat", "tea", "ate"}, {"tan", "nat"}, {"bat"}]
        assert len(result_sets) == len(expected_sets)
        for expected_set in expected_sets:
            assert expected_set in result_sets
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_decode_string_basic(self):
        """Test string decoding basic cases."""
        assert self.string_algos.decode_string("3[a]2[bc]") == "aaabcbc"
        assert self.string_algos.decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
        assert self.string_algos.decode_string("abc3[cd]xyz") == "abccdcdcdxyz"
    
    @pytest.mark.string_algorithms
    @pytest.mark.string_algorithms_intermediate
    @pytest.mark.medium
    def test_simplify_path_basic(self):
        """Test path simplification basic cases."""
        assert self.string_algos.simplify_path("/home/") == "/home"
        assert self.string_algos.simplify_path("/../") == "/"
        assert self.string_algos.simplify_path("/home//foo/") == "/home/foo"
        assert self.string_algos.simplify_path("/a/./b/../../c/") == "/c"