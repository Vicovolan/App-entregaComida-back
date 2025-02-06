import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'ativo' : False}, {'nome': 'Pizzaiola', 'categoria':'Pizza', 'ativo' : True}, 
                {'nome': 'Cantina', 'categoria':'Italiana', 'ativo' : False}]


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
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante: {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print('Restaurante cadastrado com sucesso\n')
    voltar_ao_menu()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(subtitulo)
    print()

def listar_restaurantes():  
    os.system('cls')
    exibir_subtitulo('Listar restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante["nome"]} - {restaurante["categoria"]} - {"Ativo" if restaurante["ativo"] else "Inativo"}')
    print('\n')
    voltar_ao_menu()

def alterar_status_restaurante():
    exibir_subtitulo('Alterar status do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O status do restaurante {restaurante["nome"]} foi alterado para {"ativo" if restaurante["ativo"] else "inativo"}'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_ao_menu()      

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()   
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
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
