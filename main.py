import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mail_service.credential_loader import load_credential
from mail_service.mail_sender import MailSender
from web_connection.utils_web import *
from web_connection.utils_pdf import *
from datetime import datetime
import google.generativeai as genai

PATH_FOR_PDF = '/Users/davideborghini/Documents/GitHub/Smensiamo/web_connection/menu.pdf'

def get_menu_string() -> str:
    '''
    Get the menu for a specific day.
    
    Args:
        day (str): The day of the week. (m,t,w,t,f,s) or (mon,tue,wed,thu,fri,sat) or (monday,tuesday,wednesday,thursday,friday,saturday)
        dinner (bool): True if dinner, False if lunch.
    
    Returns:
        The menu for the specific day.
    '''
    page_str = get_page_string(TOSCANA_MENU_URL)
    menu_url = get_menu_url(page_str)
    menu_pdf = get_menu_pdf(menu_url)
    save_pdf(menu_pdf, PATH_FOR_PDF)

    today = datetime.today().weekday()
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'Current time is {current_time}')
    dinner_time = datetime.strptime("13:00:00", "%H:%M:%S").time()
    is_dinner = datetime.now().time() >= dinner_time
    print(f'Today is {day_from_int(today)}:')
    crop_pdftable_to_daymeal(PATH_FOR_PDF, today, dinner=is_dinner)
    menu_str = get_text_from_pdf(f'/Users/davideborghini/Documents/GitHub/Smensiamo/web_connection/cropped_menu_{today}_{"True" if is_dinner else "False"}.pdf')

    # Remove the saved PDF files
    for file in os.listdir('/Users/davideborghini/Documents/GitHub/Smensiamo/web_connection'):
        if file.endswith('.pdf'):
            os.remove(os.path.join('/Users/davideborghini/Documents/GitHub/Smensiamo/web_connection', file))
    
    return menu_str

if __name__ == '__main__':
    #print(get_menu_string())
    credentials = load_credential()
    genai.configure(api_key=credentials['api_key'])
    model = genai.GenerativeModel(credentials['model_id'])
    response = model.generate_content(f"Il menù della mensa Martiri di oggi è: {get_menu_string()}. \
Comunicalo all'utente in modo amichevole e conciso (sara' inviata una mail). \
Aggiungi anche una citazione di John Steibeck. (usa emoji e non usare la sintassi markdown)")
    mailer = MailSender(credentials['mail'], credentials['password'], credentials['recipients'])
    mailer.send_mail("Menu", response.text)