from numpy import arange

class Calculo:
    def __init__(self, num_raiz):
        self.num = num_raiz

    def integral(self, a, b, h):
        integral = 0
        for x in arange(a, b, 1/h):
            integral += (1 / (1 + x ** 2) + 1 / (1 + (x + 1/h) ** 2)) / 2 * 1/h
        return 4 * integral

    def raiz_quadrada(self):
        valor_anterior = 0
        interacoes = 0
        while True:
            if interacoes == 0:
                tempvalor = self.num / 2
            else:
                tempvalor = 0.5 * (valor_anterior + self.num / valor_anterior)

            if abs(tempvalor - valor_anterior) > 0.000001:
                valor_anterior = tempvalor
                interacoes += 1
            else:
                break

        saida = [valor_anterior, interacoes]
        return saida


calc1 = Calculo(88)
calc2 = Calculo(10050.66)
calc3 = Calculo(2)
calc4 = Calculo(2)
calc5 = Calculo(2)

print(30*"-=")

print(f"{calc1.integral(0,1,1):.5f} (h=1)")
print(f"{calc2.integral(0,1,10):.5f} (h=10)")
print(f"{calc3.integral(0,1,100):.5f} (h=100)")
print(f"{calc4.integral(0,1,200):.5f} (h=200)")
print(f"{calc5.integral(0,1,500):.5f} (h=500)")

print(30*"-=")

print(f"Valor da raíz de 88: {calc1.raiz_quadrada()[0]:.2f}")
print(f"Número de interações: {calc1.raiz_quadrada()[1]}")
print(f"Valor da raíz de 10050.66: {calc2.raiz_quadrada()[0]:.2f}")
print(f"Número de interações: {calc2.raiz_quadrada()[1]}")

print(30*"-=")