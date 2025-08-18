import logging

logging.basicConfig(level=logging.DEBUG,filename='log1.log',filemode='w',
                    format='%(asctime)s-%(levelname)s-%(message)s')
x=2
logging.info(f'the logging variable message is {x}')