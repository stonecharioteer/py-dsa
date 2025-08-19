# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for practicing Data Structures and Algorithms (DSA) concepts. The project uses modern Python packaging with `pyproject.toml` and requires Python 3.13+. It's structured as a learning platform with progressive exercises grouped by difficulty and topic.

## Architecture

- **Package Structure**: Standard Python package layout with source code in `src/py_dsa/`
- **Entry Point**: Main entry point is `py_dsa:main` function in `src/py_dsa/__init__.py`
- **Build System**: Uses `uv_build` as the build backend
- **Exercise Modules**: 
  - `fundamentals_exercises.py` - Basic data structures (queues, trees, recursion)
  - `bfs_exercises.py` - Breadth-First Search problems
  - `dp_exercises.py` - Dynamic Programming problems
  - `sliding_window_exercises.py` - Sliding Window technique problems
  - `two_pointers_exercises.py` - Two Pointers technique problems
  - `backtracking_exercises.py` - Backtracking algorithm problems
- **Testing**: Comprehensive test suite with pytest markers for organization

## Learning Path

1. **Start with Fundamentals**: Complete `fundamentals_exercises.py` first
2. **Core Techniques**: Learn the main algorithmic patterns:
   - `sliding_window_exercises.py` - Efficient array/string processing
   - `two_pointers_exercises.py` - Linear traversal techniques
   - `bfs_exercises.py` - Tree and graph traversal
3. **Advanced Techniques**:
   - `dp_exercises.py` - After understanding recursion and memoization
   - `backtracking_exercises.py` - Systematic solution space exploration

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
# Run specific exercise types
just test-fundamentals
just test-sliding-window
just test-two-pointers
just test-bfs
just test-dp
just test-backtracking

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