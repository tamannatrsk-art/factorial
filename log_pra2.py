import logging
logging.basicConfig(level=logging.INFO, format =' %(asctime)s - %(levelname)s - %(message)s ')
logging.critical('Critical erro! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! critical error!')
logging.error('Error! Error!')