valor1 = 8.79
valor2 = 3932.6
valor3 = 11.349

# formatação apenas como valor float
print("Valor 1: {:f}".format(valor1))

# formatação float e com decimal em 2 dígitos
print("Valor 1: {:.2f}".format(valor1))
print("Valor 2: {:.2f}".format(valor2))
print("Valor 3: {:.2f}".format(valor3))

# formatação float, com total de dígitos 7 (números e ponto), sendo 2 decimais.
print("Valor 1: {:7.2f}".format(valor1))
print("Valor 2: {:7.2f}".format(valor2))
print("Valor 3: {:7.2f}".format(valor3))

# semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessário
print("Valor 1: {:07.2f}".format(valor1))
print("Valor 2: {:07.2f}".format(valor2))
print("Valor 3: {:07.2f}".format(valor3))