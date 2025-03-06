# SQLY Geospatial Queries

## 📖 Introduction

Geospatial queries enable querying, filtering, and analyzing location-based data. SQLY supports operations for points, polygons, distances, and spatial joins.

---

## 📍 Filtering by Location

You can filter records based on geographic coordinates.

### ✅ Example 1: Find Stores in a Specific City

```yaml
query:
  select: [id, name, location]
  from: stores
  where:
    city: "San Francisco"
```

This retrieves all stores located in San Francisco.

---

## 📏 Distance-Based Queries

You can find locations within a certain radius of a given point.

### ✅ Example 2: Find Restaurants Within 10 km of a User's Location

```yaml
query:
  select: [id, name, location]
  from: restaurants
  where:
    location:
      within_distance:
        point: [37.7749, -122.4194]
        distance: 10km
```

This retrieves all restaurants within 10 km of the given latitude/longitude (San Francisco coordinates).

---

## 🌍 Bounding Box Queries

Find records within a rectangular region.

### ✅ Example 3: Find Parks Within a Defined Area

```yaml
query:
  select: [id, name, location]
  from: parks
  where:
    location:
      within_bbox:
        min: [37.70, -122.50]
        max: [37.80, -122.40]
```

This retrieves all parks within the defined latitude/longitude boundaries.

---

## 🗺️ Spatial Joins

Geospatial joins allow comparing locations between datasets.

### ✅ Example 4: Find Customers Near a Store

```yaml
query:
  select: [customers.id, customers.name]
  from: customers
  join: stores
    on:
      customers.location:
        within_distance:
          point: stores.location
          distance: 5km
```

This retrieves customers located within 5 km of any store.

---

## 📌 Summary

- Use `within_distance` for radius-based queries.
- Use `within_bbox` to filter by rectangular regions.
- Spatial joins enable location-based comparisons.
