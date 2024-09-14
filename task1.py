# Задание 1. Логирование с использованием нескольких файлов.

import logging

logger = logging.getLogger('multi_file_logger')
logger.setLevel(logging.DEBUG)

# Обработчик для debug и info
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.addFilter(lambda record: record.levelno <= logging.INFO)

# Обработчик для warning и errors
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")