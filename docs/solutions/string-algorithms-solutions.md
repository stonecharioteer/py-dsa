# String Algorithms - Detailed Solutions

This document provides detailed solutions for medium and hard string algorithm problems. These solutions focus on building understanding rather than just providing code.

## Problem: One Edit Distance

### Problem Statement
Check if two strings are exactly one edit away from each other. An edit can be an insertion, deletion, or replacement of a character.

### Approach
The key insight is to handle three cases based on the length difference:
1. If length difference > 1, return False immediately
2. If lengths are equal, check for exactly one replacement
3. If lengths differ by 1, check for exactly one insertion/deletion

### Implementation
```python
def one_edit_distance(self, s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    
    # Ensure s1 is shorter or equal length
    if m > n:
        return self.one_edit_distance(s2, s1)
    
    # If length difference > 1, impossible
    if n - m > 1:
        return False
    
    for i in range(m):
        if s1[i] != s2[i]:
            if m == n:  # Same length - check replacement
                return s1[i+1:] == s2[i+1:]
            else:  # Different length - check deletion from s2
                return s1[i:] == s2[i+1:]
    
    # All characters match, valid only if lengths differ by 1
    return n - m == 1
```

### Time/Space Complexity
- Time: O(min(m,n)) where m,n are string lengths
- Space: O(1) excluding substring comparisons

### Key Insights
- Handle the three edit cases systematically
- Early termination when length difference is too large
- Normalize by ensuring one string is shorter

## Problem: Minimum Window Substring

### Problem Statement
Find the minimum window in string s that contains all characters of string t.

### Approach
Use the sliding window technique with two pointers:
1. Expand right pointer to include characters until we have a valid window
2. Contract left pointer to minimize window while maintaining validity
3. Track character frequencies to determine window validity

### Implementation
```python
def minimum_window_substring(self, s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters in t
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1
    
    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(target_count)  # Number of unique chars in t
    formed = 0  # Number of unique chars in current window with desired frequency
    
    window_count = {}
    
    for right in range(len(s)):
        # Add character from right to window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if this character contributes to forming a valid window
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        
        # Contract window from left
        while left <= right and formed == required:
            # Update minimum window if current is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove leftmost character
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]
```

### Time/Space Complexity
- Time: O(|s| + |t|) - each character visited at most twice
- Space: O(|s| + |t|) for the hash maps

### Key Insights
- Two-pointer sliding window technique
- Track both target frequencies and current window frequencies
- The "formed" counter optimizes validity checking

## Problem: Longest Palindromic Substring (Manacher's Algorithm)

### Problem Statement
Find the longest palindromic substring in linear time using Manacher's algorithm.

### Approach
Manacher's algorithm preprocesses the string to handle even-length palindromes, then uses previously computed information to avoid redundant comparisons.

### Implementation
```python
def longest_palindromic_substring(self, s: str) -> str:
    if not s:
        return ""
    
    # Transform string to handle even-length palindromes
    transformed = '#'.join('^{}$'.format(s))
    n = len(transformed)
    P = [0] * n  # P[i] = length of palindrome centered at i
    center = right = 0  # Current rightmost palindrome info
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within current rightmost palindrome,
        # we can use previously computed information
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Try to expand palindrome centered at i
        while transformed[i + (1 + P[i])] == transformed[i - (1 + P[i])]:
            P[i] += 1
        
        # If palindrome centered at i extends past right,
        # adjust center and right
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    # Find the longest palindrome
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
    
    # Extract the palindrome from original string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]
```

### Time/Space Complexity
- Time: O(n) - each position visited at most once in expansion
- Space: O(n) for the transformed string and P array

### Key Insights
- String transformation handles even/odd length palindromes uniformly
- Use symmetry to avoid redundant character comparisons
- The algorithm amortizes to linear time despite nested loops

## Problem: Edit Distance with Operations

### Problem Statement
Return the actual sequence of edit operations to transform one string into another, not just the minimum count.

### Approach
Use dynamic programming to build the edit distance table, then backtrack to reconstruct the actual operations performed.

