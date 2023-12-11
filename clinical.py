class Patient:
    def __init__(self, name, age, rg, medical_record):
        self.name = name
        self.age = age
        self.rg = rg
        self.medical_record = medical_record
        self.horarios = []


class Session:
    def __init__(self, duration, day, month):
        self.duration = duration
        self.day = day
        self.month = month
        self.patients = []
        self.is_active = False

    def add_patient(self, patient):
        self.patients.append(patient)


class Clinica:
    def __init__(self):
        self.sessions = []
        self.patients = []

    def add_patient(self, name, age, rg, medical_record):
        patient = Patient(name, age, rg, medical_record)
        self.patients.append(patient)
        return patient

    def add_session(self, duration, day, month):
        session = Session(duration, day, month)
        self.sessions.append(session)
        return session

    def add_patient_to_session(self, session, patient):
        session.add_patient(patient)


def title():
    print("-=-" * 20)
    print(" " * 18, "Clinica Dente Clean")
    print("-=-" * 20)
    print("")


def sistema_recepcao():
    reception = Clinica()
    while True:
        title()
        print(" " * 17, "1 - Cadastrar Paciente")
        print(" " * 17, "2 - Cadastrar Sessão")
        print(" " * 17, "3 - Listar Sessões")
        print(" " * 17, "4 - Buscar Sessão")
        print(" " * 17, "5 - Iniciar Sessão Do Dia")
        print(" " * 17, "6 - Marcar Horário Para Paciente")
        print(" " * 17, "7 - Listar Horários De Um Paciente")
        print("")
        print(" " * 18, end="")
        escolha_opcao = int(input("Escolha uma opção: "))

        if escolha_opcao == 1:
            title()
            can_add = True
            name = input("Digite o nome completo do paciente: ")
            age = int(input("Digite a idade do paciente: "))
            rg = int(input("Digite o RG do paciente: "))
            medical_record = []

            for patient in reception.patients:
                if patient.rg == rg:
                    print("Esse RG já está cadastrado!")
                    can_add = False
                    break

            if can_add:
                reception.add_patient(name, age, rg, medical_record)
                print("Paciente cadastrado com sucesso!\n")
            input("[!] Pressione ENTER para continuar")

        elif escolha_opcao == 2:
            title()
            can_add = True
            duration = int(input("Digite a duração da sessão (minutos): "))
            day = int(input("Digite o dia da sessão: "))
            month = int(input("Digite o mês da sessão: "))

            for session in reception.sessions:
                if session.day == day and session.month == month:
                    print("Já existe uma sessão nessa data!")
                    input("[!] Pressione ENTER para continuar")
                    can_add = False
                    break

            if can_add:
                reception.add_session(duration, day, month)
                print()
                print("[!] Sessão adicionada com sucesso!")
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 3:
            title()
            print("Sessões Cadastradas:")
            for session_data in reception.sessions:
                print()
                print(f"Duração: {session_data.duration}min,"
                      f"Dia: {session_data.day}, Mês: {session_data.month}")
                for patient in session_data.patients:
                    print(f"|-> Paciente: {patient.name}")
            print()
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 4:
            title()
            dia_busca_sessao = int(input("Digite o dia da sessão: "))
            mes_busca_sessao = int(input("Digite o mês da sessão: "))
            print()
            if reception.sessions != []:
                for session_data in reception.sessions:
                    contador = 0
                    contador = +1
                    if (session_data.day == dia_busca_sessao
                            and session_data.month == mes_busca_sessao):
                        print(" " * 13, f"Sessão {contador}")
                        print(f"Duração: {session_data.duration}min,"
                              f"Dia: {session_data.day},"
                              f" Mês: {session_data.month}")
                        if session_data.patients != []:
                            print("-> Pacientes: ")
                            for patient in session_data.patients:
                                print(f"[#] Paciente: {patient.name},"
                                      f" Idade: {patient.age},"
                                      f" RG: {patient.rg}")
                                print("=-=" * 5)
            else:
                print()
                print("[!] Não há sessões cadastradas!")
            print()
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 5:
            title()
            dia_inicio_sessao = int(input("Digite o dia da sessão: "))
            mes_inicio_sessao = int(input("Digite o mês da sessão: "))
            print()
            for session_data in reception.sessions:
                if (session_data.day == dia_inicio_sessao
                        and session_data.month == mes_inicio_sessao
                        and session_data.is_active is False):
                    session_data.is_active = True
                    print("[!] Sessão iniciada com sucesso!")
                else:
                    print("[!] Sessão já iniciada ou não existe!")
            print()
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 6:
            title()
            dia_busca_sessao = int(input("Digite o dia da sessão: "))
            mes_busca_sessao = int(input("Digite o mês da sessão: "))

            session_disponivel = None
            selected_session = None

            for session in reception.sessions:
                print()
                print(f"Sessão -> Dia: {session.day}, Mês: {session.month}")
                if (session.day == dia_busca_sessao and
                   session.month == mes_busca_sessao):
                    session_disponivel = True
                    selected_session = session
                    break

            if session_disponivel:
                if reception.patients:
                    print()
                    print("Lista de Pacientes:")
                    for patient in reception.patients:
                        print(f"Nome: {patient.name}, RG: {patient.rg}")
                        print("")
                    rg_paciente = int(input(
                        "Digite o RG do paciente para marcar o horário: "))
                    horario = input("Digite o horário marcado pro paciente:")

                paciente_selecionado = next((patient for patient in
                                             reception.patients if patient.rg
                                             == rg_paciente), None)

                if paciente_selecionado:
                    reception.add_patient_to_session(selected_session,
                                                     paciente_selecionado)
                    paciente_selecionado.horarios.append(
                        [selected_session.day, selected_session.month, horario]
                    )
                    print("[!] Horário marcado com sucesso!")
                else:
                    print("[!] Paciente não encontrado.")
            else:
                print("[!] Sessão não disponível.")
            print()
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 7:
            title()
            contador = 0
            rg_paciente = int(
                input("Digite o RG do paciente a ser pesquisado: "))
            if reception.patients:
                for patient in reception.patients:
                    if rg_paciente == patient.rg:
                        for i in patient.horarios:
                            if patient.horarios:
                                print()
                                print("-"*10)
                                print("Sessão")
                                print(f"Dia: {patient.horarios[contador][0]}")
                                print(f"Mês: {patient.horarios[contador][1]}")
                                print(
                                    f"Horário: {patient.horarios[contador][2]}"
                                )
                                print("-"*10)
                                print()
                                contador += 1
                            else:
                                print(f"O Paciente {patient.name} "
                                      "não tem sessões agendadas.")
                    else:
                        print("[!] Nenhum paciente com este RG encontrado!")
            else:
                print("Não há pacientes cadastrados!")
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 8:
            title()


title()
print(" " * 20, "1. Recepção")
print(" " * 20, "2. Dentista")
print("")
print(" " * 12, end="")
escolha = int(input("Qual sistema deseja acessar? "))
if escolha == 1:
    sistema_recepcao()
