import matplotlib.pyplot as plt
from numpy import arange

def integral(a, b, h):
    integral = 0
    for x in arange(a, b, h):
        integral += (1 / (1 + x**2) + 1 / (1 + (x+h)**2))/2 * h
    return integral

a = 0
b = 1

x = [1, 0.1, 0.001, 0.0001]
z = list()

for i in x:
    z.append(4*integral(a, b, i))

# Define dimensão da figura
plt.figure(figsize=(4, 3))

# Inserir valores e função
plt.plot(x, z, marker='o', label='vx(x)')

# Título
plt.title("Valores de z contra h")

# Definindo domínio limitante
plt.xscale('log')
plt.xlim(0.0001, 0.1)
plt.ylim(3, 3.2)

# Configurações e execução
plt.grid(True)
plt.tight_layout()
plt.savefig('../../png/integral.png')
plt.show()