# Topological Sort (Kahn's Algorithm)

## What problem it solves

Topological sorting returns a valid linear ordering of nodes in a **Directed Acyclic Graph (DAG)** such that every directed edge `u -> v` places `u` before `v`.

If a directed graph contains a cycle, no valid topological ordering exists.

---

## Core idea (Kahn's Algorithm)

1. Compute in-degree of every node.
2. Push all nodes with in-degree `0` into a queue.
3. Repeatedly:
- pop one node from queue,
- append it to output order,
- decrement in-degree of its outgoing neighbors,
- enqueue neighbors whose in-degree becomes `0`.
4. If output length is less than number of nodes, a cycle exists.

This is a BFS-like process over dependency layers.

---

## Complexity

Let `V` = number of nodes, `E` = number of edges.

- **Time:** `O(V + E)`
- **Space:** `O(V + E)` for adjacency list, in-degree array, and queue

---

## Why this matters in distributed systems

Topological sorting is directly useful for dependency scheduling:

- workflow orchestration (Airflow/Dagster-style DAG runs)
- ETL/feature pipeline stage ordering
- microservice rollout sequences with dependency constraints
- build/deploy graph execution plans

For ML Engineer / MLOps roles, this maps to practical job scheduling reliability: execute prerequisites first, detect impossible dependency graphs early.

---

## Practical notes

- Multiple valid topological orders may exist.
- Queue choice affects which valid order you get (e.g., deterministic ordering with min-heap).
- Cycle detection via processed-node count is simple and reliable.
- Validate node IDs and edge bounds in production code paths.

---

## Example

Edges:
- `0 -> 1`
- `0 -> 2`
- `1 -> 3`
- `2 -> 3`

Valid topological orders include:
- `[0, 1, 2, 3]`
- `[0, 2, 1, 3]`

Both respect all dependencies.