import logging
import os
from datetime import datetime

LOG_FILE = "logs"

LOG_DIR = os.path.join(os.getcwd(),LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
filename = f"log_{CURRENT_TIME_STAMP}.log"

LOG_FILE_PATH = os.path.join(LOG_DIR,filename)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.NOTSET)