# Data Models

## Purpose

This document defines the core data models used throughout the Fitness Data Platform.

The models represent the business entities required to ingest, transform, and analyze fitness activity data from multiple sources.

---

# Data Model Overview

The platform consists of three logical layers:

```text
Bronze
  ↓
Silver
  ↓
Gold
```

Bronze stores raw source data.

Silver stores cleansed and standardized business entities.

Gold stores aggregated and analytics-ready datasets.

---

# Bronze Layer Models

## strava_activities

Purpose:

Store raw activity snapshots extracted from the Strava API.

Format:

```text
JSON
```

Examples:

```json
{
  "id": 123456,
  "name": "Morning Run",
  "distance": 5000,
  "moving_time": 1800,
  "type": "Run"
}
```

---

## google_tasks

Purpose:

Store raw exercise records extracted from Google Tasks.

Format:

```text
JSON
```

Examples:

```json
{
  "id": "task_001",
  "title": "Push-ups",
  "due_date": "2026-10-01"
}
```

---

# Silver Layer Models

Silver models standardize data from multiple sources.

---

## activities

Purpose:

Store normalized cardio activities.

### Primary Key

```text
activity_id
```

### Columns

| Column | Type |
|----------|----------|
| activity_id | string |
| source_system | string |
| activity_type | string |
| activity_date | date |
| distance_km | decimal |
| duration_minutes | decimal |
| moving_time_seconds | integer |

---

## exercises

Purpose:

Store normalized strength exercises.

### Primary Key

```text
exercise_id
```

### Columns

| Column | Type |
|----------|----------|
| exercise_id | string |
| source_system | string |
| exercise_name | string |
| exercise_date | date |
| repetitions | integer |
| duration_minutes | decimal |

---

# Gold Layer Models

Gold models support analytics and reporting.

---

## weekly_summary

Purpose:

Weekly training metrics.

### Columns

| Column | Type |
|----------|----------|
| week_start_date | date |
| total_activities | integer |
| total_distance_km | decimal |
| total_duration_minutes | decimal |
| total_exercises | integer |

---

## monthly_summary

Purpose:

Monthly performance aggregation.

### Columns

| Column | Type |
|----------|----------|
| month | string |
| total_activities | integer |
| total_distance_km | decimal |
| total_duration_minutes | decimal |
| total_exercises | integer |

---

## personal_records

Purpose:

Store relevant personal achievements.

### Columns

| Column | Type |
|----------|----------|
| record_date | date |
| activity_type | string |
| metric_name | string |
| metric_value | decimal |

Examples:

- Longest Run
- Fastest 5K
- Longest Ride

---

## training_score

Purpose:

Provide a simplified training intensity indicator.

### Columns

| Column | Type |
|----------|----------|
| score_date | date |
| training_score | decimal |
| total_duration_minutes | decimal |
| total_distance_km | decimal |

---

# Entity Relationships

```text
Strava Activities
        │
        ▼
    activities
        │
        ├────────► weekly_summary
        │
        ├────────► monthly_summary
        │
        ├────────► personal_records
        │
        └────────► training_score


Google Tasks
        │
        ▼
    exercises
        │
        ├────────► weekly_summary
        │
        └────────► monthly_summary
```

---

# Approved Models

The following models are approved for Version 1:

Bronze

- strava_activities
- google_tasks

Silver

- activities
- exercises

Gold

- weekly_summary
- monthly_summary
- personal_records
- training_score