from fastapi import FastAPI

from app.config import load_config
from app.logger import logger


# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

config = load_config()

# app = FastAPI(debug=config.debug)  # Устанавливаем debug режим при создании
app = FastAPI()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def read_root():
    logger.info("Handlig request to root endpoint")
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}
