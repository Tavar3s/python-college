def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n-1)

def sin(x, n):
    seno = 0
    for i in range(n):
       seno = seno + ((-1)**i / fatorial(2*i + 1)) * (x ** (2*i+1))
    return seno


print(sin(float(input("Valor do Ângulo (Radianos):")), 50))
