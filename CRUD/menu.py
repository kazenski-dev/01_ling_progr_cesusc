from person import Pessoa

class Interface:
    """
    def busca_padrao(self):
        while True:
            print("COmando de buscar pessoa escolhido.")
            #busca_usuario = input("\nInsira o nome, cpf ou email da pessoa para realizar a busca detalhada...\n")
            #busco o cadastro e pergunto se este cadastro mostrado eh o que o usuario deseja ver
            #em seguida mostro o menu novamente
            pass
    """
    def listar_pessoa(self):
        print("COmando de listar pessoa escolhido.")
        pass

    def cadastrar_pessoa(self):
        print("COmando de cadastrar pessoa escolhido.")

        nome_pessoa = input('Qual é o nome da pessoa?\n')
        nome_pessoa.upper
        cpf_pessoa = input('Qual é o cpf da pessoa?\n')
        cpf_pessoa.upper
        email_pessoa = input('Qual é o email da pessoa?\n')
        email_pessoa.upper
        atividade = 1

        print('\n\nEfetuando novo Cadastro...\n')

        cad_pessoa = {}

        cadastro_novo = Pessoa(nome_pessoa, cpf_pessoa, email_pessoa, atividade)
        cad_pessoa.update(cadastro_novo)
        print(cad_pessoa)

        append_dic_on_list(cad_pessoa)

        def append_dic_on_list(self, dicionario):
            pessoas = []
            pessoas.append(dicionario)

        print('\nPessoa cadastrada com sucesso!\n')

    def alterar_pessoa(self):
        print("COmando de alterar pessoa escolhido.")
        pass

    def excluir_pessoa(self):
        #buscar a pessoa nos cadastros e apenas alterar o atributo 'atividade' para 0.
        print("COmando de excluir pessoa escolhido.")
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
