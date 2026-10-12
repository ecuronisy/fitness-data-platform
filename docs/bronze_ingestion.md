# Bronze Ingestion

## Objective

The objective of this process is to extract raw activity data from Strava and store immutable snapshots in the Bronze layer.

This represents the first production ingestion pipeline implemented in the Fitness Data Platform.

---

## Source System

Source:

```text
Strava API
```

Endpoint:

```text
GET /api/v3/athlete/activities
```

---

## Ingestion Flow

```text
Refresh Token
        ↓
Generate Access Token
        ↓
Strava API
        ↓
Activities Endpoint
        ↓
Raw JSON Response
        ↓
Bronze Storage
```

---

## Extraction Script

Implementation:

```text
src/ingestion/extract_strava_activities.py
```

Main responsibilities:

1. Generate a fresh Access Token.
2. Call the Activities API endpoint.
3. Download activity records.
4. Persist the raw response.
5. Create immutable Bronze snapshots.

---

## Storage Location

Raw files are stored in:

```text
data/fitness_catalog/bronze/strava_activities/
```

---

## Snapshot Strategy

Each execution creates a new file.

Example:

```text
activities_20261012_162524.json
```

Benefits:

- Full historical preservation.
- Auditability.
- Replay capability.
- Reprocessing support.
- Data lineage.

---

## Data Format

Bronze data is stored exactly as returned by the source API.

Format:

```text
JSON
```

No transformations are applied.

No filtering is applied.

No business rules are applied.

No schema enforcement is applied.

The Bronze layer acts as the system of record for raw source data.

---

## First Execution Results

Execution Date:

```text
2026-10-12
```

Results:

```text
Activities Downloaded: 47
```

Output File:

```text
data/fitness_catalog/bronze/strava_activities/activities_20261012_162524.json
```

Status:

```text
HTTP 200
```

---

## Example Attributes

A typical activity record contains fields such as:

```json
{
  "id": 123456789,
  "name": "Morning Run",
  "sport_type": "Run",
  "distance": 5000,
  "moving_time": 1800,
  "elapsed_time": 1850,
  "start_date": "2026-10-10T08:00:00Z"
}
```

Actual values vary per activity.

---

## Bronze Layer Principles

The Bronze layer follows the following rules:

- Preserve source fidelity.
- Store raw data.
- Avoid business transformations.
- Maintain historical snapshots.
- Support reproducibility.

---

## Future Enhancements

Planned improvements:

- Incremental ingestion.
- Pagination support.
- Metadata tracking.
- Error handling framework.
- Logging framework.
- Retry mechanism.
- Automated scheduling.

---

## Validation Results

The ingestion process was successfully validated.

Verified capabilities:

- OAuth Authentication.
- Access Token Generation.
- Strava API Connectivity.
- Activity Download.
- Raw JSON Storage.
- Bronze Layer Persistence.

Status:

✅ Completed
