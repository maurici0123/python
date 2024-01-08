#help()
help(print)

help(input.__doc__)

a=7
def fun(x, y, z=1):
    """
    -> contador
    x = inicio
    y = final
    z = passo a passo
    """
    global a
    a=9
    print(a)
    
    for c in range(x, y ,z):
        print(c)

fun(0, 2)
print(a)
help(fun)