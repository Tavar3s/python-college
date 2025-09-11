import matplotlib.pyplot as plt

# Criando os dados para x e y
# x vai de 0 a 10
x = list(range(11))
# y é igual a x
y = x

# Criando o gráfico
plt.plot(x, y)

# Adicionando um título e rótulos aos eixos
plt.title("Função y = x")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Definindo a grade de x e y entre 0 e 10
plt.xlim(0, 10)
plt.ylim(0, 10)

# Adicionando a grade visual ao gráfico
plt.grid(True)

# Assegurando que a proporção dos eixos seja a mesma
plt.gca().set_aspect('equal', adjustable='box')

# Salvando a imagem do gráfico
plt.savefig('funcao_y_igual_x.png')