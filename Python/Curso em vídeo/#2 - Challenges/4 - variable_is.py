print('===== DESAFIO 4 =====')

value = input('Digite um valor: ')

print('O tipo primitivo desse valor é: ', type(value), '\n')

print('É alfanumérico?', value.isalnum())

print('Está no alfabeto?', value.isalpha())

print('Tem caracteres ASCII?', value.isascii())

print('É um número decimal?', value.isdecimal())

print('É um dígito?', value.isdigit())

# Entender
print('É uma string com identificador?', value.isidentifier())

print('Tem todos os caracteres minúsculos?', value.islower()) 

print('Tem todos os caracteres maiúsculos?', value.isupper())

print('É numérico?', value.isnumeric())

print('É printável?', value.isprintable()) 

print('É um espaço / vazio?', value.isspace()) 

print('É um título (de acordo com as regras)?', value.istitle()) 
