import os

restaurantes = ['Pizza, Burguer, Massa']

def exibir_nome_programa():
    print('Sabor express\n')
def exibir_opcoes(): 
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # s.system('clear') no mac
    print('Finalizando o app')

def voltar_ao_menu():
    input("Digite uma tecla para voltar ao menu principal")
    main()

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print('Restaurante cadastrado com sucesso\n')
    voltar_ao_menu()

def listar_restaurantes():  
    os.system('cls')
    print('Listar restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante }')
    print('\n')
    voltar_ao_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()   
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()        

if __name__ == '__main__':
    main()
