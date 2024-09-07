import requests, urllib3, json

urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def first_skolportal():
    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return requests.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, verify=False, allow_redirects=False)

def second_skolportal(cookies):
    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return requests.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, cookies=cookies, verify=False, allow_redirects=False)

def third_skolportal(cookies, session):
    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return session.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, cookies=cookies, verify=False, allow_redirects=False)

def home_skolportal(cookies):
    return requests.get('https://skolportal.uppsala.se/wa/desktop.html', cookies=cookies, verify=False, allow_redirects=False)

def me_skolportal(cookies):
    return requests.get('https://skolportal.uppsala.se/https/api/rest/v1.0/me', cookies=cookies, verify=False, allow_redirects=False)

def set_me_attributes_skolportal(cookies, attributes):
    headers = {
        'Content-Type': 'application/json',
    }

    return requests.post('https://skolportal.uppsala.se/https/api/rest/v1.0/me/attributes', cookies=cookies, headers=headers, data=json.dumps(attributes), verify=False, allow_redirects=False)

def first_skola24():
    return requests.get('https://uppsala-sso.skola24.se/', verify=False, allow_redirects=False)

def second_skola24(cookies):
    params = {
        'c': '1',
    }

    return requests.get('https://uppsala-sso.skola24.se/', params=params, cookies=cookies, verify=False, allow_redirects=False)

def third_skola24(cookies):
    return requests.get('https://uppsala-sso.skola24.se/', cookies=cookies, verify=False, allow_redirects=False)

def skola24_login(cookies):
    params = {
        'host': 'uppsala-sso.skola24.se',
    }

    return requests.get(
        'https://uppsala-sso.skola24.se/Applications/Authentication/login.aspx',
        params=params,
        cookies=cookies,
        verify=False,
        allow_redirects=False
    )

def first_skola24_saml():
    return requests.get(
        'https://service-sso1.novasoftware.se/saml-2.0/authenticate?customer=https%3a%2f%2fskolfederation.uppsala.se%2fidp&targetsystem=Skola24',
        verify=False,
    )

def second_skola24_saml(cookies, saml_data):
    data = {
        'SAMLRequest': saml_data,
    }

    return requests.post(
        'https://skolfederation.uppsala.se/wa/auth/saml/',
        cookies=cookies,
        data=data,
        verify=False,
    )

def third_skola24_saml(saml_data):
    data = {
        'SAMLResponse': saml_data,
    }

    return requests.post('https://service-sso1.novasoftware.se/saml-2.0/response', data=data, allow_redirects=False)

def skola24_signin(t, cookies):
    params = {
        't': t,
    }

    return requests.get('https://web.skola24.se/sign-in', params=params, cookies=cookies)

def skola24_info(cookies):
    headers = {
        'X-Scope': 'a0b6c9c4-11d7-4a52-a030-a55a15058eef',
        'X-Requested-With': 'XMLHttpRequest',
    }

    json_data = None

    return requests.post('https://web.skola24.se/api/get/user/info', cookies=cookies, json=json_data, headers=headers)

def timetable_years(cookies):
    headers = {
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
    }

    json_data = {
        'hostName': '',
        'checkSchoolYearsFeatures': False,
    }

    return requests.post('https://web.skola24.se/api/get/active/school/years', cookies=cookies, headers=headers, json=json_data)

def timetable_timetables(cookies):
    headers = {
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
    }

    json_data = {
        'getPersonalTimetablesRequest': {
            'hostName': 'uppsala-sso.skola24.se',
        },
    }

    return requests.post(
        'https://web.skola24.se/api/services/skola24/get/personal/timetables',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def timetable_key(cookies):
    headers = {
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
    }

    json_data = None

    return requests.post('https://web.skola24.se/api/get/timetable/render/key', cookies=cookies, headers=headers, json=json_data)

def timetable(cookies, years_data, timetables_data, key_data, week, width, height, day, year):
    headers = {
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
    }

    json_data = {
        'renderKey': key_data["data"]["key"],
        'host': 'uppsala-sso.skola24.se',
        'unitGuid': timetables_data["data"]["getPersonalTimetablesResponse"]["studentTimetables"][0]["unitGuid"],
        'schoolYear': years_data["data"]["activeSchoolYears"][0]["guid"],
        'startDate': None,
        'endDate': None,
        'scheduleDay': day,
        'blackAndWhite': False,
        'width': width,
        'height': height,
        'selectionType': 5,
        'selection': timetables_data["data"]["getPersonalTimetablesResponse"]["studentTimetables"][0]["personGuid"],
        'showHeader': False,
        'periodText': '',
        'week': week,
        'year': year,
        'privateFreeTextMode': None,
        'privateSelectionMode': True,
        'customerKey': '',
    }

    return requests.post('https://web.skola24.se/api/render/timetable', cookies=cookies, headers=headers, json=json_data)
