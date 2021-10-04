from requests import session
from json import loads
from bs4 import BeautifulSoup as bs


class API(object):
    def __init__(self):
        self.base_url = "https://focus.pcsb.org/focus/"
        self.api_url = "API/APIEndpoint.php"
        self.modules_url = "Modules.php?force_package=SIS&modname=misc/Portal.php"
        
        self.session = session()
    
    def login(self, username, password):
        payload = {"login": "true", "data": f"username={username}&password={password}"}
        request = self.session.post(self.base_url, data=payload)
        response = loads(request.text)
        print(response)

    def grades(self):
        # find where grades API goes
        return None


if __name__ == "__main__":
    api = API()
    api.login("8g.2r", "F3tusd3l3tus")
    print(api.grades())
