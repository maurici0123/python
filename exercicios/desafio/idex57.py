s=''
while s!='m' and s!='f':
    s=input('qual seu sexo [F/M]: ').lower()
    if s!='m' and s!='f':
        print('é apenas F ou M')