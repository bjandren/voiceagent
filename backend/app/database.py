import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()

# Hämta databasURL från miljövariabler eller använd en standard
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost/voiceagent"
)

# Skapa SQLAlchemy-engine
engine = create_engine(DATABASE_URL)

# Skapa en sessionfabrik
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Skapa en bas för deklarativa modeller
Base = declarative_base()


# Utility-funktion för att få en databassession
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
