import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')   
logging.debug('Some minot code and debugging details. ')

logging.info('An event happend')
logging.warning('SOmething could go wrong')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover !')