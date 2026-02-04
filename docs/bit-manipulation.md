# Bit Manipulation: The Art of Thinking in Binary

Bit manipulation is the closest you'll get to the metal in high-level programming. It's where elegant mathematical insights meet brutal efficiency, where a single clever bit trick can replace dozens of lines of conventional code. Master these techniques, and you'll unlock optimizations that seem like magic to those who don't understand them.

## Why Bits Matter More Than Ever

In an era of high-level abstractions, why should you care about individual bits? Several reasons:

1. **Performance**: Bit operations are among the fastest operations a CPU can perform
2. **Memory efficiency**: Pack multiple boolean flags into a single integer
3. **Algorithm elegance**: Many problems have beautiful bit-based solutions
4. **Systems programming**: Low-level code often requires bit manipulation
5. **Interview questions**: They're a favorite for testing problem-solving skills

## The Binary Mindset

Before diving into tricks, you need to think in binary. Every integer is a collection of bits:

```
13 in binary: 1101
Positions:    3210  (right to left, starting from 0)

Bit 0: 1 (value = 1)
Bit 1: 0 (value = 0) 
Bit 2: 1 (value = 4)
Bit 3: 1 (value = 8)
Total: 1 + 0 + 4 + 8 = 13
```

**The insight**: Each bit position represents a power of 2. Understanding this is fundamental to everything that follows.

## The Essential Operations

### Basic Bit Operations

```python
# AND (&) - both bits must be 1
5 & 3    # 101 & 011 = 001 = 1

# OR (|) - at least one bit must be 1  
5 | 3    # 101 | 011 = 111 = 7

# XOR (^) - exactly one bit must be 1
5 ^ 3    # 101 ^ 011 = 110 = 6

# NOT (~) - flip all bits
~5       # ~101 = ...11111010 (two's complement)

# Left shift (<<) - multiply by 2^n
5 << 1   # 101 << 1 = 1010 = 10

# Right shift (>>) - divide by 2^n
5 >> 1   # 101 >> 1 = 10 = 2
```

### Individual Bit Manipulation

```python
def get_bit(num, i):
    """Get the ith bit (0 or 1)."""
    return (num >> i) & 1

def set_bit(num, i):
    """Set the ith bit to 1."""
    return num | (1 << i)

def clear_bit(num, i):
    """Set the ith bit to 0."""
    return num & ~(1 << i)

def toggle_bit(num, i):
    """Flip the ith bit."""
    return num ^ (1 << i)
```

**The pattern**: Use `1 << i` to create a mask with only the ith bit set, then combine with the appropriate operation.

## The Power Tricks

### Checking if a Number is a Power of 2

```python
def is_power_of_two(n):
    """Check if n is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0

# Why this works:
# Power of 2: 8 = 1000
# n - 1:      7 = 0111
# n & (n-1):    = 0000 = 0
```

**The insight**: Powers of 2 have exactly one bit set. Subtracting 1 flips all the trailing bits, so the AND operation yields 0.

### Counting Set Bits (Population Count)

```python
def count_set_bits(n):
    """Count the number of 1s in binary representation."""
    count = 0
    while n:
        count += 1
        n &= n - 1  # Remove the rightmost set bit
    return count

# Brian Kernighan's algorithm
# Each iteration removes exactly one set bit
```

**The magic**: `n & (n-1)` always removes the rightmost set bit. The number of iterations equals the number of set bits.

### Finding the Rightmost Set Bit

```python
def rightmost_set_bit(n):
    """Get the rightmost set bit."""
    return n & (-n)

# Example: n = 12 = 1100
# -n (two's complement) = ...11110100
# n & (-n) = 0100 = 4
```

**The mathematics**: In two's complement, `-n` flips all bits and adds 1. This isolates the rightmost set bit.

## XOR: The Swiss Army Knife

XOR has unique properties that make it incredibly useful:

