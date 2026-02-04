# Heap & Priority Queue: Real-World Applications Guide

Heaps are one of the most practically useful data structures in software development. Unlike abstract algorithm puzzles, heap problems directly translate to real systems you'll build.

## What Problems Do Heaps Solve?

**Core Problem**: "I need to efficiently find and remove the most important item from a collection that's constantly changing."

This pattern appears everywhere in production systems:
- **Task scheduling** - Which job should run next?  
- **Resource management** - Which request gets the CPU/memory?
- **Recommendation systems** - What are the top K most relevant items?
- **Monitoring & alerting** - Which errors are most critical?

## Real-World Use Cases by Exercise

### **Basic Level - Foundation Concepts**

#### **Kth Largest Element** → **System Monitoring**
```python
def kth_largest_element(self, nums: List[int], k: int) -> int:
```
**Real Use Case**: **Server load monitoring dashboard**
- **Scenario**: You have hundreds of servers reporting CPU usage every minute
- **Problem**: Dashboard needs to show "95th percentile CPU usage" in real-time
- **Solution**: Maintain a min-heap of size 5% of servers. The top shows 95th percentile
- **Why Heap?**: O(log k) insertion vs O(n log n) full sort every minute

**Production Example**:
```python
class ServerMonitor:
    def __init__(self, percentile=95):
        self.k = int(100 - percentile)  # For 95th percentile, track top 5%
        self.heap = []  # Min heap for kth largest
    
    def report_cpu_usage(self, server_id: str, cpu_percent: float):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, cpu_percent)
        elif cpu_percent > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, cpu_percent)
    
    def get_95th_percentile(self) -> float:
        return self.heap[0] if self.heap else 0.0
```

#### **Last Stone Weight** → **Resource Pool Management**
```python
def last_stone_weight(self, stones: List[int]) -> int:
```
**Real Use Case**: **Container resource allocation**
- **Scenario**: Kubernetes pods with different memory requirements need scheduling
- **Problem**: Efficiently pair pods to minimize resource waste on nodes
- **Solution**: Always combine the two largest resource requirements first
- **Why Heap?**: Constantly need the largest available resources - perfect for max heap

#### **Merge K Sorted Lists** → **Log Aggregation**
```python
def merge_k_sorted_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
```
**Real Use Case**: **Distributed log aggregation (like ELK stack)**
- **Scenario**: Collecting logs from 50 microservices, each sending time-ordered events
- **Problem**: Merge all logs into single chronological stream for analysis
- **Solution**: Heap tracks the next earliest event from each service
- **Why Heap?**: Need minimum timestamp from K streams - min heap is perfect

**Production Example**:
```python
class LogAggregator:
    def __init__(self, log_streams: List[Iterator]):
        self.heap = []
        for i, stream in enumerate(log_streams):
            try:
                log_entry = next(stream)
                heapq.heappush(self.heap, (log_entry.timestamp, i, log_entry, stream))
            except StopIteration:
                pass
    
    def get_next_chronological_entry(self):
        if not self.heap:
            return None
        
        timestamp, stream_id, entry, stream = heapq.heappop(self.heap)
        
        # Add next entry from this stream
        try:
            next_entry = next(stream)
            heapq.heappush(self.heap, (next_entry.timestamp, stream_id, next_entry, stream))
        except StopIteration:
            pass
        
        return entry
```

### **Intermediate Level - Production Systems**

#### **Top K Frequent Elements** → **Analytics & Recommendations**
```python
def top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
```
**Real Use Cases**:
1. **E-commerce recommendations**: "Customers who bought X also bought..." (top K co-purchased items)
2. **Social media trending**: Top K hashtags/topics in real-time
3. **Error monitoring**: Top K most frequent errors for debugging priority

**Production Example - Social Media Trending**:
```python
class TrendingHashtags:
    def __init__(self, k=10):
        self.k = k
        self.frequency = defaultdict(int)
        self.heap = []  # Min heap of (frequency, hashtag)
    
    def add_post(self, hashtags: List[str]):
        for hashtag in hashtags:
            old_freq = self.frequency[hashtag]
            self.frequency[hashtag] += 1
            new_freq = self.frequency[hashtag]
            
            # Update heap efficiently
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, (new_freq, hashtag))
            elif new_freq > self.heap[0][0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, (new_freq, hashtag))
    
    def get_trending_topics(self) -> List[str]:
        return [hashtag for freq, hashtag in sorted(self.heap, reverse=True)]
```

#### **Task Scheduler** → **CPU/Thread Pool Management**
```python
def task_scheduler(self, tasks: List[str], n: int) -> int:
```
**Real Use Case**: **Operating system process scheduling**
- **Scenario**: OS needs to schedule processes with minimum context-switch overhead
- **Problem**: Some processes can't run immediately after finishing (cooldown for I/O)
- **Solution**: Heap tracks which processes are ready, queue manages cooldown
- **Why Heap?**: Need highest priority ready process at any moment

#### **K Closest Points** → **Location-Based Services**
```python
def k_closest_points_to_origin(self, points: List[List[int]], k: int) -> List[List[int]]:
```
**Real Use Cases**:
1. **Ride-sharing apps**: Find K nearest drivers to passenger
2. **Food delivery**: K closest restaurants to customer
3. **Gaming**: K nearest players for matchmaking

**Production Example - Uber/Lyft Driver Matching**:
```python
class RideShareMatcher:
    def __init__(self):
        self.available_drivers = {}  # driver_id -> (lat, lon)
    
    def find_closest_drivers(self, passenger_lat: float, passenger_lon: float, k: int):
        heap = []  # Max heap of distances (negative for max heap)
        
        for driver_id, (lat, lon) in self.available_drivers.items():
            distance = calculate_distance(passenger_lat, passenger_lon, lat, lon)
            
            if len(heap) < k:
                heapq.heappush(heap, (-distance, driver_id, lat, lon))
            elif distance < -heap[0][0]:  # Closer than farthest in heap
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, driver_id, lat, lon))
        
        return [(driver_id, lat, lon) for _, driver_id, lat, lon in heap]
```

