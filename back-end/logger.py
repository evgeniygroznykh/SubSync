from config import PROVIDER_CONFIG
from concurrent_log_handler import ConcurrentRotatingFileHandler
import logging


LOGGING_CFG_KEY = 'logging'
LOG_FOLDER_CFG_KEY = 'logFolder'
ROTATING_PERIOD_TYPE_CFG_KEY = 'rotatingPeriodType'
ROTATING_PERIOD_VALUE_CFG_KEY = 'rotatingPeriodValue'

LOG_FOLDER = PROVIDER_CONFIG[LOGGING_CFG_KEY][LOG_FOLDER_CFG_KEY]
ROTATING_PERIOD_TYPE = PROVIDER_CONFIG[LOGGING_CFG_KEY][ROTATING_PERIOD_TYPE_CFG_KEY]
ROTATING_PERIOD_VALUE = PROVIDER_CONFIG[LOGGING_CFG_KEY][ROTATING_PERIOD_VALUE_CFG_KEY]


def prepare_log_message(channel_name, target_file, event):
    if event == 'new_subtitle':
        return f"{channel_name}: {target_file} was copied to server. Reason: new subtitle file."
    elif event == 'subtitle_update':
        return f"{channel_name}: {target_file} was copied to server. Reason: subtitle file was changed in source folder."
    elif event == 'subtitle_deletion':
        return f"{channel_name}: {target_file} was deleted from server. Reason: clip for this subtitle file was deleted."

def create_log_record(message, log_level):
    handler = ConcurrentRotatingFileHandler(f'{LOG_FOLDER}\\workflow_log',
                                    mode="a",
                                    maxBytes=1000,
                                    backupCount=1)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[handler])

    logger = logging.getLogger("WORKFLOW")
    logger.setLevel(log_level)
    if log_level == logging.INFO:
        logger.info(message)
    elif log_level == logging.DEBUG:
        logger.debug(message)
    elif log_level == logging.WARNING:
        logger.warning(message)
    elif log_level == logging.CRITICAL:
        logger.critical(message)
    elif log_level == logging.ERROR:
        logger.error(message)