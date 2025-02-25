import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Driven Customer Support Agent"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "SaaS-baserad AI-kundsupportagent för fastighetsbolag"

    # Databasinställningar
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost/voiceagent"
    )

    # Twilio-inställningar
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN", "")
    TWILIO_PHONE_NUMBER: str = os.getenv("TWILIO_PHONE_NUMBER", "")

    # Elevenlabs-inställningar
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")

    # API-inställningar
    API_PREFIX: str = "/api/v1"
    BACKEND_CORS_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Skapa en inställningsinstans
settings = Settings()
