import logging
logging.basicConfig(level=logging.DEBUG,filename='tingtong.log',filemode='w',
                    format='%(asctime)s-%(message)s-%(levelname)s')

try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError",exc_info=True)
    logging.exception('test')