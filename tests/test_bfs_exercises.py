import pytest
from src.py_dsa.bfs_exercises import BFSExercises, TreeNode, GraphNode


class TestBFSExercises:
    """
    Comprehensive tests for BFS exercises with progressive difficulty.
    Run specific test groups using pytest markers.
    """
    
    def setup_method(self):
        self.bfs = BFSExercises()
    
    # Helper methods to create test trees
    def create_tree_1(self) -> TreeNode:
        """Creates tree: [3,9,20,null,null,15,7]"""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root
    
    def create_tree_2(self) -> TreeNode:
        """Creates tree: [1,2,3,null,5,null,4]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        return root
    
    def create_tree_3(self) -> TreeNode:
        """Creates tree: [1,2,3,4,5]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root
    
    # PREREQUISITE TESTS
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_implement_queue_with_list(self):
        """Test basic queue implementation understanding."""
        # This test will verify the student understands queue operations
        # The student should implement a Queue class in the method
        result = self.bfs.implement_queue_with_list()
        # Note: This is more of a practice exercise, actual testing would involve
        # the student creating a Queue class and testing its methods
        assert result is None  # Method should practice queue operations
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_tree_traversal_iterative_empty(self):
        """Test iterative traversal with empty tree."""
        result = self.bfs.tree_traversal_iterative(None)
        assert result == []
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_tree_traversal_iterative_single_node(self):
        """Test iterative traversal with single node."""
        root = TreeNode(1)
        result = self.bfs.tree_traversal_iterative(root)
        assert result == [1]
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_tree_traversal_iterative_multiple_nodes(self):
        """Test iterative traversal with multiple nodes."""
        root = self.create_tree_3()
        result = self.bfs.tree_traversal_iterative(root)
        # Should contain all node values (order may vary based on implementation)
        assert set(result) == {1, 2, 3, 4, 5}
        assert len(result) == 5
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_count_tree_nodes_empty(self):
        """Test counting nodes in empty tree."""
        result = self.bfs.count_tree_nodes(None)
        assert result == 0
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_count_tree_nodes_single(self):
        """Test counting nodes in single node tree."""
        root = TreeNode(1)
        result = self.bfs.count_tree_nodes(root)
        assert result == 1
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_count_tree_nodes_multiple(self):
        """Test counting nodes in multi-node tree."""
        root = self.create_tree_1()
        result = self.bfs.count_tree_nodes(root)
        assert result == 5
    
    # BASIC LEVEL TESTS
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_level_order_traversal_empty(self):
        """Test level order traversal with empty tree."""
        result = self.bfs.binary_tree_level_order_traversal(None)
        assert result == []
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_level_order_traversal_single(self):
        """Test level order traversal with single node."""
        root = TreeNode(1)
        result = self.bfs.binary_tree_level_order_traversal(root)
        assert result == [[1]]
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_level_order_traversal_complex(self):
        """Test level order traversal with complex tree."""
        root = self.create_tree_1()
        result = self.bfs.binary_tree_level_order_traversal(root)
        expected = [[3], [9, 20], [15, 7]]
        assert result == expected
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_right_side_view_empty(self):
        """Test right side view with empty tree."""
        result = self.bfs.binary_tree_right_side_view(None)
        assert result == []
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_right_side_view_single(self):
        """Test right side view with single node."""
        root = TreeNode(1)
        result = self.bfs.binary_tree_right_side_view(root)
        assert result == [1]
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_binary_tree_right_side_view_complex(self):
        """Test right side view with complex tree."""
        root = self.create_tree_2()
        result = self.bfs.binary_tree_right_side_view(root)
        expected = [1, 3, 4]
        assert result == expected
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_minimum_depth_empty(self):
        """Test minimum depth with empty tree."""
        result = self.bfs.minimum_depth_of_binary_tree(None)
        assert result == 0
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_minimum_depth_single(self):
        """Test minimum depth with single node."""
        root = TreeNode(1)
        result = self.bfs.minimum_depth_of_binary_tree(root)
        assert result == 1
    
    @pytest.mark.bfs
    @pytest.mark.bfs_basic
    @pytest.mark.easy
    def test_minimum_depth_complex(self):
        """Test minimum depth with complex tree."""
        root = self.create_tree_1()
        result = self.bfs.minimum_depth_of_binary_tree(root)
        assert result == 2
    
    # INTERMEDIATE LEVEL TESTS
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_zigzag_level_order_empty(self):
        """Test zigzag traversal with empty tree."""
        result = self.bfs.zigzag_level_order_traversal(None)
        assert result == []
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_zigzag_level_order_single(self):
        """Test zigzag traversal with single node."""
        root = TreeNode(1)
        result = self.bfs.zigzag_level_order_traversal(root)
        assert result == [[1]]
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_zigzag_level_order_complex(self):
        """Test zigzag traversal with complex tree."""
        root = self.create_tree_1()
        result = self.bfs.zigzag_level_order_traversal(root)
        expected = [[3], [20, 9], [15, 7]]
        assert result == expected
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_perfect_squares_small(self):
        """Test perfect squares with small numbers."""
        assert self.bfs.perfect_squares(1) == 1
        assert self.bfs.perfect_squares(4) == 1
        assert self.bfs.perfect_squares(8) == 2
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_perfect_squares_medium(self):
        """Test perfect squares with medium numbers."""
        assert self.bfs.perfect_squares(12) == 3
        assert self.bfs.perfect_squares(13) == 2
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_rotting_oranges_no_fresh(self):
        """Test rotting oranges with no fresh oranges."""
        grid = [[2, 2], [2, 2]]
        result = self.bfs.rotting_oranges(grid)
        assert result == 0
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_rotting_oranges_impossible(self):
        """Test rotting oranges where some fresh oranges can't be reached."""
        grid = [[2, 1, 0, 1]]
        result = self.bfs.rotting_oranges(grid)
        assert result == -1
    
    @pytest.mark.bfs
    @pytest.mark.bfs_intermediate
    @pytest.mark.medium
    def test_rotting_oranges_normal(self):
        """Test rotting oranges normal case."""
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        result = self.bfs.rotting_oranges(grid)
        assert result == 4
    
    # ADVANCED LEVEL TESTS
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_word_ladder_no_path(self):
        """Test word ladder when no path exists."""
        result = self.bfs.word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        assert result == 0
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_word_ladder_direct(self):
        """Test word ladder with direct path."""
        result = self.bfs.word_ladder("hit", "hot", ["hot"])
        assert result == 2
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_word_ladder_complex(self):
        """Test word ladder with complex path."""
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = self.bfs.word_ladder("hit", "cog", word_list)
        assert result == 5
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_open_the_lock_simple(self):
        """Test open lock with simple case."""
        result = self.bfs.open_the_lock(["8888"], "0009")
        assert result == 1
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_open_the_lock_impossible(self):
        """Test open lock when impossible."""
        result = self.bfs.open_the_lock(["0000"], "8888")
        assert result == -1
    
    @pytest.mark.bfs
    @pytest.mark.bfs_advanced
    @pytest.mark.hard
    def test_open_the_lock_complex(self):
        """Test open lock with complex case."""
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        result = self.bfs.open_the_lock(deadends, "0202")
        assert result == 6