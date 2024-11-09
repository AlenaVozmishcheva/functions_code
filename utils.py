import re



def get_reg_data():
    name_re = re.compile(r'^[А-Яа-яA-Za-z]+$')
    lastname_re = re.compile(r'^[А-Яа-яA-Za-z]+$')
    phone_re = re.compile(r'^\+(\d{1,3})\((\d{2})\)(\d{7})$')
    email_re = re.compile(r'^[a-zA-Z0-9]+@[yY]andex\.ru$')
    return [name_re, lastname_re, phone_re, email_re]


def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    if not re.match(reg_pattern, user_data):
        print("Данные не соответствуют заданному формату!")
        return None
    if data_to_check is not None:
        res = check_unique_data(user_data, data_to_check)
        if res is False:
            return None
    return user_data

def check_unique_data(user_data, data_to_check):
    if user_data in data_to_check:
        print("Данные уже есть в базе, регистрация невозможна")
        return False
    return True




