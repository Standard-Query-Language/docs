# JSON & Arrays in SQLY

## 📖 Introduction

SQLY provides powerful support for querying and manipulating JSON data and array structures, enabling efficient handling of semi-structured data.

---

## 📦 Querying JSON Fields

SQLY allows extracting and filtering data from JSON objects.

### ✅ Example 1: Extract a JSON Field

```yaml
json_query:
  select: [customer_id, profile.name]
  from: customers
  where:
    profile.age: "> 30"
```

This extracts the `name` field from the `profile` JSON object and filters customers older than 30.

### ✅ Example 2: Filter by a JSON Array Value

```yaml
json_query:
  select: [order_id, items]
  from: orders
  where:
    items[*].category: "electronics"
```

This retrieves orders containing items in the `electronics` category.

---

## 📑 Modifying JSON Data

SQLY enables updates and modifications within JSON structures.

### ✅ Example 3: Update a JSON Field

```yaml
json_modify:
  update: customers
  set:
    profile.status: "VIP"
  where:
    customer_id: 123
```

This updates the `status` field inside the `profile` JSON object.

---

## 📂 Working with Arrays

Arrays are supported for querying and filtering within SQLY.

### ✅ Example 4: Check If a Value Exists in an Array

```yaml
array_query:
  select: [user_id, roles]
  from: users
  where:
    roles: contains("admin")
```

This retrieves users who have `admin` in their `roles` array.

### ✅ Example 5: Unnest an Array

```yaml
array_query:
  select: [user_id, unnest(permissions)]
  from: users
```

This expands the `permissions` array into individual rows.

---

## 📌 Summary

- Query JSON fields using dot notation.
- Filter JSON arrays with wildcard `[*]`.
- Modify JSON data using structured updates.
- Work with arrays using `contains()` and `unnest()`.
