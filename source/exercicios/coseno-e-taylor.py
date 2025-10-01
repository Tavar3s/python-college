from math import pi

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def cosseno(rad):
    cos = 0
    for i in range(50):
        cos = cos + (-1)**i / fact(2*i) * rad**(2*i)
    return cos


l = 5
c = 1
v0 = 15
valores_x = [0, l/2, l, 3*l/2, 2*l]

for k, i in enumerate(valores_x):
    vx = v0 * (1 + ((c * pi / l) ** 2) * (cosseno(i * pi / l) ** 2)) ** (-1 / 2)
    vy = v0 * c * pi / l * cosseno(i * pi / l) * (1 + ((c * pi / l) ** 2) * (cosseno(i * pi / l) ** 2)) ** (-1 / 2)

    print(f"Para o {k+1}º de x: vx = {vx:.2f} e vy = {vy:.2f}")