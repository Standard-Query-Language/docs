# SQLY Full-Text Search

## 📖 Introduction

Full-text search (FTS) enables powerful searching capabilities over large text fields. SQLY supports FTS with advanced matching techniques, ranking, and filtering.

---

## 🔍 Basic Full-Text Search

The `full_text_search` operator searches for keywords within text fields.

### ✅ Example 1: Search for Articles Containing "Machine Learning"

```yaml
query:
  select: [id, title, content]
  from: articles
  where:
    content:
      full_text_search: "machine learning"
```

This query retrieves all articles that mention "machine learning" anywhere in the content.

---

## 🔠 Phrase and Proximity Search

FTS allows searching for exact phrases and nearby words.

### ✅ Example 2: Exact Phrase Match

```yaml
query:
  select: [id, title]
  from: articles
  where:
    content:
      full_text_search:
        phrase: "deep neural networks"
```

This ensures that "deep neural networks" appears exactly as typed.

### ✅ Example 3: Words Within Close Proximity

```yaml
query:
  select: [id, title]
  from: articles
  where:
    content:
      full_text_search:
        near:
          words: ["AI", "ethics"]
          distance: 5
```

This finds instances where "AI" and "ethics" appear within 5 words of each other.

---

## 🔝 Ranking and Relevance

SQLY supports ranking results based on relevance.

### ✅ Example 4: Rank Articles by Relevance to "Cybersecurity"

```yaml
query:
  select: [id, title, rank]
  from: articles
  where:
    content:
      full_text_search: "cybersecurity"
  order_by: rank DESC
```

This ranks articles based on how relevant they are to "cybersecurity."

---

## 📂 Searching Multiple Fields

FTS can search across multiple text fields simultaneously.

### ✅ Example 5: Search Across Title and Content

```yaml
query:
  select: [id, title]
  from: articles
  where:
    or:
      - title:
          full_text_search: "quantum computing"
      - content:
          full_text_search: "quantum computing"
```

This searches for "quantum computing" in both the title and content fields.

---

## 📌 Summary

- `full_text_search` enables keyword-based search.
- Use `phrase` for exact matches and `near` for proximity searches.
- `rank` orders results based on relevance.
- Multi-field search expands search scope.
