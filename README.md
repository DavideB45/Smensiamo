# Smensiamo
Smensiamo is not a project, an application, a way to spam e-mails. Smesiamo is a _mindset_ it is the way you consume lunch and dinner with your friends, the warm comfort of _Mensa Martiri_

What can make a tour to the university cantine better and more convenient? Well... receiving an email with the menu, a suggested dish and obviously a Silvio Berlusconi quote. Now decide what to eat can easily be automatized thaks to the power of AI.

## What the code actually does
Running `main.py` will retrieve the Martiri's menu and generate a desctiption using a LLM.

The `mail_service` folder contains all that is necessary to send an email (only few email provider can be used for this, libero.it is the suggested one, this because most of the provider requre 2fa and it is a mess to get around that)

In `web_connection` can be founded utility functions to download the menu, crop it, read it etc..

## Getting started
The setup is not really straightforward, you'll need to setup a coupple of accounts, and retrieve some key.

create a libero-email account at [libero.it](https://registrazione.libero.it/?service_id=hp&ref=hp-hd)

require an api key to use gemini at [gemini](https://aistudio.google.com/app/apikey)

Config files:
`mail_service/credential.json`: in this file should have the form

```json
{
    "mail": "sender@libero.it",
    "password": "password for sender@libero.it",
    "recipient": "email to which email will be sent",
    "api_key": "google gemini api key"
}
```

`paths`: set all path to match the location on your computer (in teh future this will possibly be in a single file)