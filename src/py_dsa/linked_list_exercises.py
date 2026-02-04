from typing import Optional, List


class ListNode:
    """Standard singly linked list node definition."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class DoublyListNode:
    """Doubly linked list node with prev pointer."""
    def __init__(self, val: int = 0, next: Optional['DoublyListNode'] = None, prev: Optional['DoublyListNode'] = None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedListExercises:
    """
    Linked List exercises with progressive difficulty.
    
    Linked lists are fundamental linear data structures where elements are stored
    in nodes connected via pointers. Essential for understanding pointer manipulation
    and dynamic memory management concepts.
    
    Key patterns:
    - Two pointers (fast/slow, dummy nodes)
    - Reversal techniques
    - Cycle detection
    - Merge operations
    """
    
    # BASIC EXERCISES - Understanding linked list fundamentals
    
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Basic: Reverse a singly linked list iteratively.
        
        Example:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
        
        Approach: Use three pointers (prev, curr, next) to reverse links
        Time: O(n), Space: O(1)
        
        TODO: Implement iterative reversal using pointer manipulation
        """
        pass
    
    def reverse_linked_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Basic: Reverse a singly linked list recursively.
        
        Example:
        Input: head = [1,2,3,4,5]  
        Output: [5,4,3,2,1]
        
        Approach: Recursive divide and conquer
        Time: O(n), Space: O(n) for recursion stack
        
        TODO: Implement recursive reversal
        """
        pass
    
    def find_middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Basic: Find middle node using two-pointer technique.
        
        Example:
        Input: head = [1,2,3,4,5]
        Output: node with value 3
        
        Approach: Fast pointer moves 2 steps, slow moves 1 step
        Time: O(n), Space: O(1)
        
        TODO: Use fast/slow pointers to find middle
        """
        pass
    
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Basic: Detect cycle in linked list using Floyd's algorithm.
        
        Example:
        Input: head = [3,2,0,-4] with cycle from position 1
        Output: True
        
        Approach: Fast/slow pointers (Floyd's Cycle Detection)
        Time: O(n), Space: O(1)
        
        TODO: Implement cycle detection with two pointers
        """
        pass
    
    def find_cycle_start(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Medium: Find the node where cycle begins.
        
        Example:
        Input: head = [3,2,0,-4] with cycle from position 1
        Output: node with value 2
        
        Approach: Floyd's algorithm + mathematical insight
        Time: O(n), Space: O(1)
        
        TODO: First detect cycle, then find start position
        """
        pass
    
    # MANIPULATION EXERCISES - Modifying linked list structure
    
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Medium: Remove nth node from end of list.
        
        Example:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
        
        Approach: Two pointers with n gap
        Time: O(L), Space: O(1) where L is list length
        
        TODO: Use dummy node and two pointers
        """
        pass
    
    def remove_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Easy: Remove duplicates from sorted linked list.
        
        Example:
        Input: head = [1,1,2,3,3]
        Output: [1,2,3]
        
        Approach: Single pass with pointer manipulation
        Time: O(n), Space: O(1)
        
        TODO: Skip nodes with duplicate values
        """
        pass
    
    def remove_all_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Medium: Remove all nodes that have duplicates.
        
        Example:
        Input: head = [1,2,3,3,4,4,5]
        Output: [1,2,5]
        
        Approach: Dummy node + careful pointer tracking
        Time: O(n), Space: O(1)
        
        TODO: Remove entire duplicate sequences
        """
        pass
    
    def partition_list(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Medium: Partition list around value x.
        
        Example:
        Input: head = [1,4,3,2,5,2], x = 3
        Output: [1,2,2,4,3,5]
        
        Approach: Two separate lists then connect
        Time: O(n), Space: O(1)
        
        TODO: Create before and after lists
        """
        pass
    
    # MERGING EXERCISES - Combining linked lists
    
    def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Easy: Merge two sorted linked lists.
        
        Example:
        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        
        Approach: Two pointers with dummy head
        Time: O(n+m), Space: O(1)
        
        TODO: Compare values and build merged list
        """
        pass
    
    def merge_k_sorted_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Hard: Merge k sorted linked lists.
        
        Example:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        
        Approach: Divide and conquer
        Time: O(N log k), Space: O(log k)
        
        TODO: Use divide and conquer with merge_two_sorted_lists
        """
        pass
    
    # ADVANCED EXERCISES - Complex operations
    
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Medium: Add two numbers represented as linked lists.
        
        Example:
        Input: l1 = [2,4,3], l2 = [5,6,4] (represents 342 + 465)
        Output: [7,0,8] (represents 807)
        
        Approach: Simulate addition with carry
        Time: O(max(n,m)), Space: O(max(n,m))
        
        TODO: Handle carry and different length lists
        """
        pass
    
    def reverse_nodes_in_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Hard: Reverse nodes in groups of k.
        
        Example:
        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]
        
        Approach: Group reversal with careful reconnection
        Time: O(n), Space: O(1)
        
        TODO: Reverse each complete group of k nodes
        """
        pass
    
    def copy_random_list(self, head: Optional['RandomListNode']) -> Optional['RandomListNode']:
        """
        Medium: Deep copy linked list with random pointers.
        
        Approach: Three-pass algorithm or hashmap
        Time: O(n), Space: O(1) or O(n)
        
        TODO: Copy nodes with both next and random pointers
        """
        pass
    
    # UTILITY METHODS
    
    def list_to_array(self, head: Optional[ListNode]) -> List[int]:
        """Convert linked list to array for testing."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def array_to_list(self, arr: List[int]) -> Optional[ListNode]:
        """Convert array to linked list for testing."""
        if not arr:
            return None
        
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def create_cycle(self, head: Optional[ListNode], pos: int) -> Optional[ListNode]:
        """Create cycle in linked list at given position for testing."""
        if not head or pos < 0:
            return head
        
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        if pos < len(nodes):
            nodes[-1].next = nodes[pos]
        
        return head


# Helper class for random pointer exercises
class RandomListNode:
    """Node with random pointer for copy exercises."""
    def __init__(self, val: int = 0, next: Optional['RandomListNode'] = None, random: Optional['RandomListNode'] = None):
        self.val = val
        self.next = next
        self.random = random