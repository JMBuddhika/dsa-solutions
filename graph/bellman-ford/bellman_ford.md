# Bellman-Ford: Practical Notes and Edge Cases

## What this implementation is for

Bellman-Ford solves single-source shortest paths on weighted directed graphs, including graphs with negative edge weights.
It is the correct baseline when edge weights are not guaranteed to be non-negative and when negative-cycle detection is required.

## When to choose Bellman-Ford vs Dijkstra

- **Use Dijkstra** for non-negative weights and better asymptotic performance.
- **Use Bellman-Ford** when:
- negative weights may appear,
- correctness under those weights matters,
- you need to detect reachable negative cycles.

In design interviews, explaining this decision boundary clearly is often more important than memorizing formulas.

## Key implementation details

1. Initialize:
- `dist[source] = 0`
- all other distances = `inf`
2. Relax all edges up to `V - 1` times.
3. Early-stop if one full pass makes no updates.
4. Run one extra pass:
- if an edge can still relax, a negative cycle is reachable from source.

## Reachability nuance (important)

Bellman-Ford should report only **reachable** negative cycles from the chosen source.
A negative cycle in a disconnected component must not affect the source's shortest-path result.

## Complexity

- Time: `O(V * E)`
- Space: `O(V)` for distance + predecessor arrays

## Common pitfalls

- Forgetting edge endpoint validation (`u`, `v` range checks)
- Treating unreachable nodes as having valid paths
- Reporting any negative cycle globally instead of reachable-only cycles
- Not documenting whether graph is directed (this implementation is directed)

## Portfolio framing (ML Engineer / MLOps)

This topic maps to production-grade graph reasoning:

- weighted dependency/cost propagation
- robust path logic under non-ideal data
- anomaly signaling via cycle detection
- explicit edge-case handling and test discipline

Those are practical signals for reliability-focused teams like Grab and Stripe.
