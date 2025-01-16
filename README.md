# Smensiamo
Smensiamo is not a project, an application, or a way to spam emails. Smensiamo is a _mindset_; it is the way you consume lunch and dinner with your friends, the warm comfort of _Mensa Martiri_.

What can make a tour to the university canteen better and more convenient? Well... receiving an email with the menu, a suggested dish, and obviously a Silvio Berlusconi quote. Now deciding what to eat can easily be automated thanks to the power of AI.

## What the code actually does
Running `main.py` will retrieve the Martiri's menu and generate a description using a LLM.

The `mail_service` folder contains all that is necessary to send an email (only a few email providers can be used for this, libero.it is the suggested one, because most providers require 2FA and it is a mess to get around that).

In `web_connection` you can find utility functions to download the menu, crop it, read it, etc.

## Getting started
The setup is not really straightforward; you'll need to set up a couple of accounts and retrieve some keys.

1. Create a libero-email account at [libero.it](https://registrazione.libero.it/?service_id=hp&ref=hp-hd).
2. Request an API key to use Gemini at [gemini](https://aistudio.google.com/app/apikey).

### Config files
`mail_service/credential.json`: This file should have the following format:

```json
{
    "mail": "sender@libero.it",
    "password": "password for sender@libero.it",
    "recipient": ["email1", "email2"],
    "api_key": "google gemini api key"
}
```

`paths`: Set all paths to match the location on your computer (in the future this will possibly be in a single file).

## Automatic execution
On macOS, you can simply use crontab. For more details, read this [tutorial](https://hackernoon.com/automate-python-scripts-on-mac-a-step-by-step-guide-to-scheduling-with-crontab). If you encounter any errors, try giving Full Disk Access to `cron`. To find the path of cron, you can simply type into the terminal `which cron`. By writing, for example, `0 18 * * * /Users/davideborghini/Documents/GitHub/Smensiamo/.conda/bin/python /Users/davideborghini/Documents/GitHub/Smensiamo/main.py >> /Users/davideborghini/Documents/GitHub/Smensiamo/log.txt 2>&1`, errors will be shown in the log file in the project directory.
