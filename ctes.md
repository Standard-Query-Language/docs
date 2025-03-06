# SQLY Common Table Expressions (CTEs)

## 📖 Introduction

Common Table Expressions (CTEs) provide a way to define temporary, reusable query structures within a single SQLY query. They improve readability and make complex queries more maintainable.

---

## 🔍 Defining a CTE

CTEs are defined using the `with` keyword, followed by a name and a subquery.

### ✅ Example 1: Using a CTE to Find High-Value Orders

```yaml
query:
  with:
    high_value_orders:
      select: [order_id, customer_id, total_price]
      from: orders
      where:
        total_price:
          gt: 1000
  select: *
  from: high_value_orders
```

---

## 🔗 Using Multiple CTEs

You can define multiple CTEs in a single query to modularize complex logic.

### ✅ Example 2: Using Two CTEs to Analyze Customer Spending

```yaml
query:
  with:
    customer_totals:
      select: [customer_id, sum: total_price as total_spent]
      from: orders
      group_by: customer_id
    top_customers:
      select: *
      from: customer_totals
      where:
        total_spent:
          gt: 5000
  select: *
  from: top_customers
```

---

## 🔁 Recursive CTEs

Recursive CTEs allow querying hierarchical data such as organizational structures or category trees.

### ✅ Example 3: Querying an Employee Hierarchy

```yaml
query:
  with:
    employee_hierarchy:
      select: [id, name, manager_id]
      from: employees
      where:
        manager_id: null
      union_all:
        select: [e.id, e.name, e.manager_id]
        from: employees as e
        join: employee_hierarchy as eh
          on: e.manager_id = eh.id
  select: *
  from: employee_hierarchy
```

---

## 📌 Summary

- CTEs allow defining temporary, reusable query structures.
- Multiple CTEs can be combined to simplify complex queries.
- Recursive CTEs enable hierarchical data processing.
