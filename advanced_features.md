# SQLY Advanced Features

## 📖 Introduction

This section covers advanced SQLY features, including complex filtering, sorting, joins, pagination, and more.

---

## 🔎 Complex Filtering with Logical Operators

SQLY supports combining multiple conditions using `and`, `or`, and `not`.

### ✅ Example 1: Fetch Users with Multiple Conditions

```yaml
query:
  select: [id, name, email]
  from: users
  where:
    and:
      - status: active
      - role: admin
      - last_login:
          gte: "2024-01-01"
```

### ✅ Example 2: Fetch Orders Matching Multiple Statuses

```yaml
query:
  select: [order_id, customer, total_price, status]
  from: orders
  where:
    or:
      - status: completed
      - status: shipped
```

---

## 📊 Sorting & Pagination

Sorting results and limiting the number of returned rows.

### ✅ Example 3: Sort Users by Last Login Date (Descending)

```yaml
query:
  select: [id, name, last_login]
  from: users
  order_by: last_login DESC
  limit: 20
```

### ✅ Example 4: Paginate Results (Second Page, 10 Results per Page)

```yaml
query:
  select: [id, name, created_at]
  from: users
  limit: 10
  offset: 10
```

---

## 🔗 Joining Tables

SQLY supports joining multiple tables.

### ✅ Example 5: Fetch Orders with Customer Names

```yaml
query:
  select: [orders.order_id, customers.name, orders.total_price]
  from: orders
  join:
    customers:
      on: orders.customer_id = customers.id
```

---

## 🔍 Searching with `like` and `full_text_search`

Perform searches based on text patterns.

### ✅ Example 6: Find Products Containing "Wireless"

```yaml
query:
  select: [id, name, description]
  from: products
  where:
    name:
      like: "%wireless%"
```

### ✅ Example 7: Full-Text Search on Articles

```yaml
query:
  select: [id, title, content]
  from: articles
  where:
    content:
      full_text_search: "machine learning"
```

---

## 📌 Summary

- Use `and`, `or`, `not` for complex filtering.
- `order_by` sorts results.
- `limit` and `offset` enable pagination.
- `join` allows querying across tables.
- `like` and `full_text_search` support text searches.
