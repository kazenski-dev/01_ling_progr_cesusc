#Trabalhando na linha 64


from person import Pessoa

class Interface:

    lista_principal = []

    
    def listar_pessoa(self):
        print("Comando de listar pessoa escolhida.\n")

        while True:
            busca_usuario = input("\nInsira o nome, cpf ou email da pessoa para realizar a busca detalhada.\nOu numero ZERO para voltao ao menu principal:\n")
            if busca_usuario == 0:
                loop()
            else:
                for valor1 in lista_principal:
                    if busca_usuario in valor1 and valor1[3] == 1:
                        try:
                            print("Nome: %s - CPF: %d - Email: %s\n"%(valor[0],valor[1],valor[2]))
                        except(ValueError):
                            print("Cadastro nao localizado.\n")
                            break
                        listar_pessoa()
        return valor1

    def cadastrar_pessoa(self):
        print("Comando de cadastrar pessoa escolhida.\n")

        nova_lista = []

        nome_pessoa = input('Qual é o nome da pessoa?\n')
        nome_pessoa.upper
        cpf_pessoa = int(input('Qual é o cpf da pessoa?\n'))
        email_pessoa = input('Qual é o email da pessoa?\n')
        email_pessoa.upper
        atividade = 1

        print('\n\nEfetuando novo Cadastro...\n')

        nova_lista.append(nome_pessoa)
        nova_lista.append(cpf_pessoa)
        nova_lista.append(email_pessoa)
        nova_lista.append(atividade)

        lista_principal.append(nova_lista) #Adiciona a lista criada com o cadastro da pessoa dentro da lista

        print('\nPessoa cadastrada com sucesso!\n')

    def alterar_pessoa(self):
        print("Comando de alterar pessoa escolhida.\n")

        pessoa_cadastro = listar_pessoa() #gera um vetor do cadastro buscado 'apenas'

        print("Menu de Alteracao de Cadastro:")
        print("1 - Para alterar o nome.\n")
        print("2 - Para alterar o CPF.\n")
        print("3 - Para alterar o email.\n")
        print("0 - Para voltar ao menu principal.\n")

        captura_opcao = int(input(": "))
        try:
            if captura_opcao == 1:
                pessoa_cadastro[0] = input("Insira o novo nome: ")
#ATUALMENTE AQUI #########################################
                pass
            elif captura_opcao == 2:
                pass
            elif captura_opcao == 3:
                pass
            elif captura_opcao == 0:
                pass
        except(ValueError):
            print("Opcao invalida, favor insira novamente.")

    def excluir_pessoa(self):
        #buscar a pessoa nos cadastros e apenas alterar o atributo 'atividade' para 0.
        print("Comando de excluir pessoa escolhida.\n")
        pass

    def loop(self):
        while True:
            opcao = input('\n1 - Listar cadastros\n2 - Cadastrar pessoa\n3 - Alterar cadastro\n4 - Excluir cadastro\n5 - SAIR')
            if opcao == '1':
                self.listar_pessoa()
            elif opcao == '2':
                self.cadastrar_pessoa()
            elif opcao == '3':
                self.alterar_pessoa()
            elif opcao == '4':
                self.excluir_pessoa()
            elif opcao == '5':
                break
            else:
                print('Valor não encontrado.\nFavor insira uma opcao valida: ')
                continue
