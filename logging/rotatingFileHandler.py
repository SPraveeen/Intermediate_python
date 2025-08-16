# to track log file size and rotate logs
#  it will create a new log file  called app.log.1 when the current file reaches a certain size

import logging
import time
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

handler=TimedRotatingFileHandler("app.log_1", when="s",interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(10):
    logger.info("This is a log message.")
    time.sleep(2)