# The Blind 150: Your Roadmap to Interview Success

The Blind 150 is a curated list of LeetCode problems that represents the core of technical interview preparation. Unlike random problem-solving, this collection is specifically designed to cover the essential patterns and techniques that appear repeatedly in actual interviews at top tech companies.

## Why the Blind 150 Matters

The name comes from the Blind app (anonymous professional network), where experienced engineers identified the most important problems for interview preparation. This isn't just another problem list—it's battle-tested by people who've both given and received thousands of interviews.

**The key insight**: You don't need to solve 1000 problems. You need to deeply understand the patterns that appear in the most important problems.

## The Strategic Approach

### Understanding vs. Memorization

The goal isn't to memorize solutions—it's to internalize patterns. When you see a new problem, you should recognize it as a variation of patterns you already know.

```python
# Don't memorize this specific solution
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Instead, understand this pattern:
# "Use a hash map to store complements for O(1) lookup"
# This pattern applies to many problems beyond Two Sum
```

## The Core Categories

### Array & Hashing (9 problems)

These problems teach fundamental data structure usage and optimization techniques:

- **Two Sum**: Hash map for complement lookup
- **Valid Anagram**: Character frequency counting
- **Group Anagrams**: Using sorted strings as keys
- **Top K Frequent**: Heap or bucket sort techniques
- **Product of Array Except Self**: Prefix/suffix products
- **Valid Sudoku**: Set-based validation
- **Longest Consecutive Sequence**: Union-find or set techniques

**The pattern**: Transform problems into hash map lookups or frequency counting.

### Two Pointers (5 problems)

Master the art of traversing arrays with multiple pointers:

- **Valid Palindrome**: Start from ends, move inward
- **Two Sum II**: Use sorted array property
- **3Sum**: Fix one element, use two pointers for the rest
- **Container With Most Water**: Greedy pointer movement
- **Trapping Rain Water**: Two pointers with height tracking

**The pattern**: When you need to examine pairs or find optimal combinations in sorted/sortable data.

### Sliding Window (6 problems)

Learn to optimize substring/subarray problems from O(n²) to O(n):

- **Best Time to Buy and Sell Stock**: Track minimum and maximum profit
- **Longest Substring Without Repeating Characters**: Expand/contract window
- **Longest Repeating Character Replacement**: Window with character frequency
- **Permutation in String**: Fixed-size window with frequency matching
- **Minimum Window Substring**: Variable window with coverage tracking
- **Sliding Window Maximum**: Monotonic deque

**The pattern**: Maintain a window that satisfies certain properties, expand/contract as needed.

### Stack (7 problems)

Understand LIFO operations and their applications:

- **Valid Parentheses**: Stack for matching pairs
- **Min Stack**: Auxiliary stack or single stack with pairs
- **Evaluate Reverse Polish Notation**: Stack for operand management
- **Generate Parentheses**: Backtracking with stack-like validation
- **Daily Temperatures**: Monotonic stack for next greater element
- **Car Fleet**: Stack for time-based collision detection
- **Largest Rectangle in Histogram**: Stack for boundary detection

**The pattern**: When you need to process nested structures or find the next/previous greater/smaller element.

## Learning Strategy by Difficulty

### Easy Problems: Build Foundation

Start here to understand basic patterns:

```python
# Two Sum - foundational hash map pattern
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# This teaches: hash map for O(1) lookups, complement technique
```

**Focus**: Understand the underlying pattern, not just the solution.

### Medium Problems: Pattern Recognition

These teach you to combine patterns:

```python
# 3Sum - combines sorting with two pointers
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
            continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result
```

**This teaches**: How to combine multiple patterns (sorting + two pointers + duplicate handling).

### Hard Problems: Complex Applications

These require combining multiple advanced techniques:

