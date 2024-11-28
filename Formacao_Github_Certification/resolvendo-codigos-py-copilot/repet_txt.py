# Solicita uma string e um número inteiro como entrada
string_input = input("Digite uma string: ")
numero_input = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado, com separação entre os resultados
resultado = (string_input + " ") * numero_input
print(resultado.strip())