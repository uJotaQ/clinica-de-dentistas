import os


class Patient:

    def __init__(self, name, age, rg, medical_record):
        self.name = name
        self.age = age
        self.rg = rg
        self.medical_record = medical_record


class Session:

    def __init__(self, duration, day, month):
        self.duration = duration
        self.day = day
        self.month = month
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)


class Clinica:

    def __init__(self):
        self.sessions = []

    def add_session(self, duration, day, month):
        self.sessions.append({
            'duration': duration,
            'day': day,
            'month': month,
            'patients': []
        })
        return self.sessions


def title():
    os.system('cls')
    print("-=-" * 20)
    print(" " * 18, "Clinica Dente Clean")
    print("-=-" * 20)
    print("")


def sistema_recepcao():
    reception = Clinica()
    cont = 0
    while True:
        title()
        print(" " * 17, "1 - Cadastrar paciente")
        print(" " * 17, "2 - Cadastrar sessão")
        print(" " * 17, "3 - Listar sessões")
        print("")
        print(" " * 18, end="")
        escolha_opcao = int(input("Escolha uma opção: "))
        if escolha_opcao == 1:
            title()
            name = input("Digite o nome do paciente: ")
            age = int(input("Digite a idade do paciente: "))
            rg = int(input("Digite o RG do paciente: "))
            medical_record = []
            patient = Patient(name, age, rg, medical_record)
        elif escolha_opcao == 2:
            title()
            duracao = int(input("Digite a duração da sessão (minutos): "))
            dia = int(input("Digite o dia da sessão: "))
            mes = int(input("Digite o mês da sessão: "))
            session_data = reception.add_session(duracao, dia, mes)
            input("Sessão adicionada com sucesso! Pressione"
                  " [ENTER] para continuar.")
        elif escolha_opcao == 3:
            # Para acessar as sessões dentro da instância da classe Clinica
            title()
            print("Sessões Cadastradas:")
            print("")
            for session_data in reception.sessions:
                cont += 1
                print(f"Sessão {cont} / ", end="")
                print(f"Duração: {session_data['duration']}min,"
                      f" Dia:  {session_data['day']},"
                      F" Mês: {session_data['month']}")
                for patient in session_data['patients']:
                    print(f"Paciente: {patient.name}")
            input("Pressione [ENTER] para continuar")


# Criando instâncias de pacientes
patient1 = Patient("João", 18, 2248930329, [])
patient2 = Patient("Maria", 30, 84347589, [])

# Criando instância da recepção

# Adicionando sessões à recepção

# Adicionando pacientes às sessões

# Acessando informações

title()
print(" " * 20, "1. Recepção")
print(" " * 20, "2. Dentista")
print("")
print(" " * 12, end="")
escolha = int(input("Qual sistema deseja acessar? "))
if escolha == 1:
    sistema_recepcao()
