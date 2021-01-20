import os
import configparser

# ----- Ubuntu -----
PATH = os.getenv("HOME")
CONFIG_FILE_PATH = "%s/PythonFrameWorkNew/Pytest_UI/Config/config.ini" % PATH


config = configparser.RawConfigParser()
config.read(CONFIG_FILE_PATH)


class ReadConfig:
    @staticmethod
    def get_qa_url():
        url = config.get('urls', 'QA')
        return url

    @staticmethod
    def get_beta_url():
        url = config.get('urls', 'BETA')
        return url

    @staticmethod
    def get_stage_url():
        url = config.get('urls', 'STAGE')
        return url

    @staticmethod
    def get_production_url():
        url = config.get('urls', 'PRODUCTION')
        return url

    @staticmethod
    def get_indiaams_url():
        url = config.get('urls', 'INDIAAMS')
        return url
