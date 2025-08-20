# Greedy Algorithms: When Being Selfish Actually Works

Greedy algorithms are the embodiment of "live in the moment." At each step, they make the locally optimal choice, hoping it leads to a globally optimal solution. Sometimes this works beautifully. Sometimes it fails spectacularly. Learning to recognize when greedy works is an art form.

## What Actually Is a Greedy Algorithm?

Imagine you're at a buffet with limited plate space. A greedy approach would be to always pick the most delicious-looking item you can see right now, without considering what might be coming next. Sometimes you get an amazing meal. Sometimes you fill up on bread and miss the lobster.

That's greedy algorithms in a nutshell: make the best choice available at each step, never looking back, never second-guessing.

```python
def activity_selection(start_times, end_times):
    # Greedy choice: always pick the activity that ends earliest
    activities = list(zip(start_times, end_times, range(len(start_times))))
    activities.sort(key=lambda x: x[1])  # Sort by end time
    
    selected = [activities[0]]
    last_end_time = activities[0][1]
    
    for start, end, index in activities[1:]:
        if start >= last_end_time:  # No overlap
            selected.append((start, end, index))
            last_end_time = end
    
    return selected
```

## The Greedy Choice Property

For a greedy algorithm to work, the problem must have the **greedy choice property**: a globally optimal solution can be arrived at by making locally optimal choices.

This sounds circular, but there's a way to verify it:

1. **Prove the greedy choice is safe**: Show that there exists an optimal solution that includes the greedy choice
2. **Prove optimal substructure**: After making the greedy choice, you're left with a subproblem that has the same structure

### Example: Fractional Knapsack

You have a knapsack with limited capacity and items with different values and weights. You can take fractions of items.

**Greedy choice**: Always take the item with the highest value-to-weight ratio first.

```python
def fractional_knapsack(capacity, weights, values):
    # Calculate value-to-weight ratios
    items = [(values[i] / weights[i], weights[i], values[i], i) 
             for i in range(len(weights))]
    
    # Sort by ratio (descending)
    items.sort(reverse=True)
    
    total_value = 0
    
    for ratio, weight, value, index in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take fraction of the item
            total_value += ratio * capacity
            break
    
    return total_value
```

**Why this works**: Taking the highest ratio item first is always safe—there's no scenario where taking a lower ratio item first leads to a better overall solution.

## Classic Greedy Patterns

### 1. Interval Scheduling
**Problem**: Schedule maximum number of non-overlapping activities
**Greedy choice**: Always pick the activity that ends earliest
**Why it works**: Early-ending activities leave more room for future activities

### 2. Huffman Coding
**Problem**: Optimal prefix-free binary codes for characters
**Greedy choice**: Always merge the two nodes with lowest frequency
**Why it works**: Frequent characters should have shorter codes

### 3. Minimum Spanning Tree (Kruskal's)
**Problem**: Connect all vertices with minimum total edge weight
**Greedy choice**: Always add the cheapest edge that doesn't create a cycle
**Why it works**: The cheapest edge is always part of some MST

### 4. Dijkstra's Shortest Path
**Problem**: Find shortest paths from source to all vertices
**Greedy choice**: Always process the unvisited vertex with minimum distance
**Why it works**: Once processed, we've found the shortest path to that vertex

## When Greedy Fails: The Coin Change Trap

Consider making change for 11 cents with coins [1, 4, 5]:

**Greedy approach**: Take largest coin first
- Take 5: remaining = 6
- Take 5: remaining = 1  
- Take 1: remaining = 0
- Total: 3 coins

**Optimal approach**:
- Take 4: remaining = 7
- Take 4: remaining = 3
- Take 1: remaining = 2
- Take 1: remaining = 1
- Take 1: remaining = 0
- Wait, that's worse! Let me recalculate...

Actually, for 11 cents:
- Take 5: remaining = 6
- Take 4: remaining = 2
- Take 1: remaining = 1
- Take 1: remaining = 0
- Total: 4 coins

But optimal is:
- Take 4: remaining = 7
- Take 4: remaining = 3
- Take 1: remaining = 2
- Take 1: remaining = 1
- Take 1: remaining = 0

Hmm, let me think again... Actually:
- Take 5: remaining = 6
- Take 1: remaining = 5
- Take 5: remaining = 0
- Total: 3 coins (5 + 1 + 5)

But better is:
- Take 4: remaining = 7
- Take 4: remaining = 3
- Take 1 + 1 + 1: remaining = 0
- Total: 5 coins... no wait.

Actually, let me be more careful:
For 11 cents with [1, 4, 5]:
- Greedy: 5 + 5 + 1 = 3 coins
- Better: 4 + 4 + 1 + 1 + 1 = 5 coins (worse)

