# OAuth Authentication

## Objective

Implement secure authentication against the Strava API using OAuth 2.0.

---

## Overview

The Fitness Data Platform uses the OAuth 2.0 Authorization Code Flow to access personal fitness data from Strava.

The solution is designed to:

- Authenticate securely.
- Avoid hardcoded credentials.
- Support long-term automated ingestion.
- Refresh access tokens automatically.

---

## OAuth Flow

```text
User Authorization
        ↓
Authorization Code
        ↓
Access Token + Refresh Token
        ↓
Refresh Token
        ↓
New Access Tokens
        ↓
API Requests
```

---

## Authorization Request

The following scopes were requested:

```text
read
activity:read_all
```

Authorization URL structure:

```text
https://www.strava.com/oauth/authorize
```

Example:

```text
https://www.strava.com/oauth/authorize?client_id=<client_id>&response_type=code&redirect_uri=http://localhost&approval_prompt=force&scope=read,activity:read_all
```

---

## Authorization Code

After successful authorization, Strava redirects the browser to:

```text
http://localhost/?state=&code=<authorization_code>&scope=read,activity:read_all
```

Because no application is listening on localhost, the browser displays a connection error.

This behavior is expected.

The Authorization Code is manually copied from the browser URL and exchanged for tokens.

---

## Token Exchange

The Authorization Code is exchanged through:

```text
POST https://www.strava.com/oauth/token
```

The response contains:

- Access Token
- Refresh Token
- Expiration Information
- Athlete Information

---

## Refresh Token Strategy

The project does not rely on manually generated Access Tokens.

Instead, every execution follows this process:

```text
Refresh Token
      ↓
Generate Access Token
      ↓
Execute API Requests
```

Benefits:

- Automatic token renewal
- No manual intervention
- Long-term maintainability
- Production-ready authentication pattern

---

## Environment Configuration

Sensitive values are stored locally:

```text
config/.env
```

Example:

```env
STRAVA_CLIENT_ID=286670
STRAVA_CLIENT_SECRET=<secret>
STRAVA_REFRESH_TOKEN=<refresh_token>
```

Credentials are excluded from source control.

---

## Security Principles

- No secrets are committed to GitHub.
- No secrets are hardcoded.
- Credentials are stored locally.
- Access Tokens are generated dynamically.
- Refresh Tokens are protected using environment variables.

---

## Validation Results

The following validations were completed successfully:

- OAuth authorization completed.
- Authorization Code obtained.
- Access Token generated.
- Refresh Token generated.
- Access Token refreshed successfully.
- API authentication verified.

Status:

✅ Completed