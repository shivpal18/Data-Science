import logging

logging.basicConfig(
    filename='logging.log', level=logging.DEBUG, filemode='w', format='%(asctime)s // %(message)s // %(lineno)d')

logging.debug("This is Debug")
logging.info("This is Info")
logging.warning("This is Warning")
logging.error("This is Error")
logging.critical("This is Critical")