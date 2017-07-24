# Importa o módulo sys
import sys


# Checa se foi passado exatamente 1 argumento
if len(sys.argv) != 2:
    print("\nPara usar esse programa, digite\n$ python argumento.py <número>")
    exit()

# Checa se o arguemento é um número
try:
    num = float(sys.argv[1])
except Exception:
    print("\nO argumento tem que ser um número (0, 1.10, 15.5, 100, ...)")
    exit()

print("\n{}ºC é equivalente a {}ºF e {}ºK".format(num, num * 9 / 5 + 32, num + 273.15))
