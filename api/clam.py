from .request_data import *
from requests_ntlm import HttpNtlmAuth
from urllib.parse import unquote

def parse_cookies(cookie_header: str) -> dict:
    cookies = {}
    cookie_pairs = cookie_header.split(', ')
    for cookie in cookie_pairs:
        key_value_pair = cookie.split(';', 1)[0]
        key, value = key_value_pair.split('=', 1)
        
        
        cookies[key] = value
    return cookies

class SkolportalSession():
    def __init__(self, username, password) -> None:
        session = requests.Session()
        session.auth = HttpNtlmAuth(username, password)
        portal1 = first_skolportal()
        self.hag_cookies = parse_cookies(portal1.headers["Set-Cookie"])
        print("got skolportalen session")
        portal2 = second_skolportal(self.hag_cookies)
        portal3 = third_skolportal(self.hag_cookies, session)
        if portal3.status_code == 401:
            raise ValueError("Invalid credentials")
        print("authenticated skolportalen")
        #portal_home = home_skolportal(self.hag_cookies)
    def get_user_info(self) -> json:
        return me_skolportal(self.hag_cookies).json()
    def get_user_attributes(self) -> dict:
        return self.get_user_info()["attributes"]
    def set_user_attributes(self, attributes:dict) -> None:
        request = set_me_attributes_skolportal(self.hag_cookies, attributes)
        if request.status_code != 204:
            raise ValueError(f"Attributes not allowed, status code {request.status_code}\n\n{request.text}")

class Skola24Session():
    def __init__(self, skolportal_session:SkolportalSession) -> None:
        skola1 = first_skola24()
        self.skola_cookies = parse_cookies(skola1.headers["Set-Cookie"])
        print("got skola24 session")
        skola2 = second_skola24(self.skola_cookies)
        skola3 = third_skola24(self.skola_cookies)
        #skola_login = skola24_login(self.skola_cookies)
        skola_saml1 = first_skola24_saml()
        saml_data1 = skola_saml1.text.split("lue=\"",1)[1].split("\"",1)[0]
        print("got skola24 saml data")
        skola_saml2 = second_skola24_saml(skolportal_session.hag_cookies, saml_data1)
        saml_data2 = skola_saml2.text.split("lue=\"",1)[1].split("\"",1)[0]
        print("got new skola24 saml data")
        skola_saml3 = third_skola24_saml(saml_data2)
        print("authenticated saml")
        sign_in_url = unquote(skola_saml3.headers["Location"])
        skola_signin = skola24_signin(sign_in_url.split("?t=",1)[1], self.skola_cookies)
        print("signed in to skola24")
    def get_info(self):
        return skola24_info(self.skola_cookies).json()
    def get_timetable(self, week_number, width, height, day, year)->dict:
        years = timetable_years(self.skola_cookies)
        timetables = timetable_timetables(self.skola_cookies)
        key = timetable_key(self.skola_cookies)
        years_data = years.json()
        timetables_data = timetables.json()
        key_data = key.json()
        print("got timetable data")
        timetable_data = timetable(self.skola_cookies, years_data, timetables_data, key_data, week_number, width, height, day)
        print("got timetable")
        return timetable_data.json()
