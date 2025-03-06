# SQLY Subqueries

## 📖 Introduction

Subqueries in SQLY allow you to nest one query inside another, providing powerful ways to filter, aggregate, and retrieve data dynamically.

---

## 🔍 Using Subqueries in `where` Clauses

Subqueries can be used to filter results based on another query.

### ✅ Example 1: Fetch Customers Who Placed More Than 3 Orders

```yaml
query:
  select: [id, name, email]
  from: customers
  where:
    id:
      in:
        subquery:
          select: customer_id
          from: orders
          group_by: customer_id
          having:
            count: orders.id
            gt: 3
```

---

## 🔗 Using Subqueries in `select` Clauses

A subquery can be used inside the `select` statement to fetch additional computed values.

### ✅ Example 2: Fetch Customers with Their Last Order Date

```yaml
query:
  select:
    - id
    - name
    - email
    - last_order:
        subquery:
          select: max(order_date)
          from: orders
          where:
            customer_id: customers.id
  from: customers
```

---

## 📊 Using Subqueries in `from` Clauses

Subqueries can act as temporary tables within a query.

### ✅ Example 3: Find Top 5 Highest-Spending Customers

```yaml
query:
  select: [customer_id, total_spent]
  from:
    subquery:
      select: [customer_id, sum: total_price as total_spent]
      from: orders
      group_by: customer_id
  order_by: total_spent DESC
  limit: 5
```

---

## 📌 Summary

- Use subqueries in `where` to filter based on nested queries.
- Use subqueries in `select` to retrieve computed values.
- Use subqueries in `from` to create temporary result sets.
