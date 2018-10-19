
import pdb
import logging
import m_conf as conf

logging.basicConfig()
logger = logging.getLogger('fourcheball_daemon')
logger.setLevel(conf.get_logger_level())

logger.info('Init daemon')

while True:
    logger.debug('Run 1')
    raw_input() # dev purpose
    sleep(3)
