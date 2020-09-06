from datetime import datetime


def log(message, category):
    now = datetime.now()
    date_to_string = now.strftime("%d-%m-%Y %H:%M:%S")
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'FATAL']
    file = open('app/log/monitservie.log', 'a')
    if category == 'error':
        write_message = f"{date_to_string} | {levels[3]} | {message}\n"
    elif category == 'fatal':
        write_message = f"{date_to_string} | {levels[4]} | {message}\n"
    elif category == 'warning':
        write_message = f"{date_to_string} | {levels[2]} | {message}\n"
    elif category == 'info':
        write_message = f"{date_to_string} | {levels[1]} | {message}\n"
    elif category == 'debug':
        write_message = f"{date_to_string} | {levels[0]} | {message}\n"
    file.writelines(write_message)
    file.close()
