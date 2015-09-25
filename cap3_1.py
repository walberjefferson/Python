imposto = 0.27
salario = 3000

print("Valor real: {0}\n".format(salario - (salario * imposto)))

salario2 = int(input('Salario? '))
imposto2 = input('Imposto em % (ex: 27.5)? ')
if not imposto2 :
    imposto2 = 27.5
else :
    imposto2 = float(imposto2)

print("Valor real: {0}".format(salario2 - (salario2 * (imposto2 * 0.01))))
