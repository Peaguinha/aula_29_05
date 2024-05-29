pacientes = {}
medicos = {}

def adicionar_paciente():
    cpf = input("Digite o cpf do paciente: ")
    if cpf in pacientes:
        print("Paciente já cadastrado.")
        return
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    

    pacientes[cpf] = {
        'nome': nome,
        'idade': idade,
        'endereco': endereco,
        'telefone': telefone
    }
    print("Novo paciente cadastrado!")

def adicionar_medico():
    crm = input("Digite o CRM do médico: ")
    if crm in medicos:
        print("Operação falhou: Médico já cadastrado.")
        return
    nome = input("Digite o nome do médico: ")
    especialidade = input("Digite a especialidade do médico: ")
    telefone = input("Digite o telefone do médico: ")
    
    
    medicos[crm] = {
        'nome': nome,
        'especialidade': especialidade,
        'telefone': telefone
    }
    print("Novo médico cadastrado!")

def pesquisar_paciente():
    cpf = input("Digite o CPF do paciente: ")
    if cpf in pacientes:
        paciente = pacientes[cpf]
        print(f"Nome: {paciente['nome']}, Idade: {paciente['idade']}, Endereço: {paciente['endereco']}, Telefone: {paciente['telefone']}")
    else:
        print("Paciente não encontrado ")

def pesquisar_medico():
    crm = input("Digite o CRM do médico ")
    if crm in medicos:
        medico = medicos[crm]
        print(f"Nome: {medico['nome']}, Especialidade: {medico['especialidade']}, Telefone: {medico['telefone']}")
    else:
        print(" Médico não encontrado")

def excluir_paciente():
    cpf = input("Digite o CPF do paciente a ser excluído: ")
    if cpf in pacientes:
        del pacientes[cpf]
        print("Paciente excluido")
    else:
        print("Paciente não encontrado")

def excluir_medico():
    crm = input("Digite o CRM do médico a ser excluído: ")
    if crm in medicos:
        del medicos[crm]
        print("Medico excluido")
    else:
        print("Medico não encontrado")

def sair():
    print("Obrigado!")
    return False

def menu():
    ativo = True
    while ativo:
        print("\nMenu do sistema")
        print("1. Adicionar novo Paciente")
        print("2. Adicionar novo Médico")
        print("3. Pesquisar paciente por CPF")
        print("4. Pesquisar medico por CRM")
        print("5. Excluir paciente pelo CPF")
        print("6. Excluir medico pelo CRM")
        print("7. Sair do sistema")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            adicionar_paciente()
        elif opcao == '2':
            adicionar_medico()
        elif opcao == '3':
            pesquisar_paciente()
        elif opcao == '4':
            pesquisar_medico()
        elif opcao == '5':
            excluir_paciente()
        elif opcao == '6':
            excluir_medico()
        elif opcao == '7':
            ativo = sair()
        else:
            print("Opcao invalida")

menu()


"""
    Trabalho desenvolvido por:
Marcos Marinho Falcão Segundo
Pedro Henrique de Almeida Peixoto
Pedro Lira Bandeira
Emanuel Albuquerque Sousa
Washingtton Lucena
Higor Miguel Nascimento Coutinho 

"""