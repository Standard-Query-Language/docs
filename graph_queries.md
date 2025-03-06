# SQLY Graph Queries

## 📖 Introduction

Graph queries in SQLY enable working with networked data, such as social connections, recommendation systems, and hierarchical relationships.

---

## 🔗 Basic Graph Querying

SQLY allows traversing relationships between entities using `graph_traverse`.

### ✅ Example 1: Find Direct Connections Between Users

```yaml
query:
  select: [user_a, user_b]
  from: user_connections
  where:
    graph_traverse:
      start: 42
      depth: 1
```

This retrieves all users directly connected to user 42.

---

## 🔄 Multi-Hop Traversals

Graph traversal supports multi-hop queries to find indirect relationships.

### ✅ Example 2: Find Friends of Friends

```yaml
query:
  select: [user_a, user_b]
  from: user_connections
  where:
    graph_traverse:
      start: 42
      depth: 2
```

This finds all friends and their friends (up to two levels away).

---

## 🔍 Shortest Path Queries

SQLY can compute the shortest path between nodes in a graph.

### ✅ Example 3: Find the Shortest Path Between Two Users

```yaml
query:
  select: [user_a, user_b, path_length]
  from: user_connections
  where:
    shortest_path:
      start: 42
      end: 99
```

This retrieves the shortest connection path between users 42 and 99.

---

## 🎯 Weighted Graph Queries

Some relationships may have weights, such as distances or costs.

### ✅ Example 4: Find the Cheapest Delivery Route

```yaml
query:
  select: [source, destination, total_cost]
  from: delivery_routes
  where:
    shortest_path:
      start: "Warehouse A"
      end: "Customer B"
      weight: shipping_cost
```

This retrieves the most cost-effective delivery route.

---

## 🏛️ Community Detection

Graph analytics can group entities based on relationships.

### ✅ Example 5: Detect Social Communities

```yaml
query:
  select: [user_id, community_id]
  from: users
  where:
    community_detection:
      method: louvain
```

This clusters users into social communities using the Louvain method.

---

## 📌 Summary

- `graph_traverse` finds direct and multi-hop connections.
- `shortest_path` computes optimal routes between nodes.
- Weighted graphs allow cost-based queries.
- Community detection groups entities into clusters.
