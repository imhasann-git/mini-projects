from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get DB URL from .env
db_url = os.getenv("DB_URL")

# SQLAlchemy setup
engine = create_engine(db_url) # type: ignore
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define the table model
class User(Base):
    __tablename__ = 'users'  # table name in DB

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

# Create the table in the database
Base.metadata.create_all(bind=engine)

print("✅ Table 'users' created successfully!")
