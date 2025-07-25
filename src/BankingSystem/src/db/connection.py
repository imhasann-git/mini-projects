from app.config import DB_URL
from app.helper.logger import get_logger
from db.operations import (
    create_users_info_table,
    create_accounts_info_table,
    create_branches_info_table,
    create_transactions_info_table
)
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

# Logger setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
logger = get_logger(os.path.join(LOG_DIR, "db.log"))

# initlising connection from Hosted platform
def create_connection(DB_URL):
    try:
        engine = create_engine(DB_URL)
        connection = engine.connect()
        logger.info("Database connection established.")
        return engine, connection
    except SQLAlchemyError as e:
        logger.error(f"Database connection failed: {str(e)}")
        return None, None

# creating tables into database.
def init_db(DB_URL):
    try:
        db_engine, connection = create_connection(DB_URL=DB_URL)
        if connection is None:
            raise SQLAlchemyError("Connection is None.")

        # Creating all required tables
        create_branches_info_table(connection=connection)
        create_users_info_table(connection=connection)
        create_accounts_info_table(connection=connection)
        create_transactions_info_table(connection=connection)

        logger.info("All tables created successfully.")

    except SQLAlchemyError as e:
        logger.error(f"Database initialization failed: {str(e)}")
    finally:
        if connection:
            connection.close()
            logger.info("Database connection closed.")
        if db_engine:
            db_engine.dispose()
