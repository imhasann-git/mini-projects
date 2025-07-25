import os
import dotenv

dotenv.load_dotenv()  # Loading variables from .env file

DB_URL = os.getenv("DB_URL")