### **Advanced Level - Complex Systems**

#### **Sliding Window Maximum** → **Time-Series Analytics**
```python
def sliding_window_maximum(self, nums: List[int], k: int) -> List[int]:
```
**Real Use Cases**:
1. **Stock trading**: Maximum price in sliding time windows for technical analysis
2. **System monitoring**: Peak CPU/memory usage in rolling time windows
3. **Gaming**: Player performance peaks over recent matches

**Production Example - Trading System**:
```python
class TechnicalIndicator:
    def __init__(self, window_size_minutes=60):
        self.window_size = window_size_minutes
        self.price_data = deque()  # (timestamp, price)
        self.max_heap = []  # For sliding window maximum
    
    def add_price_tick(self, timestamp: int, price: float):
        # Remove old data outside window
        cutoff_time = timestamp - (self.window_size * 60)  # Convert to seconds
        while self.price_data and self.price_data[0][0] < cutoff_time:
            self.price_data.popleft()
        
        self.price_data.append((timestamp, price))
        
        # Update max heap with lazy deletion approach
        heapq.heappush(self.max_heap, (-price, timestamp))  # Negative for max heap
        
    def get_window_high(self) -> float:
        # Clean up old entries from heap
        cutoff_time = time.time() - (self.window_size * 60)
        while self.max_heap and self.max_heap[0][1] < cutoff_time:
            heapq.heappop(self.max_heap)
        
        return -self.max_heap[0][0] if self.max_heap else 0.0
```

#### **Median from Data Stream** → **Real-Time Statistics**
```python
def find_median_from_data_stream(self) -> 'MedianFinder':
```
**Real Use Cases**:
1. **Performance monitoring**: Real-time median response time calculation
2. **Financial systems**: Running median of transaction amounts for fraud detection
3. **Gaming**: Median player skill rating updates

**Production Example - API Response Time Monitoring**:
```python
class ResponseTimeMonitor:
    def __init__(self):
        self.small_half = []  # Max heap (use negative values)
        self.large_half = []  # Min heap
    
    def record_response_time(self, milliseconds: int):
        # Add to appropriate heap
        if not self.small_half or milliseconds <= -self.small_half[0]:
            heapq.heappush(self.small_half, -milliseconds)
        else:
            heapq.heappush(self.large_half, milliseconds)
        
        # Rebalance heaps
        if len(self.small_half) > len(self.large_half) + 1:
            value = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, value)
        elif len(self.large_half) > len(self.small_half) + 1:
            value = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -value)
    
    def get_median_response_time(self) -> float:
        if len(self.small_half) == len(self.large_half):
            return (-self.small_half[0] + self.large_half[0]) / 2.0
        elif len(self.small_half) > len(self.large_half):
            return float(-self.small_half[0])
        else:
            return float(self.large_half[0])
```

## Key Heap Patterns in Production

### **Pattern 1: Top-K Problems**
- **When**: Need best/worst K items from large dataset
- **Examples**: Leaderboards, recommendation systems, anomaly detection
- **Heap Choice**: Min heap of size K for "largest K", max heap of size K for "smallest K"

### **Pattern 2: Merge Multiple Sorted Streams**  
- **When**: Combining data from multiple sorted sources
- **Examples**: Database merge joins, log aggregation, time series data fusion
- **Heap Choice**: Min heap tracking next item from each stream

### **Pattern 3: Scheduling with Priorities**
- **When**: Tasks have different priorities and constraints
- **Examples**: OS schedulers, job queues, resource allocation
- **Heap Choice**: Priority queue with custom comparators

### **Pattern 4: Streaming Statistics**
- **When**: Need to maintain statistics on unlimited data streams
- **Examples**: Median calculation, percentile tracking, rolling window stats  
- **Heap Choice**: Two heaps (median), bounded heaps (percentiles)

## Why Heaps Beat Alternatives

| Scenario | Naive Approach | Heap Approach | Performance Gain |
|----------|----------------|---------------|------------------|
| Top K from stream | Sort entire array each time | Maintain heap of size K | O(n log n) → O(log k) |
| Merge K sorted lists | Concatenate + sort | Heap of K elements | O(n log n) → O(n log k) |
| Running median | Sort array each insertion | Two heaps | O(n log n) → O(log n) |
| Task scheduling | Linear search for highest priority | Priority heap | O(n) → O(log n) |

The key insight: **heaps excel when you need to repeatedly find extremes (min/max) in dynamic data**. If you're building systems that need "best", "worst", "most important", or "least important" decisions repeatedly, heaps are usually the right tool.

## Implementation Tips for Production

1. **Use `heapq` for simple cases**: Python's built-in module is well-optimized
2. **Custom comparisons**: Use tuples for multiple criteria: `(priority, timestamp, data)`  
3. **Memory management**: For bounded heaps, eject old items to prevent memory leaks
4. **Thread safety**: Wrap heap operations in locks for concurrent access
5. **Lazy deletion**: Mark items as deleted rather than removing immediately when needed for performance

## Next Steps

After mastering heaps, you'll naturally encounter these related patterns:
- **Graph algorithms** (shortest path with priority queues)
- **Dynamic programming** (optimization problems with heap-based state management)
- **System design** (load balancing, caching strategies, distributed systems)

The heap patterns you learn here directly apply to building scalable, efficient production systems.

---

*Next guide: Graph Algorithms - from navigation systems to social networks*