

def italic(func):
    def wrapper(inpt):
        return "\x1B[3m" + func(inpt) + "\x1B[0m"
    return wrapper


def bold(func):
    def wrapper(inpt):
        return "\033[1m" + func(inpt) + "\033[0m"
    return wrapper


def underline(func):
    def wrapper(inpt):
        return "\033[4m" + func(inpt) + "\033[0m"
    return wrapper


@underline
@italic
@bold
def userInput(inpt):
    return inpt


print('Podaj wyraz')
inpt = input()
print(userInput(inpt))
