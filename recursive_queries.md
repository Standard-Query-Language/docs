# SQLY Recursive Queries

## 📖 Introduction

Recursive queries allow working with hierarchical or tree-structured data, such as organizational structures, category trees, or graph-like relationships.

SQLY supports recursion using **Common Table Expressions (CTEs)** with the `union_all` operator.

---

## 🔄 Recursive Query Syntax

Recursive queries consist of:

1. A **base case** (initial dataset)
2. A **recursive case** (query that references itself)
3. The `union_all` operator to combine results iteratively

### ✅ Example 1: Querying an Employee Hierarchy

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

This retrieves all employees recursively, starting from the top-level manager (`manager_id: null`).

---

## 🌲 Recursive Category Trees

Recursive queries are useful for retrieving hierarchical categories, such as product categories.

### ✅ Example 2: Fetching All Subcategories of a Given Category

```yaml
query:
  with:
    category_tree:
      select: [id, name, parent_category_id]
      from: categories
      where:
        parent_category_id: 5  # Fetch subcategories of category ID 5
      union_all:
        select: [c.id, c.name, c.parent_category_id]
        from: categories as c
        join: category_tree as ct
          on: c.parent_category_id = ct.id
  select: *
  from: category_tree
```

This retrieves all subcategories under the given category ID (5), expanding downwards recursively.

---

## 🔗 Recursive Graph Traversal

Recursive queries can also be used to traverse graph structures, such as finding connections between users in a social network.

### ✅ Example 3: Finding Friends of Friends

```yaml
query:
  with:
    friend_network:
      select: [user_id, friend_id]
      from: friendships
      where:
        user_id: 42  # Start from user 42
      union_all:
        select: [f.user_id, f.friend_id]
        from: friendships as f
        join: friend_network as fn
          on: f.user_id = fn.friend_id
  select: *
  from: friend_network
```

This query finds all friends (direct and indirect connections) of user ID 42.

---

## 📌 Summary

- Recursive queries use `union_all` to iterate over hierarchical data.
- They are useful for employee hierarchies, category trees, and graph traversal.
- Recursive joins allow expanding results dynamically.
