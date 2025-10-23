from numpy import arange

def raiz_quadrada(num):
    valor_anterior = 0
    interacoes = 0
    while True:
        if interacoes == 0:
            tempvalor = num/2
        else:
            tempvalor = 0.5 * (valor_anterior + num/valor_anterior)

        if abs(tempvalor - valor_anterior) > 0.000001:
            valor_anterior = tempvalor
            interacoes += 1
        else:
            break

    saida = [valor_anterior, interacoes]
    return saida

def integral(a, b, h):
    integral = 0
    for x in arange(a, b, h):
        integral += (1 / (1 + x**2) + 1 / (1 + (x+h)**2))/2 * h
    return integral

print(raiz_quadrada(int(input("Digite um valor: "))))
print(integral(0, 1, 1/10))