from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import health
from app.middleware.logging import StructuredLoggingMiddleware

app = FastAPI(
    title="Notification microservice ??Firebase FCM push, email (Resend), SMS",
    version=settings.app_version,
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url="/redoc" if settings.app_env != "production" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(StructuredLoggingMiddleware)
app.include_router(health.router, tags=["Health"])
