import os, time

# Funções de exibição
def show_options():
    print('[1] - Tipos existentes')
    print('[2] - Exemplos de cada tipo')
    print('[3] - Observações')
    print('[4] - Verificar tipo')
    print('[0] - Para encerrar programa \n')

def show_type_options():
    print('[1] - número INTEIRO')
    print('[2] - número REAL')
    print('[3] - número BOOLEANO / lógico')
    print('[4] - SEQUÊNCIA de caracteres')
    print('[0] - VOLTAR \n')

def show_types():
    print('int: número inteiro')
    print('float: número real / ponto flutuante')
    print('bool: boolean, booleano / lógico verdadeiro') 
    print('str: string, sequência de caracteres \n')

def show_examples():
    print('int: 1, 5, 2, 9')
    print('float: 2.5, 1.9, 3.6, 3.141516')
    print('bool: True, False')
    print('str: palavra, uma_frase, 56, true \n')

# Funções de atualização
def update_slow():
    time.sleep(10)
    os.system('clear')

def update_fast():
    time.sleep(1)
    os.system('clear')

print('##### TIPOS PRIMITIVOS ##### \n')

show_options()

option = input('Escolha uma opção: ')

update_fast()

# Melhorar match case para evitar duplicação [OK!]
# Criar funções específicas [OK!]
# Existe um do while em python?

while (option):
    match (int(option)):
        case 1:
            update_fast()
            show_types()
            update_slow()
            show_options()
            option = input('Escolha uma opção: ')
        case 2:
            update_fast()
            show_examples()
            update_slow()
            show_options()
            option = input('Escolha uma opção: ')
        case 3:
            update_fast()
            print('OBS 1: Concatenação ("1" + "5" = "15") ≠ Adição (1 + 5 = 6)')
            print('OBS 2: 7 (int) ≠ 7.0 (float)')
            print('OBS 3: 5 (int) ≠ "5" (string)')
            update_slow()
            show_options()
            option = input('Escolha uma opção: ')
        case 4:
            update_fast()
            show_type_options()
            type_option = input('Escolha uma opção: ')
            os.system('clear')
            match (int(type_option)):                    
                 # Aprimorar int para checagem de valores válidos
                case 1:
                    value = input('Digite um valor inteiro: ')
                    if value.isnumeric():
                        print('O valor é do tipo:', type(value))
                    else:
                        value = input('O valor não é inteiro! Digite um valor inteiro: ')
                    update_fast()
                # Aprimorar float para checagem de valores válidos
                case 2:
                    value = float(input('Digite um valor real / ponto flutuante: '))
                    print('O valor é do tipo:', type(value))
                    update_fast()
                # Aprimorar bool para checagem de valores válidos
                case 3:
                    value = bool(input('Digite um valor booleano: '))
                    print('O valor é do tipo:', type(value))
                    update_fast()
                case 4:
                    value = input('Digite um valor de string: ')
                    print('O valor é do tipo:', type(value))
                    update_fast()
                case 0:
                    update_fast()
                    show_options()
                    option = input('Escolha uma opção: ')
                case _:
                    print('Opção inválida, selecione outra!')
                    update_fast()
                    show_type_options()
                    type_option = input('Escolha uma opção: ')
        case 0:
            print('Programa encerrado! \n')
            exit()
        case _:
            print('Opção inválida, selecione outra!')
            update_fast()
            show_options()
            option = input('Escolha uma opção: ')
            os.system('clear')
