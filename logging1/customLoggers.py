import logging
logging.basicConfig(level=logging.INFO,filename='logi.log',filemode='w',
                    format='%(asctime)s-%(levelname)s-%(message)s')

logger=logging.getLogger(__name__)
logger.info('test the custom logger')