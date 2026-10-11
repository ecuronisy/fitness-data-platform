# Strava Setup

## Purpose

This document describes the configuration of the Strava application used by the Fitness Data Platform.

The application provides API access to personal fitness activity data and supports OAuth authentication.

---

# Application Information

## Application Name

```text
Fitness Data Platform
```

## Description

```text
Personal Data Engineering project for collecting, processing, and analyzing fitness activity data using a Bronze/Silver/Gold Lakehouse architecture.
```

## Website

```text
https://github.com/ecuronisy/fitness-data-platform
```

## Authorization Callback Domain

```text
localhost
```

---

# API Credentials

## Client ID

Stored securely as an environment variable.

```text
STRAVA_CLIENT_ID
```

## Client Secret

Stored securely as an environment variable.

```text
STRAVA_CLIENT_SECRET
```

---

# Local Configuration

Credentials must be stored in a local `.env` file.

Example:

```env
STRAVA_CLIENT_ID=<client_id>
STRAVA_CLIENT_SECRET=<client_secret>
```

---

# Security Rules

- Never commit Client ID and Client Secret to GitHub.
- Never store secrets in source code.
- Use environment variables for all credentials.
- Ensure `.env` is included in `.gitignore`.

---

# Development Environment

## Operating System

Local development environment.

## IDE

Visual Studio Code

## Language

Python

---

# Status

Configured

---

# Next Step

S2 - Implement OAuth Authentication