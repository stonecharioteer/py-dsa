from typing import List, Dict, Optional


class TrieExercises:
    """
    Trie (Prefix Tree) exercises with progressive difficulty.
    
    A trie is a tree-like data structure for storing strings efficiently.
    Each node represents a character, and paths represent words.
    
    Excellent for:
    - Autocomplete systems
    - Spell checkers  
    - IP routing tables
    - Word games (Scrabble, Boggle)
    """
    
    # BASIC EXERCISES - Understanding trie fundamentals
    
    def implement_trie(self) -> 'Trie':
        """
        Basic: Implement basic trie with insert, search, startsWith.
        
        Example:
        trie = Trie()
        trie.insert("apple")
        trie.search("apple")   // returns True
        trie.startsWith("app") // returns True
        
        TODO: Create Trie class with basic operations
        """
        return Trie()
    
    def word_dictionary_with_wildcards(self) -> 'WordDictionary':
        """
        Basic: Implement word dictionary that supports wildcards.
        
        Example:
        wd = WordDictionary()
        wd.addWord("bad")
        wd.search("pad")  // False  
        wd.search("bad")  // True
        wd.search(".ad")  // True (. matches any character)
        
        TODO: Extend trie to handle '.' wildcard character
        """
        return WordDictionary()
    
    def longest_word_in_dictionary(self, words: List[str]) -> str:
        """
        Basic: Find longest word that can be built one character at a time.
        
        Example:
        Input: words = ["w","wo","wor","worl","world"]
        Output: "world"
        
        TODO: Build trie and find longest buildable word
        """
        return ""
    
    def short_encoding_of_words(self, words: List[str]) -> int:
        """
        Basic: Find minimum length to encode words as suffixes.
        
        Example:
        Input: words = ["time", "me", "bell"]
        Output: 10 ("time#bell#" - "me" is suffix of "time")
        
        TODO: Use trie to eliminate words that are suffixes
        """
        return 0
    
    # INTERMEDIATE EXERCISES - Trie with additional functionality
    
    def map_sum_pairs(self) -> 'MapSum':
        """
        Intermediate: Implement map that sums values by prefix.
        
        Example:
        mapSum = MapSum()
        mapSum.insert("apple", 3)
        mapSum.sum("ap")  // returns 3
        mapSum.insert("app", 2)
        mapSum.sum("ap")  // returns 5 (apple + app)
        
        TODO: Extend trie to store and sum values
        """
        return MapSum()
    
    def replace_words(self, dictionary: List[str], sentence: str) -> str:
        """
        Intermediate: Replace words with their roots from dictionary.
        
        Example:
        Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"
        
        TODO: Use trie to find shortest matching prefix
        """
        return ""
    
    def palindrome_pairs(self, words: List[str]) -> List[List[int]]:
        """
        Intermediate: Find all pairs that form palindromes when concatenated.
        
        Example:
        Input: words = ["lls","s","sssll"]
        Output: [[0,1],[1,0]] ("lls" + "s" and "s" + "lls" form palindromes)
        
        TODO: Use trie with reverse strings and palindrome checking
        """
        return []
    
    def stream_of_characters(self) -> 'StreamChecker':
        """
        Intermediate: Check if any suffix of query stream matches dictionary words.
        
        Example:
        sc = StreamChecker(["cd","f","kl"])
        sc.query('a')  // False
        sc.query('b')  // False  
        sc.query('c')  // False
        sc.query('d')  // True (matches "cd")
        
        TODO: Use trie with reverse words for suffix matching
        """
        return StreamChecker([])
    
    # ADVANCED EXERCISES - Complex trie applications
    
    def word_search_ii(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Advanced: Find all words from dictionary in 2D board.
        
        Example:
        Input: board = [["o","a","a","n"],["e","t","a","e"]], words = ["eat","oath","pea"]
        Output: ["eat","oath"]
        
        TODO: Build trie + DFS with backtracking on board
        """
        return []
    
    def autocomplete_system(self) -> 'AutocompleteSystem':
        """
        Advanced: Design autocomplete system with hot sentences ranking.
        
        Example:
        ac = AutocompleteSystem(["i love you", "island"], [5, 3])
        ac.input('i')  // ["i love you", "island"] 
        ac.input(' ')  // ["i love you"]
        
        TODO: Trie with frequency tracking and top-k retrieval
        """
        return AutocompleteSystem([], [])
    
    def concatenated_words(self, words: List[str]) -> List[str]:
        """
        Advanced: Find all concatenated words (made of 2+ other words).
        
        Example:
        Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog"]
        Output: ["catsdogcats","dogcatsdog"]
        
        TODO: Use trie + DFS to check if word can be broken down
        """
        return []
    
    def design_search_autocomplete(self) -> 'SearchAutocomplete':
        """
        Advanced: Design Google-like search autocomplete with ranking.
        
        Features:
        - Add sentences with frequencies
        - Get top 3 suggestions for prefix
        - Update frequencies based on user selection
        
        TODO: Trie + heap for top-k suggestions with dynamic updates
        """
        return SearchAutocomplete()


# Helper classes that students should implement

class TrieNode:
    """Standard trie node structure."""
    
    def __init__(self):
        # TODO: Initialize children dict and end marker
        pass


class Trie:
    """Basic trie implementation."""
    
    def __init__(self):
        # TODO: Initialize root node
        pass
    
    def insert(self, word: str) -> None:
        # TODO: Insert word into trie
        pass
    
    def search(self, word: str) -> bool:
        # TODO: Search for exact word
        return False
    
    def startsWith(self, prefix: str) -> bool:
        # TODO: Check if any word starts with prefix
        return False


class WordDictionary:
    """Word dictionary with wildcard support."""
    
    def __init__(self):
        # TODO: Initialize trie
        pass
    
    def addWord(self, word: str) -> None:
        # TODO: Add word to dictionary
        pass
    
    def search(self, word: str) -> bool:
        # TODO: Search with '.' wildcard support
        return False


class MapSum:
    """Map that supports prefix sum queries."""
    
    def __init__(self):
        # TODO: Initialize trie with values
        pass
    
    def insert(self, key: str, val: int) -> None:
        # TODO: Insert key-value pair
        pass
    
    def sum(self, prefix: str) -> int:
        # TODO: Return sum of all values with given prefix
        return 0


class StreamChecker:
    """Stream character checker using trie."""
    
    def __init__(self, words: List[str]):
        # TODO: Build trie from words
        pass
    
    def query(self, letter: str) -> bool:
        # TODO: Check if any suffix matches dictionary word
        return False


class AutocompleteSystem:
    """Autocomplete system with frequency ranking."""
    
    def __init__(self, sentences: List[str], times: List[int]):
        # TODO: Build trie with sentence frequencies
        pass
    
    def input(self, c: str) -> List[str]:
        # TODO: Return top 3 suggestions for current input
        return []


class SearchAutocomplete:
    """Advanced search autocomplete with dynamic ranking."""
    
    def __init__(self):
        # TODO: Initialize advanced trie structure
        pass
    
    def add_sentence(self, sentence: str, frequency: int) -> None:
        # TODO: Add sentence with initial frequency
        pass
    
    def search(self, prefix: str, k: int = 3) -> List[str]:
        # TODO: Return top k suggestions for prefix
        return []
    
    def select(self, sentence: str) -> None:
        # TODO: Update frequency when user selects suggestion
        pass