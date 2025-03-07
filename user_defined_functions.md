# User-defined Functions (UDFs) in SQLY

## 📖 Introduction

SQLY supports user-defined functions (UDFs) to extend its capabilities by creating reusable logic for queries.

---

## 🔧 Defining a User-defined Function

Users can create custom functions with parameters and return types.

### ✅ Example 1: Define a Simple Function

```yaml
udf:
  name: calculate_tax
  parameters:
    - name: price
      type: float
    - name: tax_rate
      type: float
  return_type: float
  body: |
    return price * tax_rate
```

This defines a `calculate_tax` function to compute tax based on a given price and tax rate.

---

## 📌 Using UDFs in Queries

UDFs can be called in SQLY queries to process data dynamically.

### ✅ Example 2: Apply a UDF in a Query

```yaml
query:
  select: [product_id, calculate_tax(price, 0.07)]
  from: products
```

This applies the `calculate_tax` function to compute tax for each product dynamically.

---

## 🏗️ Advanced UDF Features

SQLY supports advanced UDF capabilities, including conditional logic and iteration.

### ✅ Example 3: UDF with Conditional Logic

```yaml
udf:
  name: discount_price
  parameters:
    - name: price
      type: float
  return_type: float
  body: |
    if price > 100:
      return price * 0.9
    else:
      return price
```

This function applies a discount for prices above 100.

---

## 🚀 Registering External Functions

SQLY allows integration with external libraries or APIs within UDFs.

### ✅ Example 4: Call an External API in a UDF

```yaml
udf:
  name: get_exchange_rate
  parameters:
    - name: currency
      type: string
  return_type: float
  external:
    type: REST
    endpoint: "https://api.exchangerate.com/latest"
    method: GET
    query_params:
      base: "USD"
      target: "currency"
```

This function fetches exchange rates from an external API.

---

## 📌 Summary

- Define UDFs with parameters and return types.
- Use UDFs dynamically in queries.
- Implement conditional logic within functions.
- Register external functions to call APIs or libraries.
