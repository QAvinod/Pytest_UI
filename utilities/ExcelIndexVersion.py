from Config import Enviroment
from Scripts.JobCreation.crpo_job_configuration import CRPOJobConfiguration
from Scripts.JobCreation.crpo_job_creation import CRPOJobCreation
from Scripts.LoginPage.crpo_login_page import CRPOLogin


class IndexVersion:

    """ Environment setup object with index / version instances
    """
    environment = Enviroment.EnvironmentSetup()
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

    """ Required class Objects are created 
    """
