# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for practicing Data Structures and Algorithms (DSA) concepts. The project uses modern Python packaging with `pyproject.toml` and requires Python 3.13+. It's structured as a learning platform with progressive exercises grouped by difficulty and topic.

## Architecture

- **Package Structure**: Standard Python package layout with source code in `src/py_dsa/`
- **Entry Point**: Main entry point is `py_dsa:main` function in `src/py_dsa/__init__.py`
- **Build System**: Uses `uv_build` as the build backend
- **Core DSA Modules**:
  - `fundamentals_exercises.py` - Basic data structures (queues, trees, recursion)
  - `linked_list_exercises.py` - Linked list operations and patterns
  - `binary_search_exercises.py` - Binary search and variations
  - `sliding_window_exercises.py` - Sliding Window technique problems
  - `two_pointers_exercises.py` - Two Pointers technique problems
  - `stack_queue_exercises.py` - Stack and queue operations
  - `heap_exercises.py` - Heap and priority queue problems
  - `bfs_exercises.py` - Breadth-First Search problems
  - `graph_exercises.py` - Graph algorithms and traversal
  - `trie_exercises.py` - Trie (prefix tree) operations
  - `dp_exercises.py` - Dynamic Programming problems
  - `greedy_exercises.py` - Greedy algorithm problems
  - `backtracking_exercises.py` - Backtracking algorithm problems
  - `union_find_exercises.py` - Union Find (Disjoint Set) problems
  - `bit_manipulation_exercises.py` - Bit operations and tricks
- **Interview Preparation**:
  - `blind150_exercises.py` - Blind 150 LeetCode problems for interview prep
- **Data Science & Computing**:
  - `numpy_exercises.py` - NumPy numerical computing exercises
  - `pandas_exercises.py` - Pandas data manipulation exercises
- **Testing**: Comprehensive test suite with pytest markers for organization

## Learning Path

### 🚀 Beginner Path (Start Here)
1. **Fundamentals**: `fundamentals_exercises.py` - Master basic concepts first
2. **Linear Structures**: `linked_list_exercises.py` - Understand pointer manipulation
3. **Search Basics**: `binary_search_exercises.py` - Learn divide and conquer

### 🎯 Core Patterns (Essential for Interviews)
4. **Array Techniques**:
   - `sliding_window_exercises.py` - Efficient array/string processing
   - `two_pointers_exercises.py` - Linear traversal techniques
5. **Stack/Queue**: `stack_queue_exercises.py` - LIFO/FIFO principles
6. **Tree/Graph Traversal**:
   - `bfs_exercises.py` - Breadth-first search
   - `graph_exercises.py` - Graph algorithms and pathfinding
7. **Advanced Data Structures**:
   - `heap_exercises.py` - Priority queues and heap operations
   - `trie_exercises.py` - Prefix trees for string problems

### 🧠 Advanced Algorithms
8. **Optimization Strategies**:
   - `dp_exercises.py` - Dynamic programming (after mastering recursion)
   - `greedy_exercises.py` - Locally optimal choices
   - `backtracking_exercises.py` - Systematic solution space exploration
9. **Specialized Techniques**:
   - `union_find_exercises.py` - Disjoint set operations
   - `bit_manipulation_exercises.py` - Low-level optimizations

### 🎯 Interview Preparation
10. **Comprehensive Practice**: `blind150_exercises.py` - Most common interview problems

### 🔬 Data Science Track (Optional)
11. **Numerical Computing**: `numpy_exercises.py` - Scientific computing foundations
12. **Data Manipulation**: `pandas_exercises.py` - Data analysis and preprocessing

## Development Commands

This project uses [just](https://github.com/casey/just) for convenient command running. Install it with:
```bash
# On macOS with Homebrew
brew install just

# On Ubuntu/Debian
snap install --edge just

# Or via cargo
cargo install just
```

### Quick Start
```bash
# Install dependencies and run tests
just dev

# Run all tests
just test

# Run tests with coverage
just test-cov

# Watch files and auto-run tests
just watch
```

### Test Categories
```bash
# Core DSA exercises
just test-fundamentals
just test-linked-list
just test-binary-search
just test-sliding-window
just test-two-pointers
just test-stack-queue
just test-heap
just test-bfs
just test-graph
just test-trie
just test-dp
just test-greedy
just test-backtracking
just test-union-find
just test-bit-manipulation

# Interview preparation
just test-blind150

# Data science
just test-numpy
just test-pandas

# Run by difficulty
just test-easy
just test-medium
just test-hard
```

### Advanced Testing
```bash
# Run specific difficulty for a technique
just test-sliding-window-basic
just test-dp-advanced

# Watch specific categories
just watch-fundamentals
just watch-sliding-window

# Run specific test pattern
just test-match "substring"
just watch-match "palindrome"
```

### Legacy pytest commands (still work)
```bash
# Direct pytest usage
pytest -m fundamentals
pytest -m "sliding_window and easy"
pytest --cov=src --cov-report=html
```

## Testing and Coverage

The project uses pytest with coverage measurement:
- Coverage threshold is set to 80%
- HTML coverage reports are generated in `htmlcov/`
- All exercises should be thoroughly tested
- Coverage helps ensure comprehensive test coverage for learning modules
- Configuration is centralized in `pyproject.toml` under `[tool.pytest.ini_options]`

## Exercise Structure

Each exercise module follows this pattern:
- **TODO comments**: Mark where students should implement solutions
- **Progressive difficulty**: Easy → Medium → Hard
- **Comprehensive tests**: Multiple test cases per function
- **Clear examples**: Input/output examples in docstrings

## Code Organization

- **Source code**: `src/py_dsa/` contains exercise modules
- **Tests**: `tests/` mirrors source structure with comprehensive test coverage
- **Markers**: Use pytest markers to organize and run specific exercise groups
- **Documentation**: Each function includes clear problem descriptions and examples
- You must not add solutions in the exercise file in the form of comments.
- You must add docs/ markdown files for every topic that you start in the src/py_dsa folder.
- Document harder problems in docs/solutions/ with detailed solutions
- You must be thorough in a topic before moving on to another topic
- You must not add leetcode style problems directly, build up to them so that I can build confidence in my skills.
- You must keep coverage at 80% or higher
- You must add thorough tests to validate the code the user has written.