import requests

def requestUrl(mode, username):
    readhighscoreUrl = 'http://127.0.0.1:5000/highscore/read'
    submithighscoreUrl = 'http://127.0.0.1:5000/highscore/submit'
    #data = {username : highscore}
    if mode == 'read':
        url = readhighscoreUrl + '?username=' + username
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            print(response.status_code)
        else:
            print(f"Request failed with status code: {response.status_code}")

    if mode == 'submit':
        url = submithighscoreUrl
        highscore = 1
        data = {username : highscore}
        response = requests.post(url, json=data) 
        print(response.text)
        if response.status_code == 200:
            pass
        else:
            print(f"Request failed with status code: {response.status_code}")
    return response.text