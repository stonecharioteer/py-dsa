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
    uv run uv run pytest

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