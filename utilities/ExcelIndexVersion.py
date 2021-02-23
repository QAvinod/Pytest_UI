from Config import Enviroment
from Listeners.logger_settings import ui_logger


class IndexVersion:

    """ Environment setup object with index / version instances
    """
    environment = Enviroment.EnvironmentSetup()
    try:
        if environment.server == 'qa':
            index = 0
            version = environment.sprint_version
        elif environment.server == 'dev':
            index = 1
            version = environment.sprint_version
        elif environment.server == 'beta':
            index = 1
            version = environment.sprint_version
        elif environment.server == 'india':
            index = 1
            version = environment.sprint_version

    except Exception as IndexError:
        ui_logger.error(IndexError)
