from collections import deque
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class StackQueueExercises:
    """
    Stack and Queue data structure exercises with progressive difficulty.
    
    Stack: LIFO (Last In, First Out) - like a stack of plates
    Queue: FIFO (First In, First Out) - like a line of people
    
    Essential for understanding recursion, DFS, BFS, and many algorithms.
    """
    
    # BASIC EXERCISES - Understanding stack and queue operations
    
    def implement_stack_with_list(self) -> 'MyStack':
        """
        Basic: Implement stack using Python list.
        
        Operations: push(x), pop(), top(), empty()
        
        TODO: Create MyStack class with list-based implementation
        """
        return MyStack()
    
    def implement_queue_with_list(self) -> 'MyQueue':
        """
        Basic: Implement queue using Python list (inefficient but educational).
        
        Operations: push(x), pop(), peek(), empty()
        
        TODO: Create MyQueue class (note: pop from front is O(n))
        """
        return MyQueue()
    
    def implement_queue_with_deque(self) -> 'MyDeque':
        """
        Basic: Implement queue using collections.deque (efficient).
        
        Operations: push(x), pop(), peek(), empty()
        
        TODO: Create MyDeque class using deque for O(1) operations
        """
        return MyDeque()
    
    def valid_parentheses(self, s: str) -> bool:
        """
        Basic: Check if parentheses are valid using stack.
        
        Example:
        Input: s = "()[]{}"
        Output: True
        
        TODO: Use stack to match opening/closing brackets
        """
        return False
    
    def implement_stack_using_queues(self) -> 'StackUsingQueues':
        """
        Basic: Implement stack using only queue operations.
        
        Operations: push(x), pop(), top(), empty()
        
        TODO: Use one or two queues to simulate stack behavior
        """
        return StackUsingQueues()
    
    def implement_queue_using_stacks(self) -> 'QueueUsingStacks':
        """
        Basic: Implement queue using only stack operations.
        
        Operations: push(x), pop(), peek(), empty()
        
        TODO: Use two stacks to simulate queue behavior
        """
        return QueueUsingStacks()
    
    # INTERMEDIATE EXERCISES - Stack and queue applications
    
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Intermediate: Find next greater element for each element in nums1.
        
        Example:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1] (next greater for 4: -1, for 1: 3, for 2: -1)
        
        TODO: Use monotonic stack to precompute next greater elements
        """
        return []
    
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        Intermediate: Find how many days until warmer temperature.
        
        Example:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        
        TODO: Use monotonic stack to track indices
        """
        return []
    
    def evaluate_reverse_polish_notation(self, tokens: List[str]) -> int:
        """
        Intermediate: Evaluate arithmetic expression in postfix notation.
        
        Example:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9 (((2 + 1) * 3) = 9)
        
        TODO: Use stack to process operators and operands
        """
        return 0
    
    def largest_rectangle_in_histogram(self, heights: List[int]) -> int:
        """
        Intermediate: Find area of largest rectangle in histogram.
        
        Example:
        Input: heights = [2,1,5,6,2,3]
        Output: 10 (rectangle with height 5 and width 2)
        
        TODO: Use monotonic stack to find boundaries
        """
        return 0
    
    def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
        """
        Intermediate: Find maximum in every sliding window using deque.
        
        Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        
        TODO: Use monotonic deque to maintain window maximum
        """
        return []
    
    # ADVANCED EXERCISES - Complex stack/queue problems
    
    def basic_calculator(self, s: str) -> int:
        """
        Advanced: Implement calculator for expressions with +, -, (, ).
        
        Example:
        Input: s = "1 + 1"
        Output: 2
        
        TODO: Use stack to handle parentheses and operators
        """
        return 0
    
    def basic_calculator_ii(self, s: str) -> int:
        """
        Advanced: Calculator with +, -, *, / operators (no parentheses).
        
        Example:
        Input: s = "3+2*2"
        Output: 7
        
        TODO: Use stack to handle operator precedence
        """
        return 0
    
    def remove_duplicate_letters(self, s: str) -> str:
        """
        Advanced: Remove duplicate letters maintaining lexicographic order.
        
        Example:
        Input: s = "bcabc"
        Output: "abc"
        
        TODO: Use monotonic stack with frequency counting
        """
        return ""
    
    def shortest_subarray_with_sum_k(self, nums: List[int], k: int) -> int:
        """
        Advanced: Find shortest subarray with sum at least k.
        
        Example:
        Input: nums = [1], k = 1
        Output: 1
        
        TODO: Use monotonic deque with prefix sums
        """
        return -1
    
    def trapping_rain_water(self, height: List[int]) -> int:
        """
        Advanced: Calculate trapped rainwater using stack approach.
        
        Example:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        
        TODO: Use stack to find water levels between bars
        """
        return 0
    
    def decode_string(self, s: str) -> str:
        """
        Advanced: Decode string with nested brackets and repetition.
        
        Example:
        Input: s = "3[a2[c]]"
        Output: "accaccacc"
        
        TODO: Use stack to handle nested brackets
        """
        return ""
    
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        """
        Advanced: Simulate asteroid collisions using stack.
        
        Example:
        Input: asteroids = [5,10,-5]
        Output: [5,10] (-5 explodes when hitting 10)
        
        TODO: Use stack to simulate right-moving asteroids
        """
        return []
    
    def online_stock_span(self) -> 'StockSpanner':
        """
        Advanced: Calculate stock price spans using monotonic stack.
        
        Example:
        StockSpanner stockSpanner = new StockSpanner();
        stockSpanner.next(100); // return 1
        stockSpanner.next(80);  // return 1
        
        TODO: Use monotonic stack to track previous higher prices
        """
        return StockSpanner()


