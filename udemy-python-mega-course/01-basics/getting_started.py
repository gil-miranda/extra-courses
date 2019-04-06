def bissection_step(f, a, b):
    if (f(a)*f(b)) > 0:
        print('ERRO! O dado intervalo [' + str(a)+','+str(b)+'] não contém uma raíz.')
        return (a,b)
    else:
        m = (a+b)/2
        if(f(m) == 0):
            return (m,m)
        elif (f(a)*f(m) < 0):
            return (a,m)
        elif (f(m)*f(b) < 0):
            return (m,b)
def bissecao(f,a,b,tol=1e-8,count=0,retsteps=False):
    if (abs(b-a) <= tol):
        if (f((b+a)/2)) < f(b) and f((b+a)/2) < f(a):
            if (retsteps):
                return ((b+a)/2,count)
            else:
                return (b+a)/2
        elif (f(b)<f(a)):
            if (retsteps):
                return (b,count)
            else:
                return b
        else:
            if (retsteps):
                return (a,count)
            else:
                return a
    else:
        a, b = bissection_step(f, a, b)
        count += 1
    return bissecao(f, a, b, tol, count, retsteps)







    def bissection_step(f, a, b):
    m = (a+b)/2
    if(f(m) == 0):
        return (m,m)
    elif (f(a)*f(m) < 0):
        return (a,m)
    else:
        return (m,b)

def bissecao(f,a,b,tol=1e-8,count=0,retsteps=False):
    if (abs(b-a) <= tol):
        if (retsteps):
            return ((b+a)/2,count)
        else:
            return (b+a)/2
    else:
        a, b = bissection_step(f, a, b)
        count += 1
    return bissecao(f, a, b, tol, count, retsteps)









def bissecao_step_z(f,a,b):
    'Bissecao dado os extremos.'
    z = (a+b)//2
    if f(z)!=0:
        if f(a)*f(z)<0:
            return (a,z)
        else:
            return (z,b)
    return (z,z)
def bissection_z(f,a,b):
    while abs(b-a)>=0:
        a,b = bissecao_step_z(f,a,b)
    return (a+b)//2

def bissecao(f,a,b, tol=1e-8):
    # YOUR CODE HERE
    cont = 0
    while b-a >= tol:
        count += 1
        z = (a+b)/2
        if f(z) == 0:
            return z, count
        if f(a)*f(z) < 0:
            b = z
        else:
            a = z
    return z, count
