# SQLY Performance Optimization

## 📖 Introduction

Optimizing SQLY queries ensures fast execution, efficient resource usage, and scalability. SQLY provides indexing, caching, parallel execution, and query profiling tools.

---

## ⚡ Indexing for Faster Queries

Indexes improve query performance by reducing lookup time.

### ✅ Example 1: Create an Index on a Frequently Queried Column

```yaml
performance:
  indexing:
    table: orders
    columns: [customer_id]
    type: btree
```

This creates a B-tree index on `customer_id` in the `orders` table for faster lookups.

### ✅ Example 2: Use a Full-Text Index for Faster Searches

```yaml
performance:
  indexing:
    table: articles
    columns: [content]
    type: full_text
```

This enables optimized full-text searches on the `content` column.

---

## 🗄️ Query Caching

SQLY caches query results to improve response time for repeated queries.

### ✅ Example 3: Enable Query Caching

```yaml
performance:
  caching:
    enabled: true
    expiration: 10m
```

This caches query results for 10 minutes to reduce redundant computation.

---

## 🚀 Parallel Query Execution

SQLY supports parallel execution for large datasets.

### ✅ Example 4: Enable Parallel Query Execution

```yaml
performance:
  parallel_execution:
    enabled: true
    max_threads: 8
```

This allows queries to run on up to 8 parallel threads for faster execution.

---

## 📊 Query Profiling

Profiling helps identify slow queries and optimize execution plans.

### ✅ Example 5: Profile a Query

```yaml
performance:
  profiling:
    query:
      select: [customer_id, total_spent]
      from: purchases
      where:
        total_spent: "> 1000"
```

This analyzes execution time and resource usage for the query.

---

## 📌 Summary

- Indexing speeds up lookups and searches.
- Query caching reduces repeated computation.
- Parallel execution improves performance on large datasets.
- Query profiling helps optimize slow queries.
