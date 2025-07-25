from sqlalchemy import Connection, text
from sqlalchemy.exc import SQLAlchemyError
from app.helper.logger import get_logger
from typing import Dict
import os

# Logger setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
logger = get_logger(os.path.join(LOG_DIR, "db.log"))

## TODO's 
# DONE : functions to write tables in database
# DONE : functions to insert data in tables.
# DONE : functions to update data in tables.
# DONE : functions to delete data in tables.
# DONE : general search function to search in tables.


# --- TABLE creation ---
# --- USERS TABLE ---
def create_users_info_table(connection: Connection):
    """
    Creates the users_info table if it does not exist.
    """
    query = '''
        CREATE TABLE IF NOT EXISTS users_info(
            user_id VARCHAR(15) PRIMARY KEY,
            user_full_name VARCHAR(100) NOT NULL,
            user_phone_number VARCHAR(15) NOT NULL UNIQUE,
            user_address TEXT NOT NULL,
            user_password VARCHAR(255) NOT NULL,
            branch_id VARCHAR(10) NOT NULL,
            user_joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (branch_id) REFERENCES branches_info(branch_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
    '''
    try: 
        with connection.begin():
            connection.execute(text(query))
        logger.info("[users_info] Table created or already exists.")
    except SQLAlchemyError as e:
        logger.error(f"[users_info] Table creation failed: {str(e)}")


# --- ACCOUNTS TABLE ---
def create_accounts_info_table(connection: Connection):
    """
    Creates the accounts_info table if it does not exist.
    """
    query = '''
        CREATE TABLE IF NOT EXISTS accounts_info(
            user_id VARCHAR(15) NOT NULL,
            account_number VARCHAR(10) PRIMARY KEY,
            account_type VARCHAR(20) DEFAULT 'debit',
            account_balance DECIMAL(15,2) DEFAULT 0.00,
            FOREIGN KEY (user_id) REFERENCES users_info(user_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
    '''
    try: 
        with connection.begin():
            connection.execute(text(query))
        logger.info("[accounts_info] Table created or already exists.")
    except SQLAlchemyError as e:
        logger.error(f"[accounts_info] Table creation failed: {str(e)}")


# --- BRANCHES TABLE ---
def create_branches_info_table(connection: Connection):
    """
    Creates the branches_info table if it does not exist.
    """
    query = '''
        CREATE TABLE IF NOT EXISTS branches_info(
            branch_id VARCHAR(10) PRIMARY KEY,
            branch_name VARCHAR(100) NOT NULL,
            branch_code VARCHAR(50) UNIQUE NOT NULL,
            branch_contact VARCHAR(15) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query))
        logger.info("[branches_info] Table created or already exists.")
    except SQLAlchemyError as e:
        logger.error(f"[branches_info] Table creation failed: {str(e)}")


# --- TRANSACTIONS TABLE ---
def create_transactions_info_table(connection: Connection):
    """
    Creates the transactions_info table if it does not exist.
    """
    query = '''
        CREATE TABLE IF NOT EXISTS transactions_info(
            transaction_id INT PRIMARY KEY AUTO_INCREMENT,
            sender_user_id VARCHAR(15) NOT NULL,
            receiver_user_id VARCHAR(15) NOT NULL,
            amount DECIMAL(15, 2) NOT NULL,
            transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
            transaction_status ENUM('in_progress', 'completed', 'cancelled') DEFAULT 'in_progress',
            reference_id VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_user_id) REFERENCES users_info(user_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            FOREIGN KEY (receiver_user_id) REFERENCES users_info(user_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query))
        logger.info("[transactions_info] Table created or already exists.")
    except SQLAlchemyError as e:
        logger.error(f"[transactions_info] Table creation failed: {str(e)}")


# --- Insert Functions ---

def insert_user_info(connection: Connection, user_data: Dict):
    """
    Inserts a user into the users_info table.
    
    Expected user_data keys:
    - user_id
    - user_full_name
    - user_phone_number
    - user_address
    - user_password
    - branch_id
    """
    query = '''
        INSERT INTO users_info (
            user_id,
            user_full_name,
            user_phone_number,
            user_address,
            user_password,
            branch_id
        ) VALUES (
            :user_id,
            :user_full_name,
            :user_phone_number,
            :user_address,
            :user_password,
            :branch_id
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query), user_data)
        logger.info(f"[users_info] User {user_data['user_id']} inserted successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[users_info] Insert failed for user {user_data.get('user_id', '')}: {str(e)}")
        return False


def insert_account_info(connection: Connection, account_data: Dict):
    """
    Inserts an account into the accounts_info table.
    
    Expected account_data keys:
    - user_id
    - account_number
    - account_type
    - account_balance
    """
    query = '''
        INSERT INTO accounts_info (
            user_id, account_number, account_type, account_balance
        ) VALUES (
            :user_id, :account_number, :account_type, :account_balance
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query), account_data)
        logger.info(f"[accounts_info] Account {account_data.get('account_number')} inserted successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[accounts_info] Insert failed: {str(e)}")
        return False


