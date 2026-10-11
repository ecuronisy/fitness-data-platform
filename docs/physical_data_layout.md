# Physical Data Layout

## Purpose

This document defines the physical organization of datasets within the Fitness Data Platform.

The layout is designed to simulate a modern Lakehouse architecture while running entirely on a local machine.

The structure follows the Medallion Architecture documented in the Lakehouse Architecture specification.

---

# Root Data Directory

```text
data/
```

All datasets used by the platform are stored inside this directory.

---

# Catalog Structure

The platform uses a single logical catalog:

```text
fitness_catalog
```

Complete path:

```text
data/fitness_catalog/
```

---

# Schema Structure

The catalog is divided into three logical schemas:

```text
bronze
silver
gold
```

Full layout:

```text
data/
└── fitness_catalog/
    ├── bronze/
    ├── silver/
    └── gold/
```

---

# Bronze Schema

## Purpose

Store raw source data exactly as received from external systems.

## Path

```text
data/fitness_catalog/bronze/
```

## Datasets

### strava_activities

Raw activity snapshots downloaded from the Strava API.

Path:

```text
data/fitness_catalog/bronze/strava_activities/
```

Example files:

```text
strava_activities_20261011.json
strava_activities_20261018.json
```

---

### google_tasks

Raw task snapshots downloaded from Google Tasks.

Path:

```text
data/fitness_catalog/bronze/google_tasks/
```

Example files:

```text
google_tasks_20261011.json
google_tasks_20261018.json
```

---

# Silver Schema

## Purpose

Store validated and standardized business entities.

## Path

```text
data/fitness_catalog/silver/
```

## Datasets

### activities

Standardized cardio activities.

Path:

```text
data/fitness_catalog/silver/activities/
```

Example files:

```text
activities.parquet
```

---

### exercises

Standardized strength exercises.

Path:

```text
data/fitness_catalog/silver/exercises/
```

Example files:

```text
exercises.parquet
```

---

# Gold Schema

## Purpose

Store analytics-ready datasets.

## Path

```text
data/fitness_catalog/gold/
```

## Datasets

### weekly_summary

Path:

```text
data/fitness_catalog/gold/weekly_summary/
```

Files:

```text
weekly_summary.parquet
```

---

### monthly_summary

Path:

```text
data/fitness_catalog/gold/monthly_summary/
```

Files:

```text
monthly_summary.parquet
```

---

### personal_records

Path:

```text
data/fitness_catalog/gold/personal_records/
```

Files:

```text
personal_records.parquet
```

---

### training_score

Path:

```text
data/fitness_catalog/gold/training_score/
```

Files:

```text
training_score.parquet
```

---

# Complete Layout

```text
fitness-data-platform/
│
├── data/
│   └── fitness_catalog/
│       │
│       ├── bronze/
│       │   ├── strava_activities/
│       │   └── google_tasks/
│       │
│       ├── silver/
│       │   ├── activities/
│       │   └── exercises/
│       │
│       └── gold/
│           ├── weekly_summary/
│           ├── monthly_summary/
│           ├── personal_records/
│           └── training_score/
│
├── docs/
├── src/
├── tests/
├── notebooks/
└── config/
```

---

# Dataset Naming Standard

Bronze:

```text
source_entity
```

Examples:

```text
strava_activities
google_tasks
```

Silver:

```text
business_entity
```

Examples:

```text
activities
exercises
```

Gold:

```text
business_metric
```

Examples:

```text
weekly_summary
monthly_summary
personal_records
training_score
```

---

# Future Evolution

Future datasets should be added inside the appropriate schema while preserving the existing naming conventions.

Additional schemas are not planned for Version 1.

---

# Approved Physical Layout

Status: Approved

Version: 1.0