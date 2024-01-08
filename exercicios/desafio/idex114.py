import urllib.request

try:
    site = urllib.request.urlopen('https://maurici0123.github.io/html-css/')
except:
    print('o site não está acessível')
else:
    print('o site está funcionando')