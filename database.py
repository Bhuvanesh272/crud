from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:bhuvaneshraj%4027@localhost:5432/bhuvanesh"  # Replace with your actual database URL
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)