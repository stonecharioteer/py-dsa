def main() -> None:
    """Main entry point for py-dsa learning platform."""
    print("Welcome to py-dsa!")
    print("A comprehensive Data Structures and Algorithms learning platform.")
    print("")
    print("Available exercise modules:")
    print("- fundamentals_exercises.py - Basic data structures")
    print("- sliding_window_exercises.py - Sliding window technique")
    print("- two_pointers_exercises.py - Two pointers technique") 
    print("- bfs_exercises.py - Breadth-first search")
    print("- dp_exercises.py - Dynamic programming")
    print("- backtracking_exercises.py - Backtracking algorithms")
    print("")
    print("Run 'just test' to run all tests or 'just --list' to see available commands.")
    
    # Import modules to ensure they're covered by tests
    from . import fundamentals_exercises
    from . import sliding_window_exercises  
    from . import two_pointers_exercises
    from . import bfs_exercises
    from . import dp_exercises
    from . import backtracking_exercises
