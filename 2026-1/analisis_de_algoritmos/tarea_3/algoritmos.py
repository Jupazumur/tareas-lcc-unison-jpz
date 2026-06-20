# TODO: Agregar los de polinomio grado n o aquí o en su propio archivo

# SUM
def sum(a,n):
    s = 0
    for i in range(1, n+1):
        s = s + a[i]
    
    return s

# RSUM
def r_sum(a,n):
    if n <= 0:
        return 0
    else:
        return r_sum(a, n-1) + a[n]

# ADD
def add(a, b, c, m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            c[i][j] = a[i][j] + b[i][j]
    
    return c[i][j]

# FIBONACCI
def fibonacci(n):
    if n <= 1:
        return n
    else:
        fnm2 = 0
        fnm1 = 1
        for _ in range(2, n+1):
            fn = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = fn
        return fn

# TRASPUESTA
def trasp(a, n):
    for i in range(1, n):
        for j in range(i+1, n+1):
            t = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = t
    return t

# MULTIPLICACIÓN
def mult(a, b, c, m, n, p):
    for i in range(1, m+1):
        for j in range(1, p+1):
            c[i][j] = 0
            for k in range(1, n+1):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]

    return c[i][j]

# MULTIPLICACIÓN 2
def mult(a, b, c, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            c[i][j] = 0
            for k in range(1, n+1):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    
    return c[i][j]

# PERMUTACIONES
def perm(a, k, n):
    if (k == n):
        print(a[1:n])
    else:
        for i in range(k, n+1):
            t = a[k]
            a[k] = a[i]
            a[i] = t
            perm(a, k + 1, n)
            t = a[k]
            a[k] = a[i]
            a[i] = t

# BÚSQUEDA SECUENCIAL
def seqsearch(a, x, n):
    i = n
    a[0] = x

    while (a[i] != x):
        i -= 1
    
    return i