### Implementation
```python
def edit_distance_with_operations(self, word1: str, word2: str) -> List[str]:
    m, n = len(word1), len(word2)
    
    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    # Backtrack to find operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            # Characters match, no operation needed
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            # Replace operation
            operations.append(f"replace {word1[i-1]}->{word2[j-1]} at pos {i-1}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            # Delete operation
            operations.append(f"delete {word1[i-1]} at pos {i-1}")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            # Insert operation
            operations.append(f"insert {word2[j-1]} at pos {i}")
            j -= 1
    
    return operations[::-1]  # Reverse to get correct order
```

### Time/Space Complexity
- Time: O(mn) for DP + O(m+n) for backtracking
- Space: O(mn) for the DP table

### Key Insights
- The DP table stores optimal costs, backtracking recovers the actual path
- Three cases in backtracking correspond to three possible operations
- Operations are collected in reverse order during backtracking

## Problem: KMP Pattern Search

### Problem Statement
Implement the Knuth-Morris-Pratt algorithm for efficient pattern matching.

### Approach
Build a failure function that captures the pattern's internal structure, then use it to skip characters intelligently during matching.

### Implementation
```python
def build_failure_function(self, pattern: str) -> List[int]:
    """Build the failure function for KMP."""
    m = len(pattern)
    failure = [0] * m
    j = 0
    
    for i in range(1, m):
        # Look for longest proper prefix that is also suffix
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        failure[i] = j
    
    return failure

def kmp_pattern_search(self, text: str, pattern: str) -> List[int]:
    if not pattern:
        return []
    
    failure = self.build_failure_function(pattern)
    matches = []
    j = 0  # Index in pattern
    
    for i in range(len(text)):
        # Handle mismatch by using failure function
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        # Found complete match
        if j == len(pattern):
            matches.append(i - j + 1)
            j = failure[j - 1]  # Look for overlapping matches
    
    return matches
```

### Time/Space Complexity
- Time: O(n + m) where n is text length, m is pattern length
- Space: O(m) for the failure function

### Key Insights
- The failure function encodes how much of the pattern can be "reused" after a mismatch
- Never need to backtrack in the text - only adjust pattern position
- Works by exploiting the pattern's internal repetitive structure

## Problem: Rabin-Karp Rolling Hash

### Problem Statement
Implement pattern matching using rolling hash for average case O(n+m) time.

### Approach
Use a polynomial rolling hash that can be updated in O(1) time as the window slides.

### Implementation
```python
def rabin_karp_search(self, text: str, pattern: str) -> List[int]:
    if len(pattern) > len(text):
        return []
    
    base = 256
    mod = 10**9 + 7
    m = len(pattern)
    n = len(text)
    
    # Calculate hash of pattern and first window
    pattern_hash = 0
    window_hash = 0
    power = 1
    
    # Calculate base^(m-1) % mod for rolling hash
    for i in range(m - 1):
        power = (power * base) % mod
    
    # Calculate initial hashes
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    
    matches = []
    
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == window_hash:
            # Hash collision possible - verify with actual comparison
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            # Remove leading character and add new trailing character
            window_hash = (window_hash - ord(text[i]) * power) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            # Handle negative values
            window_hash = (window_hash + mod) % mod
    
    return matches
```

### Time/Space Complexity
- Time: O(n+m) average case, O(nm) worst case (many hash collisions)
- Space: O(1)

### Key Insights
- Rolling hash allows O(1) window updates
- Hash collisions require string verification
- Choice of base and modulus affects collision probability

## Problem: Word Break II

### Problem Statement
Return all possible ways to break a string into dictionary words.

### Approach
Use dynamic programming with memoization to avoid recomputing the same subproblems.

### Implementation
```python
def word_break_ii(self, s: str, word_dict: List[str]) -> List[str]:
    word_set = set(word_dict)
    memo = {}
    
    def backtrack(start: int) -> List[str]:
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                # Recursively break the rest of the string
                rest_combinations = backtrack(end)
                for combination in rest_combinations:
                    if combination:
                        result.append(word + " " + combination)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return backtrack(0)
```

### Time/Space Complexity
- Time: O(2^n) worst case (exponential in string length)
- Space: O(2^n) for storing all combinations

### Key Insights
- Memoization prevents recomputing the same suffix multiple times
- The problem has overlapping subproblems making DP applicable
- Exponential time is unavoidable due to potentially exponential number of solutions

These solutions demonstrate key algorithmic patterns in string processing: sliding window, dynamic programming, preprocessing for efficiency, and leveraging string structure for optimization.