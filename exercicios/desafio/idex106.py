from time import sleep

def ajuda(com):
    sleep(.5)
    t=f'  acessando o manual do código {com}  '
    print('-'*len(t))
    print(t)
    print('-'*len(t))
    help(com)
    sleep(1)

def titulo(msg):
    tam=len(msg)
    print('~'*(tam+4))
    print(f'  {msg}  ')
    print('~'*(tam+4))


comando=''
while True:
    titulo('SISTEMA DE AJUDAPyHELP')
    comando=str(input('função ou biblioteca: '))
    if comando.lower()=='fim':
        break
    else:
        ajuda(comando)

titulo('ate logo')