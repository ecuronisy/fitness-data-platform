# Incremental Bronze Ingestion

## Objective

The objective of this sprint is to evolve the ingestion process from a full historical extraction to an incremental extraction pattern.

Instead of downloading all available activities on every execution, the pipeline only retrieves activities created after the most recently processed activity.

This approach reduces:

- API traffic
- Processing time
- Storage consumption
- Unnecessary reprocessing

---

## Background

The initial ingestion process implemented in Sprint S3 successfully loaded the complete activity history from Strava.

Process:

```text
Strava API
    ↓
Download All Activities
    ↓
Store Raw JSON
    ↓
Bronze Layer
```

Although functional, this design downloads historical records repeatedly.

The incremental ingestion process addresses this limitation.

---

## Incremental Strategy

The solution uses a High Water Mark (HWM) approach.

A metadata file stores the timestamp of the latest activity successfully processed.

Structure:

```json
{
    "last_activity_date": "2026-10-12T15:03:14Z"
}
```

This value acts as the ingestion checkpoint.

---

## Metadata Storage

Metadata is stored separately from business data.

Location:

```text
data/metadata/strava_ingestion_state.json
```

Purpose:

- Maintain ingestion state.
- Track latest processed activity.
- Support incremental loads.
- Avoid historical reprocessing.

---

## Watermark Design

The pipeline uses:

```text
start_date
```

from the Strava activity payload.

Example:

```json
{
    "id": 20555793489,
    "start_date": "2026-10-12T15:03