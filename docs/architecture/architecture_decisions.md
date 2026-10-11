# Architecture Decisions

## Purpose

This document records the key architectural decisions made during the design phase of the Fitness Data Platform.

The objective is to establish a simple, scalable, and maintainable foundation while applying Data Engineering best practices.

---

# AD-001: Use Python as the Primary Development Language

## Decision

Python will be used as the primary programming language for the project.

## Rationale

Python is the most widely adopted language in Data Engineering and provides extensive support for:

- API integrations
- Data processing
- Data validation
- Analytics
- Testing
- Automation

It also aligns with the project's portfolio and learning objectives.

---

# AD-002: Implement a Bronze / Silver / Gold Architecture

## Decision

The platform will follow a layered data architecture consisting of:

- Bronze Layer
- Silver Layer
- Gold Layer

## Rationale

This architecture separates:

- Raw data ingestion
- Data cleansing and standardization
- Business-ready analytics

Benefits include:

- Improved maintainability
- Better data lineage
- Easier troubleshooting
- Industry-aligned design patterns

---

# AD-003: Simulate a Lakehouse Locally

## Decision

A local folder structure will be used to simulate a Lakehouse architecture.

## Rationale

This approach allows core Data Engineering concepts to be implemented without requiring cloud infrastructure.

The design mirrors common analytics platforms while remaining lightweight and cost-effective.

---

# AD-004: Use a Catalog-Based Structure

## Decision

A logical catalog named:

fitness_catalog

will be used to organize datasets.

## Rationale

The structure follows concepts commonly found in modern Data Platforms and Data Warehouses.

This improves navigation and readability while providing a foundation for future migration to cloud environments.

---

# AD-005: Use JSON for Bronze Layer Storage

## Decision

Raw source data will be stored as JSON files.

## Rationale

JSON preserves the original API response and supports:

- Auditing
- Troubleshooting
- Replayability
- Historical snapshots

Raw data must remain unchanged after ingestion.

---

# AD-006: Use Parquet for Silver and Gold Layers

## Decision

Processed datasets will be stored using Parquet.

## Rationale

Parquet provides:

- Columnar storage
- Better compression
- Faster analytical queries
- Improved scalability

This makes it an appropriate format for transformed and analytics-ready datasets.

---

# AD-007: Use Strava as Primary Fitness Data Source

## Decision

Strava will be the primary source for cardio-related activities.

## Supported Activity Types

- Running
- Cycling
- Walking

## Rationale

Strava exposes a public API and provides rich activity data suitable for analytics and Data Engineering exercises.

---

# AD-008: Use Google Tasks as Secondary Data Source

## Decision

Google Tasks will store manually tracked strength and body-weight exercises.

## Supported Exercise Types

- Push-ups
- Leg raises
- Squats
- Planks

## Rationale

Google Tasks complements Strava by capturing workouts not typically recorded through sports tracking applications.

---

# AD-009: Repository Structure

## Decision

The repository will use the following top-level structure:

```text
fitness-data-platform/
│
├── config/
├── data/
├── docs/
├── notebooks/
├── src/
├── tests/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Rationale

The structure separates:

- Source code
- Data
- Documentation
- Configuration
- Testing assets

This improves maintainability and project organization.

---

# AD-010: Local Development First

## Decision

The project will initially run entirely on a local machine.

## Rationale

Local development reduces complexity and enables focus on:

- Data Engineering concepts
- Python development
- Data modeling
- API integration

Cloud technologies may later be incorporated as optional extensions.

---

# Approved Architecture

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

## Physical Layout

```text
data/
└── fitness_catalog/
    ├── bronze/
    │   ├── strava_activities/
    │   └── google_tasks/
    │
    ├── silver/
    │   ├── activities/
    │   └── exercises/
    │
    └── gold/
        ├── weekly_summary/
        ├── monthly_summary/
        ├── personal_records/
        └── training_score/
```

---

# Status

Approved

Date: October 2026