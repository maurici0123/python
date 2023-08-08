x = float(input('digite sua primaira nota: '))
y = float(input('digite sua segunda nota: '))
m = (y+x)/2

print('sua media foi {:.2f}'.format(m))
if m >= 6:
    print('parabens!')
else:
    print('melhore')