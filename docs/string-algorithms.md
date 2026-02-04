# String Algorithms: Where Text Processing Gets Serious

String algorithms might seem like a niche topic, but they power everything from DNA sequencing to web search engines. They're the unsung heroes behind text editors, plagiarism detection, and data compression. Plus, they make for some of the most elegant algorithm designs you'll encounter.

## The Deceptive Complexity of Strings

At first glance, strings seem simple—just arrays of characters. But this simplicity is misleading. Consider the "find needle in haystack" problem. The naive approach seems obvious:

```python
def naive_search(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            matches.append(i)
    return matches
```

This works, but it's O(nm) where n is the text length and m is the pattern length. For large texts, this becomes painfully slow.

The beauty of string algorithms lies in exploiting patterns and structure to do much better.

## The Foundation: Pattern Matching

### KMP Algorithm: The Art of Not Backtracking

The Knuth-Morris-Pratt algorithm is based on a crucial insight: when a mismatch occurs, you don't need to start over from the beginning. You can use information from the partial match to skip ahead intelligently.

```python
def build_failure_function(pattern):
    """Build the failure function for KMP."""
    m = len(pattern)
    failure = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        failure[i] = j
    
    return failure

def kmp_search(text, pattern):
    if not pattern:
        return []
    
    failure = build_failure_function(pattern)
    matches = []
    j = 0
    
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]  # The magic skip
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            matches.append(i - j + 1)
            j = failure[j - 1]
    
    return matches
```

**The insight**: The failure function tells you how far you can skip without missing any matches. It's precomputed based on the pattern's internal structure.

### Rabin-Karp: When Hashing Meets Rolling

Rabin-Karp uses a rolling hash to compare substrings in O(1) time:

```python
def rabin_karp_search(text, pattern):
    if len(pattern) > len(text):
        return []
    
    base = 256
    mod = 10**9 + 7
    
    # Calculate hash of pattern and first window
    pattern_hash = 0
    window_hash = 0
    power = 1
    
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
        if i < len(pattern) - 1:
            power = (power * base) % mod
    
    matches = []
    
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash:
            # Hash match - verify with actual comparison
            if text[i:i+len(pattern)] == pattern:
                matches.append(i)
        
        # Roll the hash to next window
        if i < len(text) - len(pattern):
            window_hash = (window_hash - ord(text[i]) * power) % mod
            window_hash = (window_hash * base + ord(text[i + len(pattern)])) % mod
            window_hash = (window_hash + mod) % mod  # Handle negative
    
    return matches
```

**The insight**: Instead of recomputing the hash for each substring, "roll" it by removing the first character and adding the next one.

## Advanced String Structures

### Z-Algorithm: Self-Comparison Mastery

The Z-algorithm computes, for each position i, the length of the longest substring starting from i that is also a prefix of the string.

```python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    
    return z
```

**The magic**: The Z-algorithm maintains a "Z-box" [left, right] representing the rightmost segment that's also a prefix. This lets it reuse previous computations.

### Suffix Arrays: The Heavy Artillery

For problems involving multiple pattern searches on the same text, suffix arrays provide powerful preprocessing:

```python
def build_suffix_array(text):
    """Build suffix array using simple sorting (not optimal but clear)."""
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def search_with_suffix_array(text, suffix_array, pattern):
    """Binary search on suffix array."""
    def compare_pattern(idx):
        return text[idx:idx+len(pattern)]
    
    left, right = 0, len(suffix_array)
    
    # Find leftmost occurrence
    while left < right:
        mid = (left + right) // 2
        if compare_pattern(suffix_array[mid]) < pattern:
            left = mid + 1
        else:
            right = mid
    
    start = left
    right = len(suffix_array)
    
    # Find rightmost occurrence
    while left < right:
        mid = (left + right) // 2
        if compare_pattern(suffix_array[mid]) <= pattern:
            left = mid + 1
        else:
            right = mid
    
    end = left
    
    return [suffix_array[i] for i in range(start, end)]
```

## String Distance and Similarity

### Edit Distance: The Rosetta Stone

Edit distance (Levenshtein distance) measures how different two strings are:

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert  
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]
```

**The insight**: Build up the solution by considering all possible operations at each step.

### Longest Common Subsequence

Not to be confused with substring—subsequence allows gaps:

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

## Palindrome Algorithms

### Manacher's Algorithm: Linear Time Palindrome Detection

Finding all palindromic substrings naively takes O(n²), but Manacher's algorithm does it in O(n):

```python
def manacher(s):
    # Transform string to handle even-length palindromes
    transformed = '#'.join('^{}$'.format(s))
    n = len(transformed)
    P = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Try to expand palindrome centered at i
        while transformed[i + (1 + P[i])] == transformed[i - (1 + P[i])]:
            P[i] += 1
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    return P
```

**The insight**: Use symmetry properties of palindromes to avoid redundant comparisons.

## Practical Applications

### Text Compression: Where Patterns Pay Off

```python
def simple_lz_compression(text):
    """Simplified LZ-style compression."""
    compressed = []
    i = 0
    
    while i < len(text):
        # Look for the longest match in previous text
        max_length = 0
        max_distance = 0
        
        for distance in range(1, min(i + 1, 256)):  # Limited lookback
            match_length = 0
            while (i + match_length < len(text) and 
                   text[i + match_length] == text[i - distance + match_length]):
                match_length += 1
            
            if match_length > max_length:
                max_length = match_length
                max_distance = distance
        
        if max_length > 2:  # Worth compressing
            compressed.append(('ref', max_distance, max_length))
            i += max_length
        else:
            compressed.append(('lit', text[i]))
            i += 1
    
    return compressed