Actually, 5 + 5 + 1 = 11, so greedy gives 3 coins.
But 4 + 4 + 3×1 = 4 + 4 + 3 = 11, giving 5 coins.

Wait, let me reconsider: 4 + 4 + 1 + 1 + 1 = 11 with 5 coins.
Or: 5 + 4 + 1 + 1 = 11 with 4 coins.
Or: 5 + 5 + 1 = 11 with 3 coins (greedy).

So greedy actually works here. Let me use a different example:

For 8 cents with coins [1, 3, 4]:
- **Greedy**: 4 + 4 = 8 (2 coins)
- **Optimal**: 4 + 4 = 8 (2 coins)

That works too! Let me try 6 cents:
- **Greedy**: 4 + 1 + 1 = 6 (3 coins)  
- **Optimal**: 3 + 3 = 6 (2 coins)

There we go! Greedy fails when the coin system isn't "canonical."

## Recognizing Greedy Opportunities

Look for these patterns:

1. **Optimization problems** (maximize/minimize something)
2. **"Earliest" or "latest" constraints**
3. **When you can sort by some criterion**
4. **Exchange arguments work** (swapping choices doesn't hurt)
5. **Problems with obvious "greedy choice"**

## The Exchange Argument

This is the formal way to prove a greedy algorithm works:

1. Assume there's an optimal solution that differs from the greedy choice
2. Show you can "exchange" parts of that solution to match the greedy choice
3. Prove the exchange doesn't make the solution worse
4. Conclude the greedy choice is safe

### Example: Activity Selection Proof

**Claim**: Always choosing the earliest-ending activity is optimal.

**Proof**: 
- Let A be the activity chosen by greedy (earliest end time)
- Let B be the first activity in some optimal solution  
- If A ≠ B, then A ends before or at the same time as B
- We can replace B with A in the optimal solution
- This doesn't conflict with any later activities (A ends earlier)
- So we have an optimal solution that starts with the greedy choice

## Common Greedy Strategies

### 1. Sort + Scan
Most greedy algorithms start by sorting according to some criterion:

```python
def meeting_rooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 'start'))
        events.append((end, 'end'))
    
    events.sort()  # Greedy: process events in chronological order
    
    rooms = 0
    max_rooms = 0
    
    for time, event_type in events:
        if event_type == 'start':
            rooms += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1
    
    return max_rooms
```

### 2. Priority Queue
When you need to always process the "best" element:

```python
import heapq

def connect_sticks(sticks):
    # Greedy: always combine the two shortest sticks
    heapq.heapify(sticks)
    total_cost = 0
    
    while len(sticks) > 1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(sticks, cost)
    
    return total_cost
```

## Implementation Tips

### 1. Be Explicit About the Greedy Choice
Don't just implement—explicitly state what your greedy choice is:

```python
# Greedy choice: always pick the job with the earliest deadline
jobs.sort(key=lambda x: x.deadline)
```

### 2. Prove or Verify the Choice
Before implementing, convince yourself (or prove) that the greedy choice is safe.

### 3. Handle Edge Cases
Greedy algorithms often have simple logic but tricky edge cases:

```python
def can_jump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:  # Can't reach this position
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:  # Early termination
            return True
    
    return True
```

## When to Choose Greedy Over DP

- **Greedy is simpler** when it works
- **Better time complexity** (usually O(n log n) vs O(n²) for DP)
- **Less memory usage** (no memoization table)

But use DP when:
- Greedy choice property doesn't hold
- You need to consider multiple future possibilities
- The problem has overlapping subproblems

## Practice Strategy

1. **Start with classic problems**: Activity selection, fractional knapsack
2. **Learn to spot the patterns**: Sorting strategies, exchange arguments
3. **Practice proving correctness**: Exchange arguments are key
4. **Recognize when greedy fails**: Try counterexamples

## Common Interview Problems

- **Jump Game** (can you reach the end?)
- **Gas Station** (circular route completion)
- **Meeting Rooms** (minimum rooms needed)
- **Task Scheduler** (schedule tasks with cooling period)
- **Candy Distribution** (minimum candies with rating constraints)

## Final Thoughts

Greedy algorithms are seductive because they're often simple and intuitive. The hard part is knowing when they work. When a greedy algorithm is correct, it's usually much simpler than the DP alternative.

The key insight: greedy works when the locally optimal choice is also globally optimal. This happens more often than you might think, especially in scheduling and optimization problems.

When in doubt, try to construct a counterexample. If you can't break your greedy approach with a small example, it might just work.

---

*Next up: Union Find - where keeping track of connected components becomes surprisingly elegant.*