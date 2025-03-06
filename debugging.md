# SQLY Advanced Debugging

## 📖 Introduction

Debugging SQLY queries ensures correctness, performance, and reliability. SQLY provides query logging, execution tracing, error handling, and optimization insights.

---

## 📜 Query Logging

Logging SQLY queries helps track execution history and identify issues.

### ✅ Example 1: Enable Query Logging

```yaml
debugging:
  logging:
    enabled: true
    log_level: detailed
    output: /var/log/sqly_queries.log
```

This enables detailed query logging to a specified file.

---

## 🔍 Execution Tracing

Tracing provides insights into how queries are processed internally.

### ✅ Example 2: Trace Query Execution

```yaml
debugging:
  tracing:
    enabled: true
    query:
      select: [order_id, total]
      from: orders
      where:
        total: "> 500"
```

This traces execution steps for a specific query.

---

## 🚨 Error Handling

SQLY captures and reports errors to assist debugging.

### ✅ Example 3: Enable Error Logging

```yaml
debugging:
  error_handling:
    log_errors: true
    capture_stack_trace: true
    output: /var/log/sqly_errors.log
```

This logs errors along with stack traces for debugging.

---

## 📊 Query Execution Plan Analysis

SQLY provides execution plans to optimize queries.

### ✅ Example 4: Analyze Query Execution Plan

```yaml
debugging:
  execution_plan:
    query:
      select: [product_id, sales]
      from: sales_data
      where:
        sales: "> 1000"
```

This retrieves the execution plan for a query, highlighting optimization opportunities.

---

## 📌 Summary

- Query logging tracks execution history.
- Execution tracing provides query insights.
- Error handling captures and logs errors.
- Execution plan analysis helps optimize queries.
