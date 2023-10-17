from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)
dataPath = 'allData/ServerData/data.json'

def GetUserHighScore(username):
    with open(dataPath) as f:
        data = json.load(f)
    if username in data:
        print(data[username])
        return str(data[username])
    else:
        return 'none'

@app.route('/highscore/read', methods=['GET'])
def give_data():
    username = request.args.get('username')
    print(username)
    data = GetUserHighScore(username)
    if data == 'none':
        response = make_response("user not registered")
    else:
        response = make_response(data)
    response.status_code = 200
    return response

@app.route('/highscore/submit', methods=['POST'])
def submit_data():
    datareceived = request.get_json()
    username = list(datareceived.keys())[0]
    score = datareceived[username]
    print(username, score)
    
    statusdumping=dumpToJson(data=datareceived, username=username)
    if statusdumping:
        response=make_response('already exist')
        return response
    else:
        response = make_response('success')
    response.status_code = 200
    return response

@app.route('/highscore/update', methods=['POST'])
def update_data():
    datareceived = request.get_json()
    username = list(datareceived.keys())[0]
    score = datareceived[username]
    print(username, score)
    print(datareceived)
    
    if updateJson(datareceived, username) == True:
        response = make_response('True')
    else:
        response = make_response('False')
    response.status_code = 200
    return response


def updateJson(data, username):
    with open(dataPath, 'r') as f:
        file_contents = f.read()
        if file_contents:
            jsondata = json.loads(file_contents)
        else:
            jsondata = {}

    if username in jsondata:
        print('updating highscore for ', username)
        jsondata.update(data)
        # Write the updated JSON data back to the file
        with open(dataPath, 'w') as f:
            json.dump(jsondata, f, indent=4)  # You can use 'indent' for formatting
        print("Data updated and saved to data.json")
        return True

    else:
        return False


def dumpToJson(data, username):
    with open(dataPath, 'r') as f:
        file_contents = f.read()
        if file_contents:
            jsondata = json.loads(file_contents)
        else:
            jsondata = {}

    if username in jsondata:
        return True

    else:
        # Merge the existing JSON data with the new data
        jsondata.update(data)
        # Write the updated JSON data back to the file
        with open(dataPath, 'w') as f:
            json.dump(jsondata, f, indent=4)  # You can use 'indent' for formatting
        print("Data updated and saved to data.json")
        return False



if __name__ == '__main__':
    app.run('0.0.0.0', 5000)