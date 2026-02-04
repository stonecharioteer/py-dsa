import pytest
from src.py_dsa.graph_exercises import GraphExercises


class TestGraphExercises:
    """
    Tests for graph algorithms covering DFS, BFS, pathfinding, and advanced graph techniques.
    Essential for understanding complex data relationships and optimization problems.
    """
    
    def setup_method(self):
        self.graph = GraphExercises()
    
    # Helper method to create test graphs
    def get_simple_graph(self):
        """Returns simple connected graph: {0: [1,2], 1: [0,2], 2: [0,1,3], 3: [2]}"""
        return {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    
    def get_disconnected_graph(self):
        """Returns disconnected graph with multiple components."""
        return {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
    
    # BASIC GRAPH REPRESENTATION TESTS
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_build_adjacency_list_basic(self):
        """Test building adjacency list from edge list."""
        edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
        result = self.graph.build_adjacency_list(4, edges)
        expected = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        
        # Check that all nodes are present
        assert set(result.keys()) == set(expected.keys())
        # Check adjacency lists (order may vary)
        for node in expected:
            assert set(result[node]) == set(expected[node])
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_build_adjacency_list_empty(self):
        """Test building adjacency list with no edges."""
        result = self.graph.build_adjacency_list(3, [])
        expected = {0: [], 1: [], 2: []}
        assert result == expected
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_build_adjacency_list_single_edge(self):
        """Test building adjacency list with single edge."""
        result = self.graph.build_adjacency_list(2, [[0, 1]])
        expected = {0: [1], 1: [0]}
        assert set(result[0]) == set(expected[0])
        assert set(result[1]) == set(expected[1])
    
    # DFS TRAVERSAL TESTS
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_dfs_iterative_simple(self):
        """Test DFS iterative traversal on simple graph."""
        graph = self.get_simple_graph()
        result = self.graph.dfs_iterative(graph, 0)
        
        # Should visit all nodes
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}
        # Should start with the given node
        assert result[0] == 0
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_dfs_iterative_single_node(self):
        """Test DFS on graph with single node."""
        graph = {0: []}
        result = self.graph.dfs_iterative(graph, 0)
        assert result == [0]
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_dfs_iterative_linear(self):
        """Test DFS on linear graph."""
        graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
        result = self.graph.dfs_iterative(graph, 0)
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}
        assert result[0] == 0
    
    # BFS TRAVERSAL TESTS
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_bfs_iterative_simple(self):
        """Test BFS iterative traversal on simple graph."""
        graph = self.get_simple_graph()
        result = self.graph.bfs_iterative(graph, 0)
        
        # Should visit all nodes
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}
        # Should start with the given node
        assert result[0] == 0
        # BFS should visit neighbors before going deeper
        # Node 0's neighbors (1,2) should come before node 3
        assert result.index(3) > result.index(1)
        assert result.index(3) > result.index(2)
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_bfs_iterative_single_node(self):
        """Test BFS on graph with single node."""
        graph = {0: []}
        result = self.graph.bfs_iterative(graph, 0)
        assert result == [0]
    
    @pytest.mark.graph
    @pytest.mark.easy
    def test_bfs_iterative_tree_structure(self):
        """Test BFS on tree-like structure."""
        # Tree: 0 -> [1,2], 1 -> [3,4], 2 -> [5,6]
        graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5, 6], 3: [1], 4: [1], 5: [2], 6: [2]}
        result = self.graph.bfs_iterative(graph, 0)
        
        assert len(result) == 7
        assert result[0] == 0
        # Level 1: nodes 1,2 should come before level 2: nodes 3,4,5,6
        level1_indices = [result.index(1), result.index(2)]
        level2_indices = [result.index(3), result.index(4), result.index(5), result.index(6)]
        assert max(level1_indices) < min(level2_indices)
    
    @pytest.mark.graph
    @pytest.mark.medium
    def test_graph_algorithms_consistency(self):
        """Test that DFS and BFS visit all reachable nodes."""
        graph = self.get_simple_graph()
        dfs_result = self.graph.dfs_iterative(graph, 0)
        bfs_result = self.graph.bfs_iterative(graph, 0)
        
        # Both should visit exactly the same set of nodes
        assert set(dfs_result) == set(bfs_result)
        assert len(dfs_result) == len(bfs_result) == 4