# Helper classes that students should implement

class MyStack:
    """Stack implementation using list."""
    
    def __init__(self):
        # TODO: Initialize stack
        pass
    
    def push(self, x: int) -> None:
        # TODO: Push element to top
        pass
    
    def pop(self) -> int:
        # TODO: Remove and return top element
        return 0
    
    def top(self) -> int:
        # TODO: Return top element without removing
        return 0
    
    def empty(self) -> bool:
        # TODO: Check if stack is empty
        return True


class MyQueue:
    """Queue implementation using list (inefficient)."""
    
    def __init__(self):
        # TODO: Initialize queue
        pass
    
    def push(self, x: int) -> None:
        # TODO: Add element to rear
        pass
    
    def pop(self) -> int:
        # TODO: Remove and return front element
        return 0
    
    def peek(self) -> int:
        # TODO: Return front element without removing
        return 0
    
    def empty(self) -> bool:
        # TODO: Check if queue is empty
        return True


class MyDeque:
    """Queue implementation using deque (efficient)."""
    
    def __init__(self):
        # TODO: Initialize deque
        pass
    
    def push(self, x: int) -> None:
        # TODO: Add element to rear
        pass
    
    def pop(self) -> int:
        # TODO: Remove and return front element
        return 0
    
    def peek(self) -> int:
        # TODO: Return front element without removing
        return 0
    
    def empty(self) -> bool:
        # TODO: Check if queue is empty
        return True


class StackUsingQueues:
    """Stack implementation using queues."""
    
    def __init__(self):
        # TODO: Initialize with queue(s)
        pass
    
    def push(self, x: int) -> None:
        # TODO: Push element
        pass
    
    def pop(self) -> int:
        # TODO: Pop element
        return 0
    
    def top(self) -> int:
        # TODO: Get top element
        return 0
    
    def empty(self) -> bool:
        # TODO: Check if empty
        return True


class QueueUsingStacks:
    """Queue implementation using stacks."""
    
    def __init__(self):
        # TODO: Initialize with stack(s)
        pass
    
    def push(self, x: int) -> None:
        # TODO: Push element
        pass
    
    def pop(self) -> int:
        # TODO: Pop element
        return 0
    
    def peek(self) -> int:
        # TODO: Peek front element
        return 0
    
    def empty(self) -> bool:
        # TODO: Check if empty
        return True


class StockSpanner:
    """Online stock span calculator."""
    
    def __init__(self):
        # TODO: Initialize data structures
        pass
    
    def next(self, price: int) -> int:
        # TODO: Calculate span for current price
        return 1