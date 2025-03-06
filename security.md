# SQLY Security & Access Control

## 📖 Introduction

SQLY provides robust security and access control mechanisms to manage user permissions, data privacy, and authentication.

---

## 🔑 Role-Based Access Control (RBAC)

SQLY allows assigning roles to users and restricting query execution based on permissions.

### ✅ Example 1: Grant Read-Only Access to Analysts

```yaml
security:
  grant:
    role: analyst
    privileges:
      - select
    on:
      - tables: [sales_data, customer_info]
```

This grants analysts read-only access to sales and customer data.

### ✅ Example 2: Restrict Write Access to Admins

```yaml
security:
  grant:
    role: admin
    privileges:
      - insert
      - update
      - delete
    on:
      - tables: [all]
```

This allows only admins to modify data.

---

## 🛡️ Row-Level Security (RLS)

SQLY supports row-level security to enforce fine-grained access control.

### ✅ Example 3: Restrict Access to User-Specific Data

```yaml
security:
  row_level_policy:
    table: orders
    filter:
      user_id: current_user()
```

This ensures users can only access their own orders.

---

## 🔐 Column-Level Security

Sensitive fields can be restricted at the column level.

### ✅ Example 4: Hide Sensitive Data from Non-Admin Users

```yaml
security:
  column_masking:
    table: customer_info
    columns:
      - credit_card_number:
          mask:
            role: non_admin
            type: partial
            format: "XXXX-XXXX-XXXX-####"
```

This masks credit card numbers for non-admin users.

---

## 🏦 Data Encryption

SQLY supports encryption at rest and in transit to protect sensitive information.

### ✅ Example 5: Encrypt Personal Data

```yaml
security:
  encryption:
    table: user_profiles
    columns: [email, phone_number]
    type: AES-256
```

This ensures that email and phone numbers are encrypted.

---

## 🛑 Query Auditing & Logging

SQLY logs queries to track access and detect suspicious activity.

### ✅ Example 6: Enable Query Auditing

```yaml
security:
  audit:
    enabled: true
    log_queries: true
    log_failed_attempts: true
```

This enables logging of all queries and failed authentication attempts.

---

## 📌 Summary

- RBAC controls user privileges.
- RLS enforces per-user access restrictions.
- Column masking protects sensitive fields.
- Encryption secures data at rest and in transit.
- Query auditing detects unauthorized access.
