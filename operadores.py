a = 3
b = -4

soma = a + b
sub = a - b
mult = a * b
div = a / b

print("Soma: ", soma)
print("Subtração :", sub)
print("Multiplicação: ", mult)
print("Divisão: ", div)
print("Cálculos dentro do print: ", ( a * b ))
print("Resto da divisão de 11 por a: ", ( 11 % a ))

print("a == b:", ( a == b) )
print("a < 5:", ( a < 5) )
print("a > b:", ( a > b) )
print("a <= 3:", ( a <= 3) )
print("a >= 4:", ( a >= 4) )
print("a != b:", ( a != b) )

# comentário simples
if ( (a > 0) & (b > 0) ):
    print("entao")
else:
    print("senao")

print("Testando", "a função", "print()", sep="-", end="@@@")


logic1 = True
logic2 = False
print(type(logic1))
print(logic1)
print(not logic1)
print(logic1 or logic2)
print(logic1 and logic2)


valor = 1200.00
print("Valor: " + str(valor))
