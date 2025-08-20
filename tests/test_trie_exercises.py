import pytest
from src.py_dsa.trie_exercises import TrieExercises


class TestTrieExercises:
    """
    Tests for Trie (Prefix Tree) data structure exercises.
    Essential for efficient string operations and prefix-based searches.
    """
    
    def setup_method(self):
        self.trie = TrieExercises()
    
    # BASIC TRIE TESTS
    
    @pytest.mark.trie
    @pytest.mark.medium
    def test_implement_trie_basic_operations(self):
        """Test basic trie operations: insert, search, startsWith."""
        trie = self.trie.implement_trie()
        
        # Test insert and search
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        
        trie.insert("app")
        assert trie.search("app") == True
    
    @pytest.mark.trie
    @pytest.mark.medium
    def test_implement_trie_multiple_words(self):
        """Test trie with multiple words."""
        trie = self.trie.implement_trie()
        
        words = ["cat", "car", "card", "care", "careful"]
        for word in words:
            trie.insert(word)
        
        # Test all words exist
        for word in words:
            assert trie.search(word) == True
        
        # Test prefixes
        assert trie.startsWith("ca") == True
        assert trie.startsWith("car") == True
        assert trie.startsWith("care") == True
        assert trie.startsWith("xyz") == False
    
    @pytest.mark.trie
    @pytest.mark.medium
    def test_word_search_2_basic(self):
        """Test word search in 2D board basic case."""
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = self.trie.word_search_2(board, words)
        expected = ["eat", "oath"]
        assert set(result) == set(expected)
    
    @pytest.mark.trie
    @pytest.mark.medium
    def test_word_search_2_no_matches(self):
        """Test word search when no words are found."""
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        result = self.trie.word_search_2(board, words)
        assert result == []
    
    @pytest.mark.trie
    @pytest.mark.hard
    def test_longest_word_basic(self):
        """Test finding longest word built one character at a time."""
        words = ["w", "wo", "wor", "worl", "world"]
        result = self.trie.longest_word(words)
        assert result == "world"
    
    @pytest.mark.trie
    @pytest.mark.hard
    def test_longest_word_tie_breaker(self):
        """Test longest word with lexicographical tie breaker."""
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        result = self.trie.longest_word(words)
        assert result == "apple"  # "apple" and "apply" both length 5, "apple" comes first lexicographically
    
    @pytest.mark.trie
    @pytest.mark.hard
    def test_longest_word_no_valid(self):
        """Test longest word when no valid word can be built."""
        words = ["abc", "def", "ghi"]
        result = self.trie.longest_word(words)
        assert result == ""