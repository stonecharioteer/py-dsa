from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple, Optional
import heapq


class GraphExercises:
    """
    Graph Algorithms and Pathfinding exercises with progressive difficulty.
    
    Covers graph representation, traversal, pathfinding, and advanced algorithms.
    Graphs can be represented as adjacency lists, adjacency matrices, or edge lists.
    """
    
    # BASIC EXERCISES - Graph representation and basic traversal
    
    def build_adjacency_list(self, n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        """
        Basic: Build adjacency list representation from edge list.
        
        Example:
        Input: n = 4, edges = [[0,1],[0,2],[1,2],[2,3]]
        Output: {0: [1,2], 1: [0,2], 2: [0,1,3], 3: [2]}
        
        TODO: Create adjacency list for undirected graph
        """
        return {}
    
    def dfs_iterative(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Basic: Depth-First Search using iterative approach with stack.
        
        Example:
        Input: graph = {0: [1,2], 1: [0,2], 2: [0,1,3], 3: [2]}, start = 0
        Output: [0, 2, 3, 1] (one possible DFS order)
        
        TODO: Use stack for iterative DFS traversal
        """
        return []
    
    def bfs_iterative(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Basic: Breadth-First Search using iterative approach with queue.
        
        Example:
        Input: graph = {0: [1,2], 1: [0,2], 2: [0,1,3], 3: [2]}, start = 0
        Output: [0, 1, 2, 3] (BFS level order)
        
        TODO: Use queue for BFS traversal
        """
        return []
    
    def has_path_dfs(self, graph: Dict[int, List[int]], start: int, end: int) -> bool:
        """
        Basic: Check if path exists between two nodes using DFS.
        
        Example:
        Input: graph = {0: [1,2], 1: [3], 2: [], 3: []}, start = 0, end = 3
        Output: True
        
        TODO: Use DFS to find if path exists
        """
        return False
    
    # INTERMEDIATE EXERCISES - Pathfinding algorithms
    
    def shortest_path_unweighted(self, graph: Dict[int, List[int]], start: int, end: int) -> List[int]:
        """
        Intermediate: Find shortest path in unweighted graph using BFS.
        
        Example:
        Input: graph = {0: [1,2], 1: [3], 2: [3], 3: []}, start = 0, end = 3
        Output: [0, 1, 3] or [0, 2, 3]
        
        TODO: Use BFS with parent tracking to reconstruct path
        """
        return []
    
    def dijkstra_shortest_path(self, graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
        """
        Intermediate: Dijkstra's algorithm for shortest paths from source.
        
        Example:
        Input: graph = {0: [(1,4), (2,1)], 1: [(3,1)], 2: [(1,2), (3,5)], 3: []}
        Output: {0: 0, 1: 3, 2: 1, 3: 4}
        
        TODO: Use priority queue for Dijkstra's algorithm
        """
        return {}
    
    def detect_cycle_undirected(self, n: int, edges: List[List[int]]) -> bool:
        """
        Intermediate: Detect cycle in undirected graph using DFS.
        
        Example:
        Input: n = 4, edges = [[0,1],[1,2],[2,3],[3,1]]
        Output: True (cycle: 1-2-3-1)
        
        TODO: Use DFS with parent tracking
        """
        return False
    
    def detect_cycle_directed(self, graph: Dict[int, List[int]]) -> bool:
        """
        Intermediate: Detect cycle in directed graph using DFS.
        
        Example:
        Input: graph = {0: [1], 1: [2], 2: [0]}
        Output: True (cycle: 0->1->2->0)
        
        TODO: Use DFS with recursion stack coloring
        """
        return False
    
    def topological_sort(self, graph: Dict[int, List[int]]) -> List[int]:
        """
        Intermediate: Topological sorting of directed acyclic graph.
        
        Example:
        Input: graph = {0: [1,2], 1: [3], 2: [3], 3: []}
        Output: [0, 1, 2, 3] or [0, 2, 1, 3]
        
        TODO: Use DFS with post-order or Kahn's algorithm
        """
        return []
    
    # ADVANCED EXERCISES - Complex graph algorithms
    
    def a_star_pathfinding(self, grid: List[List[int]], start: Tuple[int, int], 
                          goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Advanced: A* pathfinding algorithm in 2D grid.
        
        Example:
        Input: grid = [[0,0,0],[0,1,0],[0,0,0]], start = (0,0), goal = (2,2)
        Output: [(0,0), (0,1), (0,2), (1,2), (2,2)]
        
        TODO: Use priority queue with f(n) = g(n) + h(n) heuristic
        """
        return []
    
    def minimum_spanning_tree_kruskal(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Advanced: Find MST using Kruskal's algorithm with Union-Find.
        
        Example:
        Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,3],[0,3,4]]
        Output: [[0,1,1],[1,2,3],[2,3,3]] (total weight = 7)
        
        TODO: Sort edges by weight and use Union-Find
        """
        return []
    
    def minimum_spanning_tree_prim(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Advanced: Find MST using Prim's algorithm with priority queue.
        
        Example:
        Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,3],[0,3,4]]
        Output: [[0,1,1],[1,2,3],[2,3,3]] (total weight = 7)
        
        TODO: Use priority queue starting from arbitrary vertex
        """
        return []
    
    def strongly_connected_components(self, graph: Dict[int, List[int]]) -> List[List[int]]:
        """
        Advanced: Find strongly connected components using Kosaraju's algorithm.
        
        Example:
        Input: graph = {0: [1], 1: [2], 2: [0,3], 3: [4], 4: [5,7], 5: [6], 6: [4], 7: []}
        Output: [[0,1,2], [3], [4,5,6], [7]]
        
        TODO: Two-pass DFS with graph transpose
        """
        return []
    
    def all_paths_source_target(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Advanced: Find all paths from source (0) to target (n-1) in DAG.
        
        Example:
        Input: graph = [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
        
        TODO: Use DFS with backtracking to find all paths
        """
        return []
    
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Advanced: Find minimum time for signal to reach all nodes.
        
        Example:
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
        
        TODO: Use Dijkstra to find max of shortest paths
        """
        return -1
    
    def cheapest_flights_with_k_stops(self, n: int, flights: List[List[int]], 
                                    src: int, dst: int, k: int) -> int:
        """
        Advanced: Find cheapest flight with at most k stops.
        
        Example:
        Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
        Output: 200
        
        TODO: Use modified Dijkstra or Bellman-Ford with stop constraints
        """
        return -1
    
    def word_ladder_ii(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        """
        Advanced: Find all shortest transformation sequences (BFS + DFS).
        
        Example:
        Input: begin = "hit", end = "cog", words = ["hot","dot","dog","lot","log","cog"]
        Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        
        TODO: Use BFS to find shortest path length, then DFS for all paths
        """
        return []


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.
    Used for efficiently detecting cycles and MST algorithms.
    """
    
    def __init__(self, n: int):
        """Initialize Union-Find with n elements."""
        # TODO: Initialize parent and rank arrays
        pass
    
    def find(self, x: int) -> int:
        """Find root of element x with path compression."""
        # TODO: Implement find with path compression
        return x
    
    def union(self, x: int, y: int) -> bool:
        """Union two sets. Return True if they were different sets."""
        # TODO: Implement union by rank
        return False
    
    def connected(self, x: int, y: int) -> bool:
        """Check if two elements are in the same set."""
        return self.find(x) == self.find(y)