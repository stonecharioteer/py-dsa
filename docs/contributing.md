# Contributing to py-dsa

This guide explains how to add new exercises, tests, and maintain the learning platform structure. The py-dsa platform is designed as a comprehensive DSA learning system with progressive difficulty and comprehensive test coverage.

## Project Structure Overview

```
py-dsa/
├── src/py_dsa/               # Exercise modules
│   ├── __init__.py          # Main entry point  
│   ├── fundamentals_exercises.py
│   ├── sliding_window_exercises.py
│   ├── two_pointers_exercises.py
│   ├── bfs_exercises.py
│   ├── dp_exercises.py
│   └── backtracking_exercises.py
├── tests/                   # Comprehensive test suite
│   ├── test_fundamentals_exercises.py
│   ├── test_sliding_window_exercises.py
│   └── ...
├── docs/                    # Tutorial documentation
│   ├── sliding-window.md
│   ├── two-pointers.md
│   └── contributing.md
├── justfile                 # Task runner commands
├── pyproject.toml          # Project config + pytest markers
└── CLAUDE.md               # Development guidance
```

## Adding New Exercise Modules

### 1. Create the Exercise Module

Create a new file in `src/py_dsa/` following the established pattern:

```python
# src/py_dsa/new_technique_exercises.py
from typing import List, Optional, Dict


class NewTechniqueExercises:
    """
    New Technique exercises with progressive difficulty.
    
    Brief explanation of the technique and when to use it.
    """
    
    # BASIC EXERCISES - Understanding fundamentals
    
    def basic_function_name(self, param: type) -> return_type:
        """
        Basic: Clear description of what this function should do.
        
        Example:
        Input: example_input
        Output: expected_output
        
        TODO: Implementation guidance for students
        """
        pass
    
    # INTERMEDIATE EXERCISES - More complex applications
    
    def intermediate_function_name(self, param: type) -> return_type:
        """
        Intermediate: More complex problem description.
        
        Example:
        Input: example_input  
        Output: expected_output
        
        TODO: Implementation guidance
        """
        pass
    
    # ADVANCED EXERCISES - Complex real-world problems
    
    def advanced_function_name(self, param: type) -> return_type:
        """
        Advanced: Complex problem requiring deep understanding.
        
        Example:
        Input: example_input
        Output: expected_output
        
        TODO: Implementation guidance
        """
        pass
```

### 2. Design Principles for Exercises

- **Progressive Difficulty**: Start with fundamental concepts, build to complex applications
- **Clear Examples**: Every function should have input/output examples
- **Comprehensive Coverage**: Include edge cases and various input sizes
- **Real-World Relevance**: Problems should reflect actual interview/work scenarios
- **Learning Scaffolding**: Each exercise should build on previous concepts

### 3. Function Naming Convention

Use descriptive names that clearly indicate the problem:
- `longest_substring_without_repeating_chars` ✅
- `solve_problem` ❌
- `find_maximum_sum_subarray_of_size_k` ✅
- `max_sum` ❌

## Adding Comprehensive Tests

### 1. Create Test Module

Create corresponding test file in `tests/`:

```python
# tests/test_new_technique_exercises.py
import pytest
from src.py_dsa.new_technique_exercises import NewTechniqueExercises


class TestNewTechniqueExercises:
    """
    Tests for new technique exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.new_technique = NewTechniqueExercises()
    
    # BASIC LEVEL TESTS
    
    @pytest.mark.new_technique
    @pytest.mark.new_technique_basic  
    @pytest.mark.easy
    def test_basic_function_name_simple(self):
        """Test basic functionality with simple input."""
        result = self.new_technique.basic_function_name(simple_input)
        assert result == expected_result
    
    @pytest.mark.new_technique
    @pytest.mark.new_technique_basic
    @pytest.mark.easy  
    def test_basic_function_name_edge_cases(self):
        """Test basic functionality with edge cases."""
        # Empty input
        assert self.new_technique.basic_function_name(empty_input) == empty_result
        
        # Single element
        assert self.new_technique.basic_function_name(single_input) == single_result
        
        # Boundary conditions
        assert self.new_technique.basic_function_name(boundary_input) == boundary_result
```

