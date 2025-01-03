import os

import requests
import telebot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
RESUME_ID = os.getenv('RESUME_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
body = {'refresh_token': REFRESH_TOKEN, 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
update_url = f'https://api.superjob.ru/2.0/user_cvs/update_datepub/{RESUME_ID}/'
refresh_url = f'https://api.superjob.ru/2.0/oauth2/refresh_token/'
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)

def update_resume(access_token=None):
    if access_token:
        new_headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.post(update_url, headers=new_headers)
    else:
        response = requests.post(update_url, headers=headers)
    try:
        error_code = response.status_code
        error_value = response.json()['error']['message']
        send_message(f'Ошибка Superjob {error_code}: {error_value}')
    except:
        error_value = ''
        send_message(f'Резюме superjob.ru {RESUME_ID} успешно обновлено!')
    if 'токен' in error_value:
        refresh_token()

def refresh_token():
    response = requests.post(refresh_url, headers=headers, data=body)
    try:
    	error_code = response.status_code
    	error = response.json()['error']
    	error_description = response.json()['error']['error']
    	send_message(f'Ошибка Superjob {error_code}. {error}: {error_description}')
    except:
        new_access_token = response.json()['access_token']
        new_refresh_token = response.json()['refresh_token']
        write_to_env(new_access_token, new_refresh_token)
        send_message('Токен Superjob успешно обновлён!')
        update_resume(new_access_token)

def write_to_env(at, rt):
    set_key(dotenv_file, 'ACCESS_TOKEN', at)
    set_key(dotenv_file, 'REFRESH_TOKEN', rt)

if __name__ == '__main__':
    update_resume()
