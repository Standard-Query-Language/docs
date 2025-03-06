# SQLY Window Functions

## 📖 Introduction

Window functions allow for calculations across a subset of rows related to the current row. Unlike standard aggregation, they do not collapse the result set but instead provide analytical insights like ranking, running totals, and moving averages.

---

## 🔍 Basic Window Function Syntax

A window function uses `over`, which defines a partitioning and ordering context for the function.

### ✅ Example 1: Rank Customers by Total Spend

```yaml
query:
  select:
    - customer_id
    - total_spent
    - rank:
        function: rank
        over:
          partition_by: null
          order_by: total_spent DESC
  from:
    subquery:
      select: [customer_id, sum: total_price as total_spent]
      from: orders
      group_by: customer_id
```

---

## 🔢 Ranking Functions

SQLY supports ranking functions such as:

- `rank` - Assigns a unique rank, with gaps for ties.
- `dense_rank` - Assigns ranks without gaps.
- `row_number` - Assigns a unique sequential row number.

### ✅ Example 2: Assign Row Numbers to Orders per Customer

```yaml
query:
  select:
    - order_id
    - customer_id
    - order_date
    - row_num:
        function: row_number
        over:
          partition_by: customer_id
          order_by: order_date DESC
  from: orders
```

---

## 🔄 Running Totals & Moving Averages

Window functions can calculate cumulative values over a partitioned set.

### ✅ Example 3: Calculate Running Total of Sales per Customer

```yaml
query:
  select:
    - order_id
    - customer_id
    - order_date
    - total_price
    - running_total:
        function: sum
        over:
          partition_by: customer_id
          order_by: order_date ASC
          rows: unbounded preceding
  from: orders
```

### ✅ Example 4: Calculate a 3-Period Moving Average of Sales

```yaml
query:
  select:
    - order_id
    - customer_id
    - order_date
    - total_price
    - moving_avg:
        function: avg
        over:
          partition_by: customer_id
          order_by: order_date ASC
          rows: 2 preceding
  from: orders
```

---

## 📌 Summary

- Window functions operate over a partitioned subset of data.
- Use `rank`, `dense_rank`, and `row_number` for ordering analysis.
- `sum` and `avg` can compute running totals and moving averages.
