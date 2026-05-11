# api/core/logging.py

import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path


# ---------------------------------------------------
# Create Logs Directory
# ---------------------------------------------------

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


# ---------------------------------------------------
# Setup Logging
# ---------------------------------------------------

def setup_logging():

    logging.basicConfig(
        level=logging.INFO,

        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),

        handlers=[

            # Console logs
            logging.StreamHandler(sys.stdout),

            # File logs
            RotatingFileHandler(
                LOG_FILE,
                encoding="utf-8",
                maxBytes=1024*1024*5,  # 5 MB
                backupCount=5
            )
        ]
    )


# ---------------------------------------------------
# Get Logger
# ---------------------------------------------------

def get_logger(name: str):

    return logging.getLogger(name)