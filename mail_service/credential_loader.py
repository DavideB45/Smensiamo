import json

PATH_CREDENTIALS = './mail_service/credential.json'

def load_credential():
    with open(PATH_CREDENTIALS) as f:
        return json.load(f)    