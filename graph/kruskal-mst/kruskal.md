# Kruskal's Minimum Spanning Tree (MST)

## What problem Kruskal solves

Given a weighted, undirected graph, Kruskal finds a set of edges that connects all vertices with minimum total cost and no cycles.

- If the graph is connected: result is a **Minimum Spanning Tree (MST)** with `V - 1` edges.
- If the graph is disconnected: result is a **Minimum Spanning Forest (MSF)**.

## Core idea

Kruskal is greedy:

1. Sort all edges by ascending weight.
2. Iterate edges from smallest to largest.
3. Add an edge only if it connects two different components (does not form a cycle).
4. Use Union-Find (Disjoint Set Union) to track components efficiently.

Why this works: by the cut property, the lightest edge crossing a valid cut is always safe to include.

## Complexity

Let `V = #vertices`, `E = #edges`.

- Sorting edges: `O(E log E)` (dominant cost)
- Union-Find operations: near `O(1)` amortized each (`O(alpha(V))`)
- Total: `O(E log E)`
- Space: `O(V + E)` (Union-Find + sorted edges)

## Kruskal vs Prim (quick tradeoff)

- **Kruskal**
- Great when edges are easy to sort globally
- Naturally handles disconnected graphs (produces MSF)
- Pairs well with Union-Find

- **Prim**
- Often preferred with adjacency lists + heap on dense-ish connected graphs
- Grows one tree from a start node

For interview and production discussions: mention both and choose based on graph representation and constraints.

## Practical relevance (ML / MLOps at scale)

MST/MSF-style thinking appears in:

- Cost-efficient network/backbone design
- Hierarchical clustering foundations (single-link style intuition)
- Reducing redundant connections while preserving connectivity
- Building sparse structures from large weighted graphs

This signals practical optimization mindset for ML/MLOps engineering roles.

## File in this folder

- `kruskal.py`
- Typed Kruskal implementation
- Internal Union-Find with path compression + union by rank
- Returns selected edges and total weight
- Includes connected/disconnected test-style examples