# DSA Learning Platform - Just Commands
# Run `just --list` to see all available commands

# Default recipe - show help
default:
    @just --list

# Install development dependencies
install:
    uv sync --dev

# Run all tests
test:
    uv run pytest

# Run tests with coverage report
test-cov:
    uv run uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# Run tests and open coverage report in browser
test-cov-open: test-cov
    @echo "Opening coverage report..."
    @python -c "import webbrowser; webbrowser.open('htmlcov/index.html')"

# Run specific exercise category tests
test-fundamentals:
    uv run pytest -m fundamentals

test-sliding-window:
    uv run pytest -m sliding_window

test-two-pointers:
    uv run pytest -m two_pointers

test-bfs:
    uv run pytest -m bfs

test-dp:
    uv run pytest -m dp

test-backtracking:
    uv run pytest -m backtracking

test-linked-list:
    uv run pytest -m linked_list

test-greedy:
    uv run pytest -m greedy

test-union-find:
    uv run pytest -m union_find

test-bit-manipulation:
    uv run pytest -m bit_manipulation

test-binary-search:
    uv run pytest -m binary_search

test-graph:
    uv run pytest -m graph

test-stack-queue:
    uv run pytest -m stack_queue

test-trie:
    uv run pytest -m trie

test-heap:
    uv run pytest -m heap

test-blind150:
    uv run pytest -m blind150

test-numpy:
    uv run pytest -m numpy

test-pandas:
    uv run pytest -m pandas

test-string-algorithms:
    uv run pytest -m string_algorithms

test-sorting:
    uv run pytest -m sorting

test-pytorch:
    uv run pytest -m pytorch

test-pydantic:
    uv run pytest -m pydantic

test-fastapi:
    uv run pytest -m fastapi

# Run tests by difficulty level
test-easy:
    uv run pytest -m easy

test-medium:
    uv run pytest -m medium

test-hard:
    uv run pytest -m hard

# Run specific technique difficulty levels
test-fundamentals-easy:
    uv run pytest -m "fundamentals and easy"

test-sliding-window-basic:
    uv run pytest -m sliding_window_basic

test-sliding-window-intermediate:
    uv run pytest -m sliding_window_intermediate

test-sliding-window-advanced:
    uv run pytest -m sliding_window_advanced

test-two-pointers-basic:
    uv run pytest -m two_pointers_basic

test-two-pointers-intermediate:
    uv run pytest -m two_pointers_intermediate

test-two-pointers-advanced:
    uv run pytest -m two_pointers_advanced

test-bfs-basic:
    uv run pytest -m bfs_basic

test-bfs-intermediate:
    uv run pytest -m bfs_intermediate

test-bfs-advanced:
    uv run pytest -m bfs_advanced

test-dp-basic:
    uv run pytest -m dp_basic

test-dp-intermediate:
    uv run pytest -m dp_intermediate

test-dp-advanced:
    uv run pytest -m dp_advanced

test-backtracking-basic:
    uv run pytest -m backtracking_basic

test-backtracking-intermediate:
    uv run pytest -m backtracking_intermediate

test-backtracking-advanced:
    uv run pytest -m backtracking_advanced

test-string-algorithms-basic:
    uv run pytest -m string_algorithms_basic

test-string-algorithms-intermediate:
    uv run pytest -m string_algorithms_intermediate

test-string-algorithms-advanced:
    uv run pytest -m string_algorithms_advanced

# Watch for file changes and run tests
watch:
    watchexec --restart --clear --exts py -- uv run pytest

# Watch and run tests with coverage
watch-cov:
    watchexec --restart --clear --exts py -- uv run pytest --cov=src --cov-report=term-missing

# Watch specific test categories
watch-fundamentals:
    watchexec --restart --clear --exts py -- uv run pytest -m fundamentals

watch-sliding-window:
    watchexec --restart --clear --exts py -- uv run pytest -m sliding_window

watch-two-pointers:
    watchexec --restart --clear --exts py -- uv run pytest -m two_pointers

watch-bfs:
    watchexec --restart --clear --exts py -- uv run pytest -m bfs

watch-dp:
    watchexec --restart --clear --exts py -- uv run pytest -m dp

watch-backtracking:
    watchexec --restart --clear --exts py -- uv run pytest -m backtracking

watch-linked-list:
    watchexec --restart --clear --exts py -- uv run pytest -m linked_list

watch-greedy:
    watchexec --restart --clear --exts py -- uv run pytest -m greedy

watch-union-find:
    watchexec --restart --clear --exts py -- uv run pytest -m union_find

watch-bit-manipulation:
    watchexec --restart --clear --exts py -- uv run pytest -m bit_manipulation

watch-binary-search:
    watchexec --restart --clear --exts py -- uv run pytest -m binary_search

watch-graph:
    watchexec --restart --clear --exts py -- uv run pytest -m graph

watch-blind150:
    watchexec --restart --clear --exts py -- uv run pytest -m blind150

watch-numpy:
    watchexec --restart --clear --exts py -- uv run pytest -m numpy

watch-pandas:
    watchexec --restart --clear --exts py -- uv run pytest -m pandas

watch-string-algorithms:
    watchexec --restart --clear --exts py -- uv run pytest -m string_algorithms