### 2. Test Design Principles

- **Multiple Test Methods**: Separate simple cases from edge cases
- **Comprehensive Coverage**: Test empty inputs, single elements, large inputs, boundary conditions
- **Clear Test Names**: `test_function_name_scenario` pattern
- **Descriptive Docstrings**: Explain what specific scenario is being tested
- **Assert Messages**: When helpful, add custom assert messages for debugging

### 3. Required Test Categories per Function

For each exercise function, create tests for:

1. **Basic Functionality**: Standard inputs with expected outputs
2. **Edge Cases**: Empty inputs, single elements, null values
3. **Boundary Conditions**: Maximum/minimum values, size limits
4. **Error Conditions**: Invalid inputs (when applicable)
5. **Performance Cases**: Large inputs (for advanced functions)

## Using Pytest Markers Correctly

### 1. Marker Hierarchy

Every test should have **exactly 3 markers**:

```python
@pytest.mark.technique_name      # Primary technique (required)
@pytest.mark.technique_level     # Difficulty within technique (required)  
@pytest.mark.difficulty_level    # Overall difficulty (required)
def test_function_name():
    pass
```

### 2. Available Marker Categories

**Primary Technique Markers**:
- `@pytest.mark.fundamentals`
- `@pytest.mark.sliding_window`
- `@pytest.mark.two_pointers`
- `@pytest.mark.bfs`
- `@pytest.mark.dp`
- `@pytest.mark.backtracking`
- `@pytest.mark.new_technique` (when adding new)

**Technique-Specific Level Markers**:
- `@pytest.mark.technique_basic`
- `@pytest.mark.technique_intermediate` 
- `@pytest.mark.technique_advanced`

**General Difficulty Markers**:
- `@pytest.mark.easy`
- `@pytest.mark.medium`
- `@pytest.mark.hard`

### 3. Marker Guidelines

- **Consistent Application**: All functions in "BASIC EXERCISES" section get `technique_basic` + `easy`
- **Progressive Difficulty**: Basic → Intermediate → Advanced should align with Easy → Medium → Hard
- **Specific First**: Always use the most specific marker available
- **Test Discoverability**: Markers enable students to run focused practice sessions

## Adding New Markers to Configuration

### 1. Update pyproject.toml

When adding a new technique, add markers to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
markers = [
    # ... existing markers ...
    "new_technique: New Technique exercises",
    "new_technique_basic: Basic new technique exercises",
    "new_technique_intermediate: Intermediate new technique exercises", 
    "new_technique_advanced: Advanced new technique exercises",
]
```

### 2. Marker Naming Convention

- **Primary technique**: `technique_name` (e.g., `graph_algorithms`)
- **Technique levels**: `technique_name_level` (e.g., `graph_algorithms_basic`)
- **Use underscores**: Not hyphens or camelCase
- **Descriptive names**: Clear what the technique involves

## Updating Project Documentation

### 1. Update CLAUDE.md

When adding new modules, update the Exercise Modules section:

```markdown
- **Exercise Modules**: 
  - `fundamentals_exercises.py` - Basic data structures (queues, trees, recursion)
  - `new_technique_exercises.py` - New technique description
  # ... existing modules ...
```

And the Learning Path section:

```markdown
2. **Core Techniques**: Learn the main algorithmic patterns:
   - `new_technique_exercises.py` - Brief description
   # ... existing techniques ...
```

### 2. Update justfile

Add new commands for the technique:

```just
# Run specific exercise category tests  
test-new-technique:
    uv run pytest -m new_technique

# Watch specific test categories
watch-new-technique:
    uv run pytest -m new_technique

# Run specific technique difficulty levels
test-new-technique-basic:
    uv run pytest -m new_technique_basic

test-new-technique-intermediate:
    uv run pytest -m new_technique_intermediate

test-new-technique-advanced:
    uv run pytest -m new_technique_advanced
