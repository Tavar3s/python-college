import matplotlib.pyplot as plt

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
        soma = x[i]**2
    return soma

lista_x = [1, 2, 3, 4]
lista_y = [1.5, 3.1, 4.3, 6.2 ]
n = 4

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

# Título
plt.title("Valores de y contra x")

# Definindo domínio limitante
plt.xlim(0, 5)
plt.ylim(0, 7)

# Configurações e execução
plt.grid(True)
plt.tight_layout()
plt.savefig('../../png/minimoquad.png')
plt.show()

