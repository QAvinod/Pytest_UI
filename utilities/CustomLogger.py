import logging
import os

PATH = os.getenv("HOME")
LOG_FILE_PATH = "%s/PythonFrameWorkNew/Pytest_UI/Logs/automation.log" % PATH


class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename=LOG_FILE_PATH,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


