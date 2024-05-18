# import logging
from logging import basicConfig, DEBUG,exception

# logging.debug('DEBUG')
# logging.info('INFO')
# logging.warning('WARNING')
# logging.error('ERROR')
# logging.critical('ERROR')

basicConfig(level=DEBUG,
            filename='log.txt',
            filemode='w',
            format='INFO! %(asctime)s | %(levelname)s | %(message)s'
            )

try:
    print('5' + 5)
except BaseException as ex:
    # print(ex)
    exception(ex)
