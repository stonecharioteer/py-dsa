from typing import List, Dict, Set, Optional


class StringAlgorithmsExercises:
    """
    String Algorithm exercises with progressive difficulty.
    
    String algorithms are essential for:
    - Text processing and search
    - Pattern matching
    - DNA sequence analysis
    - Compression algorithms
    - Web search engines
    
    Key patterns:
    - Sliding window for substrings
    - Two pointers for palindromes
    - Dynamic programming for edit distance
    - KMP/Rabin-Karp for pattern matching
    - Trie for prefix operations
    """
    
    # BASIC EXERCISES - Fundamental string operations
    
    def count_characters(self, s: str) -> Dict[str, int]:
        """
        Warm-up: Count frequency of each character in string.
        
        Example:
        Input: s = "hello"
        Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        
        Time: O(n), Space: O(k) where k is unique characters
        
        TODO: Use dictionary to count character frequencies
        """
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        return result
    
    def reverse_string(self, s: str) -> str:
        """
        Warm-up: Reverse a string using different approaches.
        
        Example:
        Input: s = "hello"
        Output: "olleh"
        
        Time: O(n), Space: O(n)
        
        TODO: Try slicing, loops, or two-pointer approaches
        """
        return s[::-1]
    
    def is_palindrome(self, s: str) -> bool:
        """
        Basic: Check if string is palindrome (ignore case and non-alphanumeric).
        
        Example:
        Input: s = "A man, a plan, a canal: Panama"
        Output: True
        
        Approach: Two pointers from ends, skip non-alphanumeric
        Time: O(n), Space: O(1)
        
        TODO: Use two pointers with character filtering
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
    
    def is_palindrome_simple(self, s: str) -> bool:
        """
        Basic: Check if string is palindrome (simple version - no filtering).
        
        Example:
        Input: s = "racecar"
        Output: True
        
        Time: O(n), Space: O(1)
        
        TODO: Compare characters from both ends
        """
        return s == s[::-1]
    
    def reverse_words(self, s: str) -> str:
        """
        Basic: Reverse words in a string.
        
        Example:
        Input: s = "the sky is blue"
        Output: "blue is sky the"
        
        Approach: Split, reverse, join (or in-place with two-pass reversal)
        Time: O(n), Space: O(n)
        
        TODO: Handle multiple spaces and leading/trailing spaces
        """
        words = s.split()
        return ' '.join(reversed(words))
    
    def reverse_words_simple(self, s: str) -> str:
        """
        Basic: Reverse individual words in a string (keep word order).
        
        Example:
        Input: s = "hello world"
        Output: "olleh dlrow"
        
        Time: O(n), Space: O(n)
        
        TODO: Reverse each word individually
        """
        return ' '.join(word[::-1] for word in s.split())
    
    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Basic: Find longest common prefix among strings.
        
        Example:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        
        Approaches: Vertical scanning, horizontal scanning, or binary search
        Time: O(S) where S is sum of all characters, Space: O(1)
        
        TODO: Compare characters position by position
        """
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    
    def valid_anagram(self, s: str, t: str) -> bool:
        """
        Basic: Check if two strings are anagrams.
        
        Example:
        Input: s = "anagram", t = "nagaram"
        Output: True
        
        Approaches: Sort, frequency count, or character array
        Time: O(n), Space: O(1)
        
        TODO: Compare character frequencies
        """
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        
        return len(count) == 0
    
    def first_unique_character(self, s: str) -> int:
        """
        Basic: Find index of first unique character.
        
        Example:
        Input: s = "leetcode"
        Output: 0 (character 'l')
        
        Approach: Two-pass with frequency counting
        Time: O(n), Space: O(1) for lowercase letters
        
        TODO: Count frequencies, then find first unique
        """
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
    
    def remove_duplicates(self, s: str) -> str:
        """
        Basic: Remove duplicate characters while maintaining order.
        
        Example:
        Input: s = "programming"
        Output: "progamin"
        
        Time: O(n), Space: O(k) where k is unique characters
        
        TODO: Use set to track seen characters
        """
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
    def is_rotation(self, s1: str, s2: str) -> bool:
        """
        Basic: Check if one string is rotation of another.
        
        Example:
        Input: s1 = "waterbottle", s2 = "erbottlewat"
        Output: True
        
        Insight: s2 is rotation of s1 if s2 is substring of s1+s1
        Time: O(n), Space: O(n)
        
        TODO: Check if s2 appears in s1+s1
        """
        if len(s1) != len(s2):
            return False
        return s2 in s1 + s1
    
    # SUBSTRING AND SLIDING WINDOW EXERCISES
    
    def find_all_substrings(self, s: str) -> List[str]:
        """
        Basic: Generate all possible substrings.
        
        Example:
        Input: s = "abc"
        Output: ["a", "ab", "abc", "b", "bc", "c"]
        
        Time: O(n³), Space: O(n³)
        
        TODO: Use nested loops to generate all substrings
        """
        result = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                result.append(s[i:j])
        return result
    
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        Basic: Check if s is subsequence of t.
        
        Example:
        Input: s = "ace", t = "abcde"
        Output: True
        
        Time: O(n), Space: O(1)
        
        TODO: Use two pointers to match characters
        """
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)
    
    # PATTERN MATCHING EXERCISES
    
    def implement_strstr(self, haystack: str, needle: str) -> int:
        """
        Medium: Find first occurrence of needle in haystack.
        
        Example:
        Input: haystack = "hello", needle = "ll"
        Output: 2
        
        Approaches: Brute force O(nm), KMP O(n+m), or built-in
        Time: O(n+m) with KMP, Space: O(m)
        
        TODO: Implement efficient string search (KMP recommended)
        """
        if not needle:
            return 0
        return haystack.find(needle)
    
    def kmp_pattern_search(self, text: str, pattern: str) -> List[int]:
        """
        Medium: Find all occurrences using KMP algorithm.
        
        Example:
        Input: text = "ababcababa", pattern = "abab"
        Output: [0, 5] (starting indices)
        
        Approach: Build failure function, then search
        Time: O(n+m), Space: O(m)
        
        TODO: Implement KMP with failure function
        """
        pass
    
    def rabin_karp_search(self, text: str, pattern: str) -> List[int]:
        """
        Medium: Find all occurrences using Rabin-Karp rolling hash.
        
        Example:
        Input: text = "abcdefg", pattern = "cde"
        Output: [2]
        
        Approach: Rolling hash with collision detection
        Time: O(n+m) average, O(nm) worst case, Space: O(1)
        
        TODO: Implement rolling hash pattern matching
        """
        pass
    
    def z_algorithm(self, s: str) -> List[int]:
        """
        Advanced: Compute Z-array for string.
        
        Z[i] = length of longest substring starting at i that is prefix of s
        
        Example:
        Input: s = "aaabaaab"
        Output: [8, 2, 1, 0, 3, 2, 1, 0]
        
        Approach: Linear algorithm with Z-boxes
        Time: O(n), Space: O(n)
        
        TODO: Implement Z-algorithm efficiently
        """
        pass
    
    # SUBSTRING EXERCISES
    
    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Medium: Longest substring without repeating characters.
        
        Example:
        Input: s = "abcabcbb"
        Output: 3 ("abc")
        
        Approach: Sliding window with set or frequency map
        Time: O(n), Space: O(min(m,n))
        
        TODO: Use sliding window technique
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def minimum_window_substring(self, s: str, t: str) -> str:
        """
        Hard: Minimum window substring containing all characters of t.
        
        Example:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        
        Approach: Sliding window with frequency tracking
        Time: O(|s| + |t|), Space: O(|s| + |t|)
        
        TODO: Use two pointers with character frequency maps
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(target_count)
        formed = 0
        window_count = {}
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
    
    def longest_palindromic_substring(self, s: str) -> str:
        """
        Medium: Find longest palindromic substring.
        
        Example:
        Input: s = "babad"
        Output: "bab" or "aba"
        
        Approaches: Expand around centers O(n²), Manacher's O(n), or DP O(n²)
        Time: O(n) with Manacher's, Space: O(n)
        
        TODO: Implement expand around centers or Manacher's algorithm
        """
        pass
    
    def palindromic_substrings_count(self, s: str) -> int:
        """
        Medium: Count total palindromic substrings.
        
        Example:
        Input: s = "abc"
        Output: 3 ("a", "b", "c")
        
        Approach: Expand around centers
        Time: O(n²), Space: O(1)
        
        TODO: Count palindromes by expanding around each center
        """
        pass
    
    # ADVANCED STRING ALGORITHMS
    
    def edit_distance(self, word1: str, word2: str) -> int:
        """
        Hard: Minimum edit distance (Levenshtein distance).
        
        Example:
        Input: word1 = "horse", word2 = "ros"
        Output: 3 (horse -> rorse -> rose -> ros)
        
        Operations: insert, delete, replace
        Approach: Dynamic programming
        Time: O(mn), Space: O(mn) or O(min(m,n))
        
        TODO: Use DP to find minimum operations
        """
        pass
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Medium: Length of longest common subsequence.
        
        Example:
        Input: text1 = "abcde", text2 = "ace"
        Output: 3 ("ace")
        
        Approach: Dynamic programming
        Time: O(mn), Space: O(mn) or O(min(m,n))
        
        TODO: Use DP table to find LCS length
        """
        pass
    
    def longest_common_substring(self, text1: str, text2: str) -> int:
        """
        Medium: Length of longest common substring.
        
        Example:
        Input: text1 = "abcdxyz", text2 = "xyzabcd"
        Output: 4 ("abcd")
        
        Approach: Dynamic programming or suffix array
        Time: O(mn), Space: O(mn) or O(min(m,n))
        
        TODO: Use DP to find longest common substring
        """
        pass
    
    def suffix_array(self, s: str) -> List[int]:
        """
        Advanced: Build suffix array efficiently.
        
        Example:
        Input: s = "banana"
        Output: [5, 3, 1, 0, 4, 2] (indices of sorted suffixes)
        
        Approaches: O(n²logn) naive, O(nlogn) with radix sort
        Time: O(nlogn), Space: O(n)
        
        TODO: Implement efficient suffix array construction
        """
        pass
    
    # STRING MATCHING AND PARSING
    
    def regular_expression_matching(self, s: str, p: str) -> bool:
        """
        Hard: Regular expression matching with '.' and '*'.
        
        Example:
        Input: s = "aa", p = "a*"
        Output: True
        
        Approach: Dynamic programming or recursion with memoization
        Time: O(mn), Space: O(mn)
        
        TODO: Handle '.' (any char) and '*' (zero or more)
        """
        pass
    
    def wildcard_matching(self, s: str, p: str) -> bool:
        """
        Hard: Wildcard pattern matching with '?' and '*'.
        
        Example:
        Input: s = "aa", p = "*"
        Output: True
        
        Approach: Dynamic programming or greedy
        Time: O(mn), Space: O(mn)
        
        TODO: Handle '?' (single char) and '*' (any sequence)
        """
        pass
    
    def decode_string(self, s: str) -> str:
        """
        Medium: Decode string with pattern k[encoded_string].
        
        Example:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        
        Approach: Stack for nested patterns
        Time: O(maxK * n), Space: O(m) where m is length of result
        
        TODO: Use stack to handle nested encoding
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                current_string += char
        
        return current_string
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Medium: Group strings that are anagrams.
        
        Example:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        Approach: Hash by sorted string or character count
        Time: O(n * k log k), Space: O(n * k)
        
        TODO: Use sorted string as grouping key
        """
        anagram_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]
        return list(anagram_map.values())
    
    # COMPRESSION AND ENCODING
    
    def run_length_encoding(self, s: str) -> str:
        """
        Basic: Compress string using run-length encoding.
        
        Example:
        Input: s = "aabcccccaaa"
        Output: "a2b1c5a3"
        
        Approach: Count consecutive characters
        Time: O(n), Space: O(1) extra
        
        TODO: Count and encode consecutive character runs
        """
        if not s:
            return ""
        
        result = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result.append(s[i-1] + str(count))
                count = 1
        
        result.append(s[-1] + str(count))
        return ''.join(result)
    
    def run_length_decoding(self, s: str) -> str:
        """
        Basic: Decode run-length encoded string.
        
        Example:
        Input: s = "a2b1c5a3"
        Output: "aabcccccaaa"
        
        Time: O(n), Space: O(output_length)
        
        TODO: Parse count and character pairs to reconstruct string
        """
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            count = int(s[i + 1])
            result.append(char * count)
            i += 2
        return ''.join(result)
    
    def string_compression(self, chars: List[str]) -> int:
        """
        Medium: Compress character array in-place.
        
        Example:
        Input: chars = ["a","a","b","b","c","c","c"]
        Output: 6, chars = ["a","2","b","2","c","3"]
        
        Approach: Two pointers for in-place modification
        Time: O(n), Space: O(1)
        
        TODO: Modify array in-place with character counts
        """
        pass
    
    def huffman_coding_tree(self, text: str) -> Dict[str, str]:
        """
        Advanced: Build Huffman coding tree for text compression.
        
        Example:
        Input: text = "abracadabra"
        Output: Dictionary mapping characters to binary codes
        
        Approach: Priority queue to build optimal prefix tree
        Time: O(n log k), Space: O(k) where k is unique characters
        
        TODO: Build frequency table, then Huffman tree
        """
        pass
    
    # REAL-WORLD STRING PROBLEMS
    
    def validate_ip_address(self, ip: str) -> str:
        """
        Medium: Validate if string is valid IPv4 or IPv6 address.
        
        Example:
        Input: ip = "192.168.1.1"
        Output: "IPv4"
        
        Time: O(1), Space: O(1)
        
        TODO: Check format and range constraints for both IP types
        """
        pass
    
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        """
        Medium: Check if string can be segmented into dictionary words.
        
        Example:
        Input: s = "leetcode", word_dict = ["leet", "code"]
        Output: True
        
        Time: O(n²), Space: O(n)
        
        TODO: Use DP to check if prefixes can be segmented
        """
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
    def word_break_ii(self, s: str, word_dict: List[str]) -> List[str]:
        """
        Hard: Return all possible word break combinations.
        
        Example:
        Input: s = "catsanddog", word_dict = ["cat", "cats", "and", "sand", "dog"]
        Output: ["cats and dog", "cat sand dog"]
        
        Time: O(2^n) worst case, Space: O(2^n)
        
        TODO: Use DP with backtracking to generate all combinations
        """
        pass
    
    def text_justification(self, words: List[str], max_width: int) -> List[str]:
        """
        Hard: Format text with full justification.
        
        Example:
        Input: words = ["This", "is", "an", "example"], max_width = 16
        Output: ["This    is    an", "example         "]
        
        Time: O(n), Space: O(m) where m is max_width
        
        TODO: Pack words into lines and distribute spaces evenly
        """
        pass
    
    def basic_calculator(self, s: str) -> int:
        """
        Hard: Implement basic calculator for string expressions.
        
        Example:
        Input: s = "1 + 1"
        Output: 2
        
        Time: O(n), Space: O(n)
        
        TODO: Use stack to handle operator precedence
        """
        pass