watch-sorting:
    watchexec --restart --clear --exts py -- uv run pytest -m sorting

watch-pytorch:
    watchexec --restart --clear --exts py -- uv run pytest -m pytorch

watch-pydantic:
    watchexec --restart --clear --exts py -- uv run pytest -m pydantic

watch-fastapi:
    watchexec --restart --clear --exts py -- uv run pytest -m fastapi

# Watch by difficulty
watch-easy:
    watchexec --restart --clear --exts py -- uv run pytest -m easy

watch-medium:
    watchexec --restart --clear --exts py -- uv run pytest -m medium

watch-hard:
    watchexec --restart --clear --exts py -- uv run pytest -m hard

# Run specific test file
test-file file:
    uv run pytest {{file}}

# Watch specific test file
watch-file file:
    watchexec --restart --clear --exts py -- uv run pytest {{file}}

# Clean coverage files
clean:
    rm -rf htmlcov/
    rm -rf .coverage
    rm -rf .uv run pytest_cache/
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete

# Run the main script
run:
    python -m py_dsa

# Format code (if you add formatting tools later)
fmt:
    @echo "No formatter configured yet. Consider adding black or ruff."

# Lint code (if you add linting tools later)
lint:
    @echo "No linter configured yet. Consider adding ruff or pylint."

# Show test markers
show-markers:
    uv run pytest --markers

# Show coverage for all test categories sorted by coverage percentage
coverage:
    #!/usr/bin/env bash
    echo "📊 Test Coverage Report - Sorted by Coverage Percentage"
    echo "========================================================"
    echo ""
    
    # Function to get coverage for a specific marker
    get_coverage() {
        local marker="$1"
        local name="$2"
        coverage_output=$(uv run pytest -m "$marker" --cov=src --cov-report=term --tb=no --quiet 2>/dev/null | grep "TOTAL" | awk '{print $4}' | sed 's/%//')
        if [[ -n "$coverage_output" && "$coverage_output" != "0" ]]; then
            printf "%-35s %3s%%\n" "$name" "$coverage_output"
        else
            printf "%-35s %3s%%\n" "$name" "0"
        fi
    }
    
    # Core DSA categories
    echo "🚀 Core DSA Categories:"
    get_coverage "bit_manipulation" "Bit Manipulation"
    get_coverage "sliding_window" "Sliding Window"
    get_coverage "heap" "Heap & Priority Queue"
    get_coverage "string_algorithms" "String Algorithms"
    get_coverage "two_pointers" "Two Pointers"
    get_coverage "greedy" "Greedy Algorithms"
    get_coverage "backtracking" "Backtracking"
    get_coverage "fundamentals" "Fundamentals"
    get_coverage "linked_list" "Linked Lists"
    get_coverage "dp" "Dynamic Programming"
    get_coverage "graph" "Graph Algorithms"
    get_coverage "binary_search" "Binary Search"
    get_coverage "trie" "Trie (Prefix Tree)"
    get_coverage "stack_queue" "Stack & Queue"
    get_coverage "bfs" "Breadth-First Search"
    get_coverage "union_find" "Union Find"
    echo ""
    
    # Data Science categories
    echo "🔬 Data Science & ML:"
    get_coverage "numpy" "NumPy"
    get_coverage "pandas" "Pandas"
    get_coverage "pytorch" "PyTorch"
    echo ""
    
    # Web Development categories
    echo "🌐 Web Development:"
    get_coverage "fastapi" "FastAPI"
    get_coverage "pydantic" "Pydantic"
    echo ""
    
    # Interview Prep
    echo "🎯 Interview Preparation:"
    get_coverage "blind150" "Blind 150"
    echo ""
    
    # Difficulty levels
    echo "📈 By Difficulty Level:"
    get_coverage "easy" "Easy Problems"
    get_coverage "medium" "Medium Problems" 
    get_coverage "hard" "Hard Problems"
    echo ""
    
    # Overall coverage
    echo "📊 Overall Project Coverage:"
    uv run pytest --cov=src --cov-report=term --tb=no --quiet 2>/dev/null | grep "TOTAL" | awk '{printf "%-35s %s\n", "Total Project Coverage", $4}'
    echo ""
    echo "💡 Note: Low coverage in some modules is expected - they're learning exercises!"
    echo "   High coverage indicates working examples with thorough test validation."

# Show coverage with detailed breakdown by module
coverage-detailed:
    @echo "📊 Detailed Coverage Report by Module"
    @echo "====================================="
    uv run pytest --cov=src --cov-report=term-missing --tb=no --quiet 2>/dev/null | grep -A 100 "coverage:"

# Run a single test by name pattern
test-match pattern:
    uv run pytest -k "{{pattern}}"

# Watch and run tests matching pattern
watch-match pattern:
    watchexec --restart --clear --exts py -- uv run pytest -k "{{pattern}}"

# Development workflow - install deps and run tests
dev: install
    uv run pytest

# Show project structure
tree:
    @echo "Project structure:"
    @find . -type f -name "*.py" | head -20 | sort
    @echo "\nTest files:"
    @find tests/ -name "*.py" | sort
    @echo "\nDocs:"
    @find docs/ -name "*.md" | sort || echo "No docs found"