```

### DNA Sequence Analysis

```python
def find_orfs(dna_sequence):
    """Find Open Reading Frames in DNA sequence."""
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []
    
    for frame in range(3):  # Three reading frames
        i = frame
        while i < len(dna_sequence) - 2:
            if dna_sequence[i:i+3] == start_codon:
                # Found start codon, look for stop codon
                start = i
                i += 3
                while i < len(dna_sequence) - 2:
                    codon = dna_sequence[i:i+3]
                    if codon in stop_codons:
                        orfs.append((start, i + 3, frame))
                        break
                    i += 3
            else:
                i += 3
    
    return orfs
```

## Performance Considerations

### When to Use What

- **KMP**: When you need guaranteed O(n+m) time and have space for preprocessing
- **Rabin-Karp**: When dealing with multiple patterns or rolling hash fits naturally
- **Boyer-Moore**: When patterns are long and alphabet is large (great for text search)
- **Suffix Arrays**: When doing many searches on the same text

### Memory vs. Time Trade-offs

String algorithms often involve trade-offs:

- **Suffix arrays**: O(n) space, fast multiple searches
- **KMP**: O(m) preprocessing space, O(n+m) time
- **Rolling hash**: O(1) extra space, probabilistic correctness

## Common Gotchas

### Unicode and Character Encoding
```python
# This might not work as expected with Unicode
if char >= 'a' and char <= 'z':

# Better approach
if char.islower():
```

### Case Sensitivity
```python
def case_insensitive_search(text, pattern):
    return kmp_search(text.lower(), pattern.lower())
```

### String Immutability
In languages like Python and Java, strings are immutable. Building strings character by character can be inefficient:

```python
# Inefficient
result = ""
for char in text:
    result += char.upper()

# Better
result = ''.join(char.upper() for char in text)
```

## Practice Strategy

The exercises are designed to build confidence through progressive difficulty:

1. **Start with fundamentals**: Character counting, string reversal, basic palindromes
2. **Build manipulation skills**: Space handling, permutations, simple compressions
3. **Master sliding windows**: Substring problems with constraints
4. **Learn classic algorithms**: KMP, Rabin-Karp, Manacher's
5. **Practice dynamic programming**: Edit distance, LCS, word break
6. **Tackle advanced patterns**: Multi-pattern search, complex transformations

### Learning Progression

- **Basic exercises** build confidence with fundamental string operations
- **Intermediate problems** introduce algorithmic patterns and optimizations  
- **Advanced challenges** require combining multiple techniques
- **Real-world problems** demonstrate practical applications

### Solutions and Hints

- Exercise files contain only TODO hints to encourage independent thinking
- Detailed solutions for medium/hard problems are in `docs/solutions/string-algorithms-solutions.md`
- Solutions focus on explaining the "why" behind each approach
- Multiple approaches are discussed when applicable

## Extended Exercise Categories

The string algorithms exercises now include progressive difficulty levels:

### Warm-up Problems
- Character frequency counting
- String reversal techniques
- Basic palindrome checking
- Simple string manipulations

### String Manipulation Patterns
- Space replacement and in-place modifications
- String permutation and rotation detection
- One edit distance checking
- Basic string compression

### Advanced Pattern Matching
- Boyer-Moore algorithm
- Aho-Corasick multi-pattern search
- Suffix array construction and search
- Pattern matching with wildcards

### Sliding Window on Strings
- Longest substring variations
- Character replacement problems
- Anagram finding in strings
- Window-based string analysis

### Dynamic Programming on Strings
- String interleaving problems
- Subsequence counting
- Word break variations
- Complex edit operations

### Real-World String Problems
- IP address validation
- Text justification
- Expression parsing
- Path simplification

## Common Interview Problems

The expanded exercise set covers these essential patterns:

- **Longest palindromic substring** (with Manacher's algorithm)
- **Valid anagram / group anagrams** (with shifted string grouping)
- **Minimum window substring** (classic sliding window)
- **String compression** (run-length encoding variations)
- **Pattern matching with wildcards** (simplified regex)
- **Edit distance** (with operation tracking)
- **Word break problems** (DP with backtracking)
- **One edit away** (string similarity)
- **String interleaving** (advanced DP)

## Final Thoughts

String algorithms reveal a fundamental truth: what seems simple on the surface often hides deep complexity. The naive approaches work for small inputs but break down at scale.

The elegant solutions—KMP's failure function, Manacher's palindrome detection, suffix arrays—all share a common theme: they exploit structure and patterns to avoid redundant work.

Modern applications of string algorithms are everywhere: search engines use sophisticated pattern matching, DNA sequencing relies on string alignment algorithms, and data compression algorithms are essentially advanced pattern recognition.

The investment in understanding these algorithms pays dividends beyond just passing interviews—they change how you think about text processing and pattern recognition in general.

---

*Next up: Sorting Algorithms - where organizing data becomes an art form.*