def insert_branch_info(connection: Connection, branch_data: Dict):
    """
    Inserts a branch into the branches_info table.
    
    Expected branch_data keys:
    - branch_id
    - branch_name
    - branch_code
    - branch_contact
    """
    query = '''
        INSERT INTO branches_info (
            branch_id, branch_name, branch_code, branch_contact
        ) VALUES (
            :branch_id, :branch_name, :branch_code, :branch_contact
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query), branch_data)
        logger.info(f"[branches_info] Branch {branch_data.get('branch_id')} inserted successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[branches_info] Insert failed: {str(e)}")
        return False


def insert_transaction_info(connection: Connection, transaction_data: Dict):
    """
    Inserts a transaction into the transactions_info table.
    
    Expected transaction_data keys:
    - sender_user_id
    - receiver_user_id
    - amount
    - transaction_type
    - transaction_status
    - reference_id
    """
    query = '''
        INSERT INTO transactions_info (
            sender_user_id, receiver_user_id, amount,
            transaction_type, transaction_status,
            reference_id
        ) VALUES (
            :sender_user_id, :receiver_user_id, :amount,
            :transaction_type, :transaction_status,
            :reference_id
        );
    '''
    try:
        with connection.begin():
            connection.execute(text(query), transaction_data)
        logger.info(f"[transactions_info] Transaction inserted successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[transactions_info] Insert failed: {str(e)}")
        return False


# --- Update Functions ---

def update_user_info(connection: Connection, user_id: str, update_data: Dict):
    """
    Updates user information fields in users_info table.
    Allowed fields: user_full_name, user_address, user_phone_number
    
    Args:
        connection: SQLAlchemy Connection object
        user_id: ID of the user to update
        update_data: Dictionary of fields to update
    """
    allowed_fields = {"user_full_name", "user_address", "user_phone_number"}
    updates = []

    for key in update_data:
        if key in allowed_fields:
            updates.append(f"{key} = :{key}")
        else:
            logger.warning(f"Ignoring invalid field: {key}")

    if not updates:
        logger.warning("No valid fields to update.")
        return

    query = f'''
        UPDATE users_info
        SET {', '.join(updates)}
        WHERE user_id = :user_id
    '''

    try:
        update_data['user_id'] = user_id
        with connection.begin():
            connection.execute(text(query), update_data)
        logger.info(f"[users_info] User {user_id} info updated successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[users_info] Update failed: {str(e)}")
        return False
        
# --- Delete Functions ---

def delete_user(connection: Connection, user_id: str):
    """
    Deletes a user from the users_info table by user_id.
    
    Args:
        connection: SQLAlchemy Connection object
        user_id: ID of the user to delete
    """
    query = """
        DELETE FROM users_info
        WHERE user_id = :user_id
    """
    try:
        with connection.begin():
            connection.execute(text(query), {"user_id": user_id})
        logger.info(f"[users_info] User {user_id} deleted successfully.")
        return True
    except SQLAlchemyError as e:
        logger.error(f"[users_info] Delete failed for user {user_id}: {str(e)}")
        return False


def search_data(connection, table_name: str, search_params: dict):
    try:
        if table_name == "users_info":
            query = text("""
                SELECT * FROM users_info WHERE user_id = :user_id
            """)
            result = connection.execute(query, {"user_id": search_params.get("user_id")})

        elif table_name == "accounts_info":
            query = text("""
                SELECT * FROM accounts_info WHERE user_id = :user_id
            """)
            result = connection.execute(query, {"user_id": search_params.get("user_id")})

        elif table_name == "branches_info":
            query = text("""
                SELECT * FROM branches_info WHERE branch_id = :branch_id
            """)
            result = connection.execute(query, {"branch_id": search_params.get("branch_id")})

        elif table_name == "transactions_info":
            query = text("""
                SELECT * FROM transactions_info
                WHERE (sender_user_id = :user_id OR receiver_user_id = :user_id) AND reference_id = :reference_id
            """)
            result = connection.execute(query, {
                "user_id": search_params.get("user_id"),
                "reference_id": search_params.get("reference_id")
            })

        else:
            logger.warning(f"Search failed: Unknown table '{table_name}' requested.")
            return []

        rows = result.fetchall()
        if not rows:
            logger.info(f"No results found in {table_name} for {search_params}")
        return [dict(row._mapping) for row in rows]

    except SQLAlchemyError as e:
        logger.error(f"Search failed for {table_name}: {str(e)}")
        return []
