from math import *

def newton(f, p0, epsilon):
    i =  1
    N = int(input('\nDigite o número máximo de iterações: '))
    while(i <= N):
        p = p0 - f(p0) / derivada(p0)
        
        if(abs(p - p0) < epsilon):
            print ('O valor da raiz é: ', p)
            print('Número de iterações : ', i)
            return p

        else:
            i += 1
            p0 = p

    print ('O método falhou após %s iterações' % (i))
    return -1

def f(x):
    return x**3 + (4* (x**2)) - 10
 
def derivada(x):
    return 2* (x**2) + 8*x


newton(f, 0.5, 0.0001)



