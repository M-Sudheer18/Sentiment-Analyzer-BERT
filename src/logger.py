import os
import logging
from datetime import datetime
from config.config import BASE_DIR

logger = logging.getLogger(__name__)

# Generate a TimeStamp for Logged File
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create a 'Logs' directory in the Current Directory
logs_path = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the Logging Format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)