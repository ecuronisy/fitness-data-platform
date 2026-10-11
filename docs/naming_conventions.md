# Naming Conventions

## Purpose

This document defines the naming standards used throughout the Fitness Data Platform project.

Consistent naming improves readability, maintainability, and collaboration while reducing ambiguity across datasets, code, and documentation.

---

# General Principles

All names should be:

- Descriptive
- Consistent
- Lowercase whenever possible
- Free of spaces
- Easy to understand
- Stable over time

Use English for all project assets.

---

# Repository Naming

## Repository

```text
fitness-data-platform
```

Convention:

```text
kebab-case
```

Example:

```text
fitness-data-platform
customer-analytics-platform
```

---

# Folder Naming

Convention:

```text
snake_case
```

Examples:

```text
fitness_catalog
strava_activities
google_tasks
weekly_summary
personal_records
```

Avoid:

```text
StravaActivities
Strava Activities
strava-activities
```

---

# Python File Naming

Convention:

```text
snake_case.py
```

Examples:

```text
strava_ingestion.py
google_tasks_ingestion.py
activity_transformer.py
training_score_calculator.py
```

Avoid:

```text
StravaIngestion.py
Strava-Ingestion.py
```

---

# Python Variable Naming

Convention:

```python
snake_case
```

Examples:

```python
activity_id
activity_date
total_distance_km
weekly_training_score
```

---

# Python Function Naming

Convention:

```python
snake_case
```

Examples:

```python
extract_strava_activities()
save_raw_snapshot()
calculate_training_score()
```

---

# Python Class Naming

Convention:

```python
PascalCase
```

Examples:

```python
StravaClient
GoogleTasksClient
ActivityProcessor
TrainingScoreCalculator
```

---

# Constants

Convention:

```python
UPPER_CASE
```

Examples:

```python
BRONZE_PATH
SILVER_PATH
GOLD_PATH
DEFAULT_PAGE_SIZE
```

---

# JSON File Naming

Convention:

```text
source_entity_yyyymmdd.json
```

Examples:

```text
strava_activities_20261011.json
google_tasks_20261011.json
```

---

# Bronze Layer Naming

Convention:

```text
source_entity
```

Examples:

```text
strava_activities
google_tasks
```

---

# Silver Layer Naming

Convention:

```text
business_entity
```

Examples:

```text
activities
exercises
```

---

# Gold Layer Naming

Convention:

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

# Documentation Naming

Convention:

```text
snake_case.md
```

Examples:

```text
project_scope.md
architecture_decisions.md
naming_conventions.md
data_models.md
physical_data_layout.md
```

---

# Test Naming

Convention:

```text
test_<module>.py
```

Examples:

```text
test_strava_ingestion.py
test_activity_transformer.py
test_training_score.py
```

---

# Git Branch Naming

Convention:

```text
feature/<feature_name>
bugfix/<issue_name>
docs/<document_name>
```

Examples:

```text
feature/strava-ingestion
feature/google-tasks-api
docs/project-scope
bugfix/oauth-refresh-token
```

---

# Commit Message Naming

Convention:

```text
<type>: <description>
```

Types:

```text
feat
fix
docs
refactor
test
chore
```

Examples:

```text
feat: add strava oauth integration
feat: implement bronze ingestion layer

docs: add project scope document
docs: add architecture decisions

test: add unit tests for strava ingestion

refactor: improve activity transformation logic
```

---

# Approved Standards

These naming conventions apply to all current and future components of the Fitness Data Platform project.

Any exceptions should be documented and justified.