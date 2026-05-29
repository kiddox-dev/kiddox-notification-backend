# kiddox-notification-backend

Notification microservice — Firebase FCM push, email (Resend), SMS.

## Tech Stack

- Python 3.11+
- FastAPI + Uvicorn
- Pydantic v2 + pydantic-settings
- Supabase Python client
- structlog for structured logging
- Prometheus client for metrics

## Quick Start

```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8005
```

## License

Proprietary — Kiddox Limited
