import os


class Patient:

    def __init__(self, name, age, rg, medical_record):
        self.name = name
        self.age = age
        self.rg = rg
        self.medical_record = medical_record
        self.hour_of_visit = ""


class Session:

    def __init__(self, ID, duration, day, month):
        self.duration = duration
        self.day = day
        self.month = month
        self.patients = []
        self.ID = ID
        self.is_active = False

    def add_patient(self, patient):
        self.patients.append(patient)


class Clinica:

    def __init__(self):
        self.sessions = []
        self.patinents = []

    def add_session(self, duration, day, month):
        self.sessions.append({
            'duration': duration,
            'day': day,
            'month': month,
            'patients': []
        })
        return self.sessions


def title():
    # os.system('clear')
    print("-=-" * 20)
    print(" " * 18, "Clinica Dente Clean")
    print("-=-" * 20)
    print("")


def sistema_recepcao():
    reception = Clinica()
    cont = 0
    while True:
        title()
        print(" " * 17, "1 - Cadastrar Paciente")
        print(" " * 17, "2 - Cadastrar Sessão")
        print(" " * 17, "3 - Listar Sessões")
        print(" "*17, "4 - Busar Sessão")
        print(" "*17, "5 - Iniciar Sessão Do Dia")
        print(" "*17, "6 - Marcar Horário Para Paciente")
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
            reception.patinents.append({'Name': name, 'Age': age,
                                        'Rg': rg, 'Medical Record': medical_record})
          #
          # Fazendo função 6, de adicionar paciente em horario marcado.
          # Aqui parei criando uma forma de armazenar os pacientes criados.
          #
            input("Paciente adicionado com sucesso! Pressione [ENTER] para continuar")
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
        elif escolha_opcao == 4:
            title()
            dia_busca_sessao = int(input("Digite a data da sessão: "))
            mes_busca_sessao = int(input("Digite o mês da sessão: "))
            for session_data in reception.sessions:
                if (session_data['day'] == dia_busca_sessao and
                    session_data['month'] == mes_busca_sessao):
                    print(f"Sessão {cont} / ", end="")
                    print(f"Duração: {session_data['duration']}min, ", end="")
                    print(f"Dia:  {session_data['day']}, ", end="")
                    print(f"Mês: {session_data['month']} ")
                    print("")
                    print("Pacientes: ")
                    for patient in session_data['patients']:
                      print(f"Paciente: {patient.name}, ", end="")
                      print(f"Idade: {patient.age}, ", end="")
                      print(f"RG: {patient.rg}, ", end="")
                      print("=-="*5)
        elif escolha_opcao == 5:
            title()
            dia_inicio_sessao = int(input("Digite o dia da sessão: "))
            mes_inicio_sessao = int(input("Digite o mês da sessão: "))
            for session_data in reception.sessions:
                if (session_data['day'] == dia_inicio_sessao and
                    session_data['month'] == mes_inicio_sessao):
                    session_data.is_active = True
            input("Enter")
        elif escolha_opcao == 6:
            title()
            sessao_disponivel = False
            dia_busca_sessao = int(input("Digite o dia da sessão: "))
            mes_busca_sessao = int(input("Digite o mês da sessão"))
            rg_busca = int(input("Digite o RG do paciente: "))
            for session_data in reception.sessions:
              if (session_data['day'] == dia_busca_sessao and
                session_data['month'] == mes_busca_sessao):
                  sessao_disponivel = True
            for i in reception.
                

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
