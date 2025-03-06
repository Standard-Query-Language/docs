# SQLY Basics

## 📖 Introduction

SQLY (Standard Query Language) is a YAML-based query language designed for structured and semi-structured data. It is inspired by JQL, Kusto, and DQL while offering a human-readable syntax.

---

## 🛠 Basic Query Structure

A simple SQLY query consists of the following components:

- `select`: Specifies the fields to retrieve.
- `from`: Defines the data source.
- `where`: Filters the results.
- `order_by`: Sorts the results.
- `limit`: Limits the number of returned rows.

### ✅ Example 1: Fetch Active Users

```yaml
query:
  select: [id, name, email]
  from: users
  where:
    status: active
  order_by: name ASC
  limit: 50
```

### ✅ Example 2: Fetch Orders Above a Certain Price

```yaml
query:
  select: [order_id, customer, total_price]
  from: orders
  where:
    total_price:
      gt: 100
  order_by: total_price DESC
```

---

## 🔍 Filtering & Logical Operators

SQLY supports multiple conditions using logical operators:

| Operator | Description |
|----------|------------|
| `gt` | Greater than |
| `lt` | Less than |
| `gte` | Greater than or equal |
| `lte` | Less than or equal |
| `in` | Matches any value in a list |
| `not` | Negates a condition |

### ✅ Example 3: Fetch High-Value Orders from Specific Customers

```yaml
query:
  select: [order_id, customer, total_price]
  from: orders
  where:
    total_price:
      gte: 500
    customer:
      in: ["Alice", "Bob", "Charlie"]
```

### ✅ Example 4: Fetch Users Who Are Not Admins

```yaml
query:
  select: [id, name]
  from: users
  where:
    role:
      not: admin
```

---

## 📊 Aggregation & Grouping

SQLY allows aggregation functions with `group_by`.

### ✅ Example 5: Calculate Average Order Value per Customer

```yaml
query:
  select:
    - customer_id
    - avg: total_price
  from: orders
  group_by: customer_id
```

---

## 📌 Summary

- Use `select` to define fields.
- `from` specifies the data source.
- `where` applies filtering.
- Use `order_by` for sorting results.
- Apply `group_by` for aggregations.

Proceed to **[Advanced Features](advanced_features.md)** to explore more capabilities.
