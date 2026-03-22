# Bellman-Ford Algorithm (with Negative-Cycle Detection)

## Why Bellman-Ford matters

Bellman-Ford computes shortest paths from a single source in a weighted graph, including graphs with negative edge weights.  
It is also one of the standard algorithms that can detect whether a reachable negative-weight cycle exists.

For interview prep and production reasoning, this is the key complement to Dijkstra.

## Core idea

Given `V` vertices and directed weighted edges:

1. Initialize:
   - `dist[source] = 0`
   - all other distances = infinity
2. Relax every edge `V - 1` times:
   - if `dist[u] + w < dist[v]`, update `dist[v]`
3. Perform one extra full pass over edges:
   - if any distance can still be improved, a reachable negative cycle exists

## Complexity

- Time: `O(V * E)`
- Space: `O(V)` (distance + predecessor arrays)

### Practical optimization
If a full relaxation pass makes no updates, terminate early (common optimization in real code).

## Bellman-Ford vs Dijkstra

- **Use Dijkstra** when all edge weights are non-negative and speed is critical.
- **Use Bellman-Ford** when negative edges are possible or negative-cycle detection is required.

A good engineering signal is choosing based on constraints, not defaulting blindly to one algorithm.

## ML / MLOps relevance

Bellman-Ford appears in systems where weighted transitions can include penalties and credits:

- Cost propagation over dependency graphs
- Routing/scoring pipelines with adjustments that may be negative
- Sanity checks for pathological feedback loops (negative cycles)

This maps well to large-scale, reliability-focused engineering environments.

## What this folder contains

- `bellman_ford.py`
  - Typed Bellman-Ford implementation
  - Predecessor tracking
  - Reachable negative-cycle detection
  - Path reconstruction helper
  - Runnable examples with assertions