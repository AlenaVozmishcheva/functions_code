import utils

users_list = []
patterns = utils.get_reg_data()
while len(users_list) < 3:
    user_data_list = []
    while len(user_data_list) < 4:
        name = input("Введите имя пользователя: ")
        name = utils.reg_check(name, patterns[0], users_list)
        if name is None:
            continue
        lastname = input("Введите фамилию пользователя: ")
        lastname = utils.reg_check(lastname, patterns[1], users_list)
        if lastname is None:
            continue
        phone = input("Введите номер телефона пользователя: ")
        phone = utils.reg_check(phone, patterns[2], users_list, list(map(lambda l: l[2], users_list)))
        if phone is None:
            continue
        email = input("Введите email пользователя: ")
        email = utils.reg_check(email, patterns[3],users_list, list(map(lambda l: l[3], users_list)))
        if email is None:
            continue
        user_data_list = [name,lastname,phone,email]
        users_list.append(user_data_list)
for user_data_list in users_list:
    print(user_data_list)