```python
# Minimum Window Substring - combines sliding window with hash map
def min_window(s, t):
    if not s or not t:
        return ""
    
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)
    left = right = 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

**This teaches**: How to manage complex state (multiple hash maps, counters) while maintaining sliding window invariants.

## Study Methodology

### Phase 1: Pattern Absorption (4-6 weeks)

1. **Solve by category**: Don't mix topics initially
2. **Time yourself**: Start with unlimited time, gradually reduce
3. **Write out patterns**: Document the technique after solving
4. **Code from scratch**: Don't look at hints initially

### Phase 2: Mixed Practice (2-3 weeks)

1. **Random selection**: Mix problems from different categories
2. **Timed practice**: 25-30 minutes per medium problem
3. **Mock interviews**: Use platforms like Pramp or interviewing.io
4. **Pattern identification**: Quickly categorize new problems

### Phase 3: Company-Specific Prep (1-2 weeks)

1. **Research company preferences**: Some companies favor certain types
2. **Mock interviews**: Focus on communication and optimization
3. **Edge case mastery**: Practice handling corner cases quickly
4. **System design**: For senior roles, complement with system design

## The Mental Models

### Problem Classification Framework

When you see a new problem, ask:

1. **What's the input structure?** (Array, string, tree, graph)
2. **What's the constraint?** (Sorted, distinct values, positive numbers)
3. **What's the objective?** (Find, count, optimize, validate)
4. **What's the pattern?** (Two pointers, sliding window, DP, etc.)

### Optimization Progression

Most problems follow this optimization path:

1. **Brute force**: O(n³) or worse - understand the problem
2. **Better approach**: O(n²) - eliminate one dimension
3. **Optimal approach**: O(n log n) or O(n) - use proper data structures
4. **Space optimization**: Reduce space complexity if possible

## Common Anti-Patterns

### Premature Optimization

Don't jump to the optimal solution immediately:

```python
# Start with this (brute force)
def contains_duplicate_v1(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Then optimize to this
def contains_duplicate_v2(nums):
    return len(nums) != len(set(nums))
```

### Over-Engineering

Keep solutions simple and readable:

```python
# Over-engineered
def two_sum_complex(nums, target):
    class Solution:
        def __init__(self):
            self.memo = {}
        
        def helper(self, nums, target, start=0):
            # Complex recursive solution...
            pass
    
    return Solution().helper(nums, target)

# Simple and correct
def two_sum_simple(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

## Interview Day Strategy

### The 4-Step Approach

1. **Clarify** (2-3 minutes): Ask about constraints, edge cases, examples
2. **Plan** (5-7 minutes): Discuss approach, time/space complexity
3. **Code** (15-20 minutes): Implement while explaining
4. **Test** (3-5 minutes): Walk through examples, edge cases

### Communication Template

```
"Looking at this problem, I notice [pattern recognition].
This seems like a [category] problem.
Let me think about the constraints... [analysis]
I think I can solve this using [technique] in [time complexity].
Let me code this up... [implementation with explanation]
Now let me test with the given example... [verification]
```

## Tracking Progress

### Metrics That Matter

- **First-time solve rate**: Aim for 70%+ on mediums
- **Time to solution**: 25-30 minutes for mediums
- **Pattern recognition speed**: <2 minutes to identify approach
- **Bug-free coding**: Minimize syntax and logic errors

### Spaced Repetition

- **Day 1**: Solve the problem
- **Day 3**: Solve again from memory
- **Day 7**: Solve again, focusing on optimization
- **Day 21**: Final review, ensure pattern is internalized

## Beyond the 150

### When You're Ready

You've mastered the Blind 150 when:

1. You can identify patterns within 1-2 minutes
2. You code solutions with minimal bugs
3. You can explain time/space complexity confidently
4. You handle edge cases naturally

### Next Steps

1. **Company-specific problems**: Research your target companies
2. **System design**: Essential for senior roles
3. **Behavioral prep**: Don't neglect the non-technical side
4. **Mock interviews**: Practice the complete interview experience

## Final Thoughts

The Blind 150 isn't just a checklist—it's a curriculum for developing algorithmic thinking. Each problem teaches you to see patterns, make trade-offs, and communicate technical ideas clearly.

The journey is challenging, but it's also transformative. You'll emerge not just as someone who can solve interview problems, but as a better engineer who thinks more clearly about algorithms, data structures, and optimization.

Remember: the goal isn't to memorize 150 solutions. It's to internalize the problem-solving patterns that these problems represent. When you achieve that, you'll be ready for any interview question that comes your way.

The patterns you learn here will serve you throughout your career, long after the interviews are over.

---

*Next up: The individual problem categories with detailed pattern breakdowns and practice strategies.*