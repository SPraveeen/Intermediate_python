import logging
import traceback
try:
    a=[1,2,3]
    val=a[3]
except IndexError as e:
    logging.error("Error occurred: %s", e)
    logging.error("Error occurred: %s", e, exc_info=True)
    logging.error("Error occurred: %s", traceback.format_exc())