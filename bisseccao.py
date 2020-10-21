def bissecao(f, a, b, epsilon, N):  
    i = 1  
    funcA = f(a)
    while (i <= N):  
        
        pm = a + (b - a) / 2
        funcP = f(pm)

        if( funcP == 0 or (b - a) / 2 < epsilon):
            print('A raíz é: ', pm) 
            break

        i+=1
        if ((funcA * funcP) > 0 ):
            a = pm 
            funcA = funcP
        
        else:
            b = pm
        


def f(x):
  return (x**3) + 4*(x**2) - 10

bissecao(f, 1, 2, 0.1, 10)





