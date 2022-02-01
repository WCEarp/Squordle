import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Discord Settings
DISCORD_TOKEN = os.environ.get("SECRET_KEY")

# Database Settings
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PSWD = os.environ.get("DATABASE_PSWD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")