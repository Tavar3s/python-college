import matplotlib.pyplot as plt
from numpy import cos, arange
from math import pi

# Definindo cosntantes
v0 = 15
c = 1
long = 5

# Domínio de análise da função
x = arange(0, 2*long+1, .1)

# Funções da velocidade em x e y
vx = v0 * (1 + ((c*pi/long)**2) * (cos(x*pi/long)**2))**(-1/2)
vy = v0*c*pi/long * cos(x*pi/long) * (1+((c*pi/long)**2)*(cos(x*pi/long)**2))**(-1/2)

# Define dimensão da figura
plt.figure(figsize=(4, 3))

# Inserir valores e função
plt.plot(x, vx, 'b-', label='vx(x)')
plt.plot(x, vy, 'c-', label='vy(x)')

# Título
plt.title("Função da velocidade em x")

# Definindo domínio limitante
plt.xlim(0, 2*long)

# Configurações e execução
plt.grid(True)
plt.tight_layout()
plt.savefig('../../png/grafico.png')
plt.show()
