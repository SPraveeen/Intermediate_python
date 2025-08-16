# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# using other helper file
# import helper

# set different log handllers
import logging
import logging.config

logging.config.dictConfig('logging.conf')
logger=logging.getLogger('simpleExample')
logger.debug('This is a debug message')

# logger=logging.getLogger(__name__)

# # create handler
# stream_h=logging.StreamHandler()
# file_h=logging.FileHandler('File.log')

# # set level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# # add handler to logger
# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning message')
# logger.error('This is an error message')