```

### 3. Update Main Entry Point

Add import to `src/py_dsa/__init__.py`:

```python
def main() -> None:
    # ... existing content ...
    print("- new_technique_exercises.py - New technique description")
    
    # Import modules to ensure they're covered by tests
    from . import new_technique_exercises  # Add this line
```

## Maintaining High Test Coverage

### 1. Coverage Requirements

- **Maintain 80%+ coverage**: All new code must maintain the coverage threshold
- **Test all code paths**: Ensure every function is called by at least one test
- **Meaningful Tests**: Tests should validate correct behavior, not just coverage

### 2. Coverage Verification

Before submitting changes:

```bash
# Check coverage
just test-cov

# Open detailed coverage report  
just test-cov-open

# Ensure new technique is covered
just test-new-technique
```

### 3. Coverage Troubleshooting

If coverage drops:

1. **Check missing functions**: Ensure every new function has tests
2. **Verify imports**: Make sure modules are imported in `__init__.py`
3. **Test execution**: Confirm all test methods are being discovered
4. **Marker coverage**: Verify all difficulty levels have tests

## Writing Tutorial Documentation

### 1. Create Tutorial Files

Add tutorial documentation in `docs/`:

```markdown
# docs/new-technique.md
# New Technique: Brief Catchy Title

Brief introduction explaining what this technique is and why it's useful.

## Core Concept

Explain the fundamental idea behind the technique...

## Common Patterns

### Pattern 1: Basic Usage
Explanation and example...

### Pattern 2: Advanced Usage  
More complex scenarios...

## When to Use This Technique

Signs that indicate this technique might be helpful...

## Common Gotchas

Typical mistakes and how to avoid them...

## Practice Strategy

Recommended learning progression...
```

### 2. Tutorial Writing Guidelines

- **Conversational Tone**: Instructional but approachable
- **Practical Examples**: Include code snippets and real scenarios
- **Visual Aids**: Use ASCII diagrams when helpful
- **Progressive Learning**: Start simple, build complexity
- **Cross-Reference**: Link to related exercises and techniques

## Quality Checklist

Before adding new exercises, verify:

### Exercise Module Checklist
- [ ] Functions have clear, descriptive names
- [ ] All functions include docstrings with examples
- [ ] Progressive difficulty (Basic → Intermediate → Advanced)
- [ ] Functions return appropriate default values (not None)
- [ ] Import statements are complete and correct

### Test Module Checklist
- [ ] All functions have corresponding tests
- [ ] Tests cover basic functionality + edge cases
- [ ] All tests have exactly 3 markers (technique, level, difficulty)
- [ ] Test methods have descriptive names and docstrings
- [ ] Edge cases include empty, single element, and boundary conditions

### Configuration Checklist
- [ ] New markers added to `pyproject.toml`
- [ ] Commands added to `justfile`
- [ ] Module imported in `__init__.py`
- [ ] CLAUDE.md updated with new module info
- [ ] Tutorial documentation created

### Verification Checklist
- [ ] `just test-new-technique` works
- [ ] `just show-markers` shows new markers
- [ ] Coverage remains above 80%
- [ ] All new tests run and fail appropriately (waiting for implementation)

## Example: Complete Addition Workflow

Here's a complete example of adding "Graph Algorithms":

1. **Create**: `src/py_dsa/graph_exercises.py`
2. **Create**: `tests/test_graph_exercises.py` 
3. **Update**: `pyproject.toml` with graph markers
4. **Update**: `justfile` with graph commands
5. **Update**: `src/py_dsa/__init__.py` with import
6. **Update**: `CLAUDE.md` with graph info
7. **Create**: `docs/graph-algorithms.md`
8. **Verify**: Run `just test-cov` and `just test-graph`

This systematic approach ensures consistency, maintainability, and comprehensive learning coverage across all DSA techniques.

---

## Getting Help

When contributing:
- Follow existing patterns in the codebase
- Run `just test-cov` to verify coverage
- Use `just show-markers` to verify marker configuration
- Check `just --list` to see all available commands

The goal is to maintain a high-quality, comprehensive learning platform that helps students master DSA concepts through progressive practice and thorough testing.