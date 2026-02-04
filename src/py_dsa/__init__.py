def main() -> None:
    """Main entry point for py-dsa learning platform."""
    print("Welcome to py-dsa!")
    print("A comprehensive Data Structures and Algorithms learning platform.")
    print("")
    print("📚 Core DSA Topics:")
    print("  • fundamentals_exercises.py - Basic data structures and algorithms")
    print("  • linked_list_exercises.py - Linked list operations and patterns")
    print("  • binary_search_exercises.py - Binary search and variations")
    print("  • sliding_window_exercises.py - Sliding window technique")
    print("  • two_pointers_exercises.py - Two pointers technique")
    print("  • stack_queue_exercises.py - Stack and queue operations")
    print("  • heap_exercises.py - Heap and priority queue")
    print("  • bfs_exercises.py - Breadth-first search")
    print("  • graph_exercises.py - Graph algorithms")
    print("  • trie_exercises.py - Trie (prefix tree) operations")
    print("  • dp_exercises.py - Dynamic programming")
    print("  • greedy_exercises.py - Greedy algorithms")
    print("  • backtracking_exercises.py - Backtracking algorithms")
    print("  • union_find_exercises.py - Union Find (Disjoint Set)")
    print("  • bit_manipulation_exercises.py - Bit operations and tricks")
    print("")
    print("🎯 Interview Preparation:")
    print("  • blind150_exercises.py - Blind 150 LeetCode problems")
    print("")
    print("🔬 Data Science & ML:")
    print("  • numpy_exercises.py - NumPy numerical computing")
    print("  • pandas_exercises.py - Pandas data manipulation")
    print("  • pytorch_exercises.py - PyTorch deep learning")
    print("")
    print("🌐 Web Development:")
    print("  • fastapi_exercises.py - FastAPI framework for APIs")
    print("  • pydantic_exercises.py - Data validation with Pydantic")
    print("")
    print("🔤 Advanced Algorithms:")
    print("  • string_algorithms_exercises.py - String processing and pattern matching")
    print("  • sorting_exercises.py - Sorting algorithms and analysis")
    print("")
    print("🚀 Getting Started:")
    print("  1. Start with fundamentals_exercises.py")
    print("  2. Practice core patterns (sliding window, two pointers)")
    print("  3. Master data structures (linked lists, trees, graphs)")
    print("  4. Tackle advanced algorithms (DP, greedy, backtracking)")
    print("  5. Prepare for interviews with blind150_exercises.py")
    print("")
    print("⚡ Quick Commands:")
    print("  • just test - Run all tests")
    print("  • just test-fundamentals - Test fundamentals only")
    print("  • just test-blind150 - Test Blind 150 problems")
    print("  • just --list - See all available commands")
    print("")
    
    # Import modules to ensure they're covered by tests
    from . import fundamentals_exercises
    from . import linked_list_exercises
    from . import greedy_exercises  
    from . import union_find_exercises
    from . import bit_manipulation_exercises
    from . import blind150_exercises
    from . import string_algorithms_exercises
    from . import sorting_exercises
    from . import numpy_exercises
    from . import pandas_exercises
    from . import pytorch_exercises
    from . import pydantic_exercises
    from . import fastapi_exercises
    from . import sliding_window_exercises  
    from . import two_pointers_exercises
    from . import bfs_exercises
    from . import dp_exercises
    from . import backtracking_exercises
    from . import binary_search_exercises
    from . import graph_exercises
    from . import stack_queue_exercises
    from . import trie_exercises
    from . import heap_exercises