1. **a ^ a = 0** (anything XORed with itself is 0)
2. **a ^ 0 = a** (anything XORed with 0 is unchanged)
3. **XOR is commutative and associative**

### Finding the Single Non-Duplicate

```python
def single_number(nums):
    """Find the number that appears once when all others appear twice."""
    result = 0
    for num in nums:
        result ^= num
    return result

# [2, 3, 2, 4, 4] -> 0^2^3^2^4^4 -> 3
```

**The elegance**: Duplicate numbers cancel out, leaving only the unique one.

### Swapping Without a Temporary Variable

```python
def swap_xor(a, b):
    """Swap two numbers using only XOR."""
    a ^= b
    b ^= a
    a ^= b
    return a, b

# More readable version
def swap_xor_explained(a, b):
    a = a ^ b    # a now contains a^b
    b = a ^ b    # b = (a^b)^b = a^(b^b) = a^0 = a
    a = a ^ b    # a = (a^b)^a = (a^a)^b = 0^b = b
    return a, b
```

### Finding Two Non-Duplicates

When exactly two numbers appear once and all others appear twice:

```python
def single_numbers(nums):
    """Find two numbers that appear once when others appear twice."""
    # XOR all numbers - result is a^b where a,b are the unique numbers
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Find a bit where a and b differ
    diff_bit = xor_all & (-xor_all)  # Rightmost set bit
    
    # Partition numbers based on this bit
    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num
    
    return [a, b]
```

**The insight**: The XOR of two different numbers has at least one bit set. Use that bit to partition the array into two groups.

## Bit Masks and Flags

### Using Integers as Boolean Arrays

```python
class BitSet:
    def __init__(self):
        self.bits = 0
    
    def add(self, x):
        """Add x to the set."""
        self.bits |= (1 << x)
    
    def remove(self, x):
        """Remove x from the set."""
        self.bits &= ~(1 << x)
    
    def contains(self, x):
        """Check if x is in the set."""
        return bool(self.bits & (1 << x))
    
    def size(self):
        """Count elements in the set."""
        return bin(self.bits).count('1')

# Usage
s = BitSet()
s.add(3)
s.add(7)
print(s.contains(3))  # True
print(s.contains(5))  # False
```

### Subset Generation

```python
def generate_subsets(nums):
    """Generate all subsets using bit manipulation."""
    n = len(nums)
    subsets = []
    
    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if ith bit is set
                subset.append(nums[i])
        subsets.append(subset)
    
    return subsets
```

**The pattern**: Each bit position corresponds to whether an element is included in the subset.

## Advanced Bit Manipulation

### Gray Code Generation

Gray code is a sequence where consecutive numbers differ by exactly one bit:

```python
def gray_code(n):
    """Generate n-bit Gray code sequence."""
    if n == 0:
        return [0]
    
    # Recursive approach
    prev_gray = gray_code(n - 1)
    result = []
    
    # First half: add 0 bit prefix
    for code in prev_gray:
        result.append(code)
    
    # Second half: add 1 bit prefix, reverse order
    for code in reversed(prev_gray):
        result.append(code | (1 << (n - 1)))
    
    return result

# Iterative approach
def gray_code_iterative(n):
    result = [0]
    for i in range(n):
        result += [x | (1 << i) for x in reversed(result)]
    return result
```

### Reverse Bits

```python
def reverse_bits(n):
    """Reverse the bits of a 32-bit unsigned integer."""
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Optimized version using bit manipulation tricks
def reverse_bits_optimized(n):
    # Swap pairs
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    # Swap nibbles
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # Swap bytes
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # Swap 2-byte long pairs
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # Swap 4-byte long pairs
    n = (n >> 16) | (n << 16)
    return n & 0xFFFFFFFF
```

## Arithmetic Without Arithmetic

### Addition Using Bit Operations

