
# # Import Psycopg 3 to connect Python with PostgreSQL
# import psycopg

# # Import database credentials from our application settings
# from app.core.config import settings


# # Database dependency for FastAPI endpoints
# def get_db():

#     # Establish a connection to PostgreSQL
#     connection = psycopg.connect(
#         host=settings.DB_HOST,          # PostgreSQL host
#         port=settings.DB_PORT,          # PostgreSQL port (5433)
#         dbname=settings.DB_NAME,        # Database name
#         user=settings.DB_USER,          # Database username
#         password=settings.DB_PASSWORD,  # Database password
#     )

#     try:
#         # Provide the connection to the API endpoint
#         yield connection

#     finally:
#         # Close the connection after the API request finishes
#         connection.close()




import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
