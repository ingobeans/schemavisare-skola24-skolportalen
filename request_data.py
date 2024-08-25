import requests, urllib3, json

urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def first_skolportal():
    headers = {
        'Host': 'skolportal.uppsala.se',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return requests.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, headers=headers, verify=False, allow_redirects=False)

def second_skolportal(cookies):
    headers = {
        'Host': 'skolportal.uppsala.se',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return requests.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def third_skolportal(cookies, session):
    headers = {
        'Host': 'skolportal.uppsala.se',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    params = {
        'authmech': 'Elever och lärare på skolan',
    }

    return session.get('https://skolportal.uppsala.se/wa/auth/wil/', params=params, cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def home_skolportal(cookies):
    headers = {
        'Host': 'skolportal.uppsala.se',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    return requests.get('https://skolportal.uppsala.se/wa/desktop.html', cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def me_skolportal(cookies):
    headers = {
        'Host': 'skolportal.uppsala.se',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'en-GB',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://skolportal.uppsala.se/wa/desktop.html',
        'Priority': 'u=1, i',
        'Connection': 'keep-alive',
    }

    return requests.get('https://skolportal.uppsala.se/https/api/rest/v1.0/me', cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def set_me_attributes_skolportal(cookies, attributes):
    headers = {
        'Content-Type': 'application/json',
    }

    return requests.post('https://skolportal.uppsala.se/https/api/rest/v1.0/me/attributes', cookies=cookies, headers=headers, data=json.dumps(attributes), verify=False, allow_redirects=False)

def first_skola24():
    headers = {
        'Host': 'uppsala-sso.skola24.se',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://skolportal.uppsala.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    return requests.get('https://uppsala-sso.skola24.se/', headers=headers, verify=False, allow_redirects=False)

def second_skola24(cookies):
    headers = {
        'Host': 'uppsala-sso.skola24.se',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Referer': 'https://skolportal.uppsala.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    params = {
        'c': '1',
    }

    return requests.get('https://uppsala-sso.skola24.se/', params=params, cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def third_skola24(cookies):
    headers = {
        'Host': 'uppsala-sso.skola24.se',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Referer': 'https://skolportal.uppsala.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    return requests.get('https://uppsala-sso.skola24.se/', cookies=cookies, headers=headers, verify=False, allow_redirects=False)

def skola24_login(cookies):
    headers = {
        'Host': 'uppsala-sso.skola24.se',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://uppsala-sso.skola24.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    params = {
        'host': 'uppsala-sso.skola24.se',
    }

    return requests.get(
        'https://uppsala-sso.skola24.se/Applications/Authentication/login.aspx',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
        allow_redirects=False
    )

def first_skola24_saml():
    headers = {
        'Host': 'service-sso1.novasoftware.se',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://uppsala-sso.skola24.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    return requests.get(
        'https://service-sso1.novasoftware.se/saml-2.0/authenticate?customer=https%3a%2f%2fskolfederation.uppsala.se%2fidp&targetsystem=Skola24',
        headers=headers,
        verify=False,
    )

def second_skola24_saml(cookies, saml_data):
    headers = {
        'Host': 'skolfederation.uppsala.se',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="127", "Not)A;Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-GB',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://service-sso1.novasoftware.se',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://service-sso1.novasoftware.se/',
        'Priority': 'u=0, i',
        'Connection': 'keep-alive',
    }

    data = {
        'SAMLRequest': saml_data,
    }

    return requests.post(
        'https://skolfederation.uppsala.se/wa/auth/saml/',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

def third_skola24_saml(saml_data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://skolfederation.uppsala.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://skolfederation.uppsala.se/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0, i',
    }

    data = {
        'SAMLResponse': saml_data,
    }

    return requests.post('https://service-sso1.novasoftware.se/saml-2.0/response', headers=headers, data=data, allow_redirects=False)

def skola24_signin(t, cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://skolfederation.uppsala.se/',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0, i',
    }

    params = {
        't': t,
    }

    return requests.get('https://web.skola24.se/sign-in', params=params, cookies=cookies, headers=headers)

def skola24_info(cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Scope': 'a0b6c9c4-11d7-4a52-a030-a55a15058eef',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web.skola24.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://web.skola24.se/portal/start/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = None

    return requests.post('https://web.skola24.se/api/get/user/info', cookies=cookies, headers=headers, json=json_data)

def timetable_years(cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web.skola24.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://web.skola24.se/portal/start/timetable/timetable-viewer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'hostName': '',
        'checkSchoolYearsFeatures': False,
    }

    return requests.post('https://web.skola24.se/api/get/active/school/years', cookies=cookies, headers=headers, json=json_data)

def timetable_timetables(cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web.skola24.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://web.skola24.se/portal/start/timetable/timetable-viewer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web.skola24.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://web.skola24.se/portal/start/timetable/timetable-viewer/uppsala-sso.skola24.se/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = None

    return requests.post('https://web.skola24.se/api/get/timetable/render/key', cookies=cookies, headers=headers, json=json_data)

def timetable(cookies, years_data, timetables_data, key_data, week, width, height, day):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'X-Scope': '8a22163c-8662-4535-9050-bc5e1923df48',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web.skola24.se',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://web.skola24.se/portal/start/timetable/timetable-viewer/uppsala-sso.skola24.se/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
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
        'year': 2024,
        'privateFreeTextMode': None,
        'privateSelectionMode': True,
        'customerKey': '',
    }

    return requests.post('https://web.skola24.se/api/render/timetable', cookies=cookies, headers=headers, json=json_data)
