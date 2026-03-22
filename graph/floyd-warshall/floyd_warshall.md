# Floyd-Warshall: All-Pairs Shortest Paths

## What problem it solves

Floyd-Warshall computes shortest-path distances between **every pair of vertices** in a weighted directed graph.
It supports negative edge weights and can detect negative cycles via the distance matrix diagonal.

This is a dynamic-programming algorithm and is often the cleanest baseline for dense graphs or when many source-target queries are needed.

## DP recurrence

Let `dist[i][j]` be the shortest known distance from `i` to `j`.

For each intermediate vertex `k`:

`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

Interpretation: for each `(i, j)`, decide whether routing through `k` improves cost.

## Initialization

- `dist[i][i] = 0` for all `i`
- `dist[u][v] = weight(u, v)` for each edge
- otherwise `dist[i][j] = inf`
- for path reconstruction, maintain `next_hop[i][j]`

If multiple edges exist between the same pair, keep the smallest weight.

## Negative-cycle detection

After running the algorithm, if any diagonal entry is negative (`dist[v][v] < 0`), a negative cycle is present (reachable from `v`).

When negative cycles exist, shortest-path values affected by the cycle are not well-defined.

## Complexity

- Time: `O(V^3)`
- Space: `O(V^2)`

### When to use it

Choose Floyd-Warshall when:

- graph is relatively small/medium but query volume is high (all-pairs needed),
- graph is dense,
- implementation simplicity and completeness are priorities.

Prefer repeated Dijkstra/Bellman-Ford when:

- graph is very sparse and all-pairs is not required,
- only one/few source nodes matter.

## ML / MLOps relevance (Grab-style systems)

All-pairs cost matrices are useful for:

- global routing/latency analysis between services or regions
- precomputing pairwise transfer costs in scheduling pipelines
- evaluating topology-wide impact of cost updates

This demonstrates system-level graph reasoning beyond single-source shortest paths.