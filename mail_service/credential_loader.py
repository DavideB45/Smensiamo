import json

PATH_CREDENTIALS = '/Users/davideborghini/Documents/GitHub/Smensiamo/mail_service/credential.json'

def load_credential():
    with open(PATH_CREDENTIALS) as f:
        return json.load(f)    