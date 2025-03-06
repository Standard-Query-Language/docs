# SQLY Machine Learning Queries

## 📖 Introduction

Machine Learning (ML) queries in SQLY allow users to apply predictive models, classify data, and generate insights directly within queries.

---

## 🔍 Applying Pre-Trained Models

SQLY allows integrating pre-trained ML models for predictions.

### ✅ Example 1: Predict Customer Churn

```yaml
query:
  select: [customer_id, name, churn_probability]
  from: customers
  where:
    churn_probability:
      predict:
        model: customer_churn_model
```

This retrieves customer churn probabilities using a pre-trained model.

---

## 📊 Classifying Data

ML models can classify records into predefined categories.

### ✅ Example 2: Categorize Support Tickets

```yaml
query:
  select: [ticket_id, description, category]
  from: support_tickets
  where:
    category:
      predict:
        model: ticket_classifier
```

This assigns categories to support tickets using an ML classifier.

---

## 📈 Forecasting Trends

SQLY supports time-series forecasting for predictive analytics.

### ✅ Example 3: Forecast Future Sales

```yaml
query:
  select: [date, predicted_sales]
  from:
    forecast:
      model: sales_forecast_model
      input:
        past_sales:
          select: [date, total_sales]
          from: sales
```

This predicts future sales based on historical sales data.

---

## 🤖 Anomaly Detection

ML models can detect outliers and unusual patterns.

### ✅ Example 4: Detect Fraudulent Transactions

```yaml
query:
  select: [transaction_id, amount, is_fraud]
  from: transactions
  where:
    is_fraud:
      predict:
        model: fraud_detection_model
```

This flags potentially fraudulent transactions.

---

## 📌 Summary

- `predict` applies ML models to classify and analyze data.
- Forecasting models enable trend prediction.
- Anomaly detection helps identify irregularities.
