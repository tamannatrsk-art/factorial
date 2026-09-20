import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(asctime)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial (' + str(n) + ')')
    total = 1
    for i in range (n+1):
        total *= 1
        logging.debug('i is ' + str(i) + ' , total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')