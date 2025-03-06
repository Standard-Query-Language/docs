# SQLY Extensions

## 📖 Introduction

SQLY supports extensions that enable custom functions, data sources, and additional capabilities beyond the core query language.

---

## 🔌 Custom Functions

Users can define reusable functions to extend SQLY’s functionality.

### ✅ Example 1: Define a Custom Function

```yaml
extensions:
  functions:
    name: calculate_discount
    parameters: [price, discount_rate]
    return_type: float
    body: |
      return price * (1 - discount_rate)
```

This defines a `calculate_discount` function to compute discounted prices.

---

## 🗄️ Custom Data Sources

SQLY supports external data sources such as APIs, cloud storage, and third-party databases.

### ✅ Example 2: Connect to an External API

```yaml
extensions:
  data_sources:
    name: weather_api
    type: REST
    endpoint: "https://api.weather.com/v1"
    authentication: api_key
```

This configures SQLY to retrieve data from a weather API.

---

## ⚡ User-Defined Aggregations

Custom aggregations allow advanced computations over grouped data.

### ✅ Example 3: Define a Custom Aggregation

```yaml
extensions:
  aggregations:
    name: median
    input_type: float
    return_type: float
    implementation: |
      sort(values)
      return values[len(values) // 2]
```

This defines a `median` aggregation function.

---

## 🔄 Event-Driven Triggers

Triggers enable automatic actions when data changes.

### ✅ Example 4: Trigger an Action on Insert

```yaml
extensions:
  triggers:
    name: notify_new_order
    table: orders
    event: insert
    action: |
      send_email("admin@example.com", "New order received!")
```

This sends an email when a new order is inserted.

---

## 📌 Summary

- Custom functions extend SQLY’s processing power.
- External data sources enable integrations.
- User-defined aggregations allow advanced analytics.
- Triggers automate actions based on data changes.
