from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage


class CandidateLobbyLogin:
    def __init__(self, driver):
        self.driver = driver
        self.candidate_login = LoginPage(self.driver)

        self.candidate_lobby_collection = []

    def candidate_lobby_login(self, candidate_id):

        self.candidate_lobby_collection = []
        __list = [self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room()
                  ]
        for func in __list:
            if func:
                self.candidate_lobby_collection.append(func)
            else:
                self.candidate_lobby_collection.append(func)
