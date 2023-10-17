import requests
import json


def GetLocalHighScore():
    with open('allData/json/data.json', 'r') as f:
        data = json.load(f)
    highscore = data["CHIMP_TEST_LEVEL"]
    return highscore


def requestUrl(mode, username):
    readUrl = 'http://127.0.0.1:5000/highscore/read'
    submitUrl = 'http://127.0.0.1:5000/highscore/submit'
    update = 'http://127.0.0.1:5000/highscore/update'
    # data = {username : highscore}
    try:
        if mode == 'read':
            url = readUrl + '?username=' + username
            response = requests.get(url)
            if response.status_code == 200:
                print(response.status_code)
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            print(response.text)
            return response.text

        if mode == 'submit':
            url = submitUrl
            highscore = 1
            data = {username: highscore}
            response = requests.post(url, json=data)
            if response.status_code == 200:
                pass
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            print(response.text)
            return response.text

        if mode == 'update':
            url = update
            hs = GetLocalHighScore()
            data = {username: hs}
            response = requests.post(url, json=data)
            if response.status_code == 200:
                pass
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            print(response.text)
            return response.text
    except requests.exceptions.RequestException as e:
        return 'server offline'
