import os
import pathlib
import datetime


def is_file(path: str):
    if os.path.isfile(path):
        return True
    return False


def create_file(path: str):
    pathlib.Path(path).touch()


def delete_file(path: str):
    os.remove(path)


def is_yes(user_input):
    if user_input.lower() == 'y' or user_input.lower() == 'yes':
        return True
    return False


def is_no(user_input):
    if user_input.lower() == 'n' or user_input.lower() == 'no':
        return True
    return False


def get_date():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    date = now.strftime('%Y/%m/%d')
    return date
