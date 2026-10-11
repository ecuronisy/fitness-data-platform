# Lakehouse Architecture

## Purpose

This document defines the Medallion Architecture used by the Fitness Data Platform.

The platform adopts a Bronze, Silver, and Gold layered approach to organize data processing and analytics.

This design improves maintainability, scalability, traceability, and data quality while following modern Data Engineering best practices.

---

# Architecture Overview

```text
                +----------------+
                | Data Sources   |
                +----------------+
                         |
                         ▼
                +----------------+
                | Bronze Layer   |
                | Raw Data       |
                +----------------+
                         |
                         ▼
                +----------------+
                | Silver Layer   |
                | Cleansed Data  |
                +----------------+
                         |
                         ▼
                +----------------+
                | Gold Layer     |
                | Analytics Data |
                +----------------+
```

---

# Bronze Layer

## Purpose

The Bronze layer stores raw data exactly as received from source systems.

No business transformations are applied.

The objective is to preserve the original source data for:

- Auditing
- Troubleshooting
- Replayability
- Historical snapshots

---

## Data Sources

### Strava

```text
bronze/strava_activities/
```

### Google Tasks

```text
bronze/google_tasks/
```

---

## Storage Format

```text
JSON
```

---

## Rules

- Keep source data unchanged
- Preserve original API payloads
- Allow multiple snapshots over time
- Never overwrite historical data

---

# Silver Layer

## Purpose

The Silver layer contains cleansed, validated, and standardized datasets.

This layer transforms source-specific structures into common business entities.

---

## Datasets

### activities

Cardio activities standardized from Strava.

```text
silver/activities/
```

---

### exercises

Strength exercise records standardized from Google Tasks.

```text
silver/exercises/
```

---

## Storage Format

```text
Parquet
```

---

## Data Quality Rules

Examples:

- Remove duplicate records
- Validate mandatory fields
- Standardize column names
- Normalize data types

---

# Gold Layer

## Purpose

The Gold layer contains business-ready and analytics-ready datasets.

These datasets are optimized for reporting and performance analysis.

---

## Datasets

### weekly_summary

Weekly training aggregation.

```text
gold/weekly_summary/
```

---

### monthly_summary

Monthly training aggregation.

```text
gold/monthly_summary/
```

---

### personal_records

Personal achievements and milestones.

```text
gold/personal_records/
```

---

### training_score

Training intensity and activity indicator.

```text
gold/training_score/
```

---

## Storage Format

```text
Parquet
```

---

# Data Flow

```text
Strava API
        │
        ▼
Bronze/strava_activities
        │
        ▼
Silver/activities
        │
        ├──► Gold/weekly_summary
        ├──► Gold/monthly_summary
        ├──► Gold/personal_records
        └──► Gold/training_score
```

```text
Google Tasks API
        │
        ▼
Bronze/google_tasks
        │
        ▼
Silver/exercises
        │
        ├──► Gold/weekly_summary
        └──► Gold/monthly_summary
```

---

# Layer Responsibilities

| Layer | Responsibility |
|---------|---------|
| Bronze | Store raw source data |
| Silver | Standardize and validate data |
| Gold | Deliver business and analytical datasets |

---

# Benefits

The Medallion Architecture provides:

- Clear separation of concerns
- Better data lineage
- Improved maintainability
- Easier testing
- Reproducible transformations
- Scalable design patterns

---

# Approved Layer Strategy

## Catalog

```text
fitness_catalog
```

## Schemas

```text
bronze
silver
gold
```

## Bronze Format

```text
JSON
```

## Silver Format

```text
Parquet
```

## Gold Format

```text
Parquet
```

---

# Status

Approved

Version 1