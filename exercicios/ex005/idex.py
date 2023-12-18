print('hello\033[1;31;107m world! \033[m')
print()

name = 'mau'
print('o meu nome é {}{}{}'.format('\033[;32m', name, '\033[m'))
print()

none = '\033[m'

style = {
    'none': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'negative': '\033[7m'
}

text = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'gray': '\033[37m',
    'white': '\033[97m'
}

background = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'gray': '\033[47m',
    'white': '\033[107m'
}

print('embora os {}sábios{} no fim da {}vida{} saibam que é a {}treva{} que perdura'.format(style['underline'], none, text['magenta'], none, background['red'], none))