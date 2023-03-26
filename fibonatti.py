#entrando com o valor a ser testado:
numero_teste = int( input("\nDigite um numero: "))

#inicializando uma lista de numeros da sequencia de fibbonatti
#usando o numero como tamanho por margem de seguranca
lista_fib = [0,1,1]

for numero in range(1,numero_teste):
    lista_fib.append(lista_fib[numero+1]+lista_fib[numero])


if numero_teste in lista_fib:
    print("Esse numero pertence a sequencia de fibbonatti.")
else:
    print("Esse numero nao pertence a sequencia de fibbonatti.")

