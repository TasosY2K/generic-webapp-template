import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from models import Base

DB_PATH = "postgresql://postgres:root@localhost:5432"

engine = db.create_engine(DB_PATH, echo=False)
try:
    with db.create_engine(DB_PATH, isolation_level="AUTOCOMMIT").connect() as connection:
        connection.execute("""
        SET AUTOCOMMIT = ON;
        CREATE DATABASE cloud;
        CREATE TABLE PowerMeasurement(
            id INT PRIMARY KEY NOT NULL,
            timestamp STRING,
            source STRING,
            value STRING
        );
        """)
except db.exc.OperationalError:
    print("Could not connect to database")
    exit()
except db.exc.ProgrammingError:
    pass