```python
def add_without_plus(a, b):
    """Add two numbers without using + operator."""
    while b != 0:
        carry = a & b        # Calculate carry
        a = a ^ b           # Sum without carry
        b = carry << 1      # Shift carry left
    return a

# Example: 5 + 3
# a=101, b=011
# carry = 101 & 011 = 001
# a = 101 ^ 011 = 110
# b = 001 << 1 = 010
# 
# a=110, b=010  
# carry = 110 & 010 = 010
# a = 110 ^ 010 = 100
# b = 010 << 1 = 100
#
# a=100, b=100
# carry = 100 & 100 = 100  
# a = 100 ^ 100 = 000
# b = 100 << 1 = 1000
#
# a=000, b=1000
# carry = 000 & 1000 = 000
# a = 000 ^ 1000 = 1000
# b = 000 << 1 = 000
#
# b=0, so result is 1000 = 8
```

### Division Using Bit Operations

```python
def divide_without_division(dividend, divisor):
    """Divide without using / or * operators."""
    if dividend == 0:
        return 0
    
    # Handle signs
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        
        # Find the largest multiple of divisor that fits
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        dividend -= temp
        quotient += multiple
    
    return sign * quotient
```

## Practical Applications

### Fast Exponentiation

```python
def fast_power(base, exp):
    """Compute base^exp efficiently using bit manipulation."""
    result = 1
    while exp > 0:
        if exp & 1:  # If current bit is set
            result *= base
        base *= base
        exp >>= 1
    return result

# Binary representation of exponent guides the computation
# 3^13 where 13 = 1101 binary
# Result = 3^8 * 3^4 * 3^1
```

### Hamming Distance

```python
def hamming_distance(x, y):
    """Count differing bits between two integers."""
    return bin(x ^ y).count('1')

# Or using bit manipulation
def hamming_distance_optimized(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += 1
        xor &= xor - 1  # Remove rightmost set bit
    return count
```

## Performance Considerations

### When Bit Manipulation Helps

1. **Space optimization**: Storing boolean flags
2. **Fast arithmetic**: Powers of 2 operations
3. **Set operations**: Union, intersection on small sets
4. **Cryptography**: Bitwise operations in encryption
5. **Graphics**: Pixel manipulation, color operations

### When to Avoid It

1. **Readability concerns**: Bit tricks can be cryptic
2. **Maintenance issues**: Hard to debug and modify
3. **Premature optimization**: Profile first
4. **Platform dependencies**: Bit operations can be platform-specific

## Common Interview Problems

### Missing Number

```python
def missing_number(nums):
    """Find missing number in range [0, n]."""
    n = len(nums)
    result = n  # Start with n
    for i, num in enumerate(nums):
        result ^= i ^ num  # XOR index with value
    return result
```

### Power of Four

```python
def is_power_of_four(n):
    """Check if n is a power of 4."""
    # Must be power of 2 and have bit in odd position
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

### Maximum XOR

```python
def maximum_xor(nums):
    """Find maximum XOR of any two numbers."""
    max_xor = 0
    mask = 0
    
    for i in range(31, -1, -1):  # Check each bit position
        mask |= (1 << i)  # Add current bit to mask
        prefixes = {num & mask for num in nums}
        
        temp = max_xor | (1 << i)  # Try to make current bit 1
        for prefix in prefixes:
            if temp ^ prefix in prefixes:
                max_xor = temp
                break
    
    return max_xor
```

## Final Thoughts

Bit manipulation is where computer science meets pure mathematics. The elegance of these techniques lies in their simplicity—complex problems often have surprisingly simple bit-based solutions.

The key to mastering bit manipulation is practice and pattern recognition. Start with the fundamentals (setting, clearing, testing bits) and gradually work up to more complex operations. 

Remember that bit manipulation is a tool, not a goal. Use it when it provides clear benefits in terms of performance, memory usage, or algorithmic elegance. But always consider the trade-offs in code readability and maintainability.

Most importantly, think in binary. Once you can visualize numbers as patterns of bits, these operations become intuitive rather than mysterious.

---

*Next up: FastAPI - where modern Python web development meets type safety and automatic documentation.*