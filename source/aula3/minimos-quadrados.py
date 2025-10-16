import matplotlib.pyplot as plt
import numpy as np

def soma_comum(x, n):
    soma = 0
    for i in range(n):
        soma += x[i]
    return soma

def soma_produto(x, y, n):
    soma = 0
    for i in range(n):
        soma += x[i]*y[i]
    return soma

def soma_quadrado(x, n):
    soma = 0
    for i in range(n):
        soma += x[i]**2
    return soma


lista_x_entrada = list()
lista_y_entrada = list()
n = 0
continuar = ''

while continuar != "N":
    try:
        lista_x_entrada.append(float(input('Digite o valor de x: ')))
        lista_y_entrada.append(float(input("Digite o valor de y: ")))
        continuar = input("Quer continuar? [Y/N]: ").upper()
        n += 1
    except TypeError:
        print("Não foi inserido um valor real")

lista_x = np.array(lista_x_entrada)
lista_y = np.array(lista_y_entrada)

soma_x = soma_comum(lista_x, n)
soma_y = soma_comum(lista_y, n)
soma_xy = soma_produto(lista_x, lista_y, n)
soma_x2 = soma_quadrado(lista_x, n)

a = (n*soma_xy - soma_x*soma_y)/(n*soma_x2 - soma_x**2)
b = (soma_y*soma_x2 - soma_x* soma_xy) / (n*soma_x2 -soma_x**2)


y = a*lista_x + b

plt.figure(figsize=(4, 3))

# Inserir valores e função
plt.plot(lista_x, y, 'b-', label='vx(x)')
for i in range(n):
    plt.plot(lista_x[i], lista_y[i], color="#FF0000", marker='.', ms='10')

# Título
plt.title("Valores de y contra x")

# Definindo domínio limitante
plt.xlim(lista_x[0], lista_x[n-1])
plt.ylim(lista_y[0], lista_y[n-1])

# Configurações e execução
plt.grid(True)
plt.tight_layout()
plt.savefig('../../png/minimoquad.png')
plt.show()

