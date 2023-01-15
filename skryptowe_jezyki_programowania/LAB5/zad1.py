import re


def emailValidation(mail):
    emailRegex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(emailRegex, mail):
        print('Poprawny email')
    else:
        email = input('Email jest niepoprawny, podaj poprawny email: ')
        emailValidation(email)


def loginValidation(log):
    loginRegex = re.compile(r'^[a-zA-Z0-9]{4,}$')
    if re.fullmatch(loginRegex, log):
        print('Poprawny login')
    else:
        login = input('Login jest niepoprawny, podaj poprawny login: ')
        loginValidation(login)


def pwdValidation(password):
    pwdRegex = re.compile(
        r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
    if re.fullmatch(pwdRegex, password):
        print('Poprawne hasło')
    else:
        pwd = input('Hasło jest niepoprawne, podaj poprawne hasło: ')
        loginValidation(pwd)


login = input('Podaj login: ')
loginValidation(login)

pwd = input('Podaj hasło: ')
pwdValidation(pwd)

email = input('Podaj email: ')
emailValidation(email)
