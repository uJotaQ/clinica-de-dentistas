from datetime import datetime


class Patient:
    def __init__(self, name, age, rg):
        self.name = name
        self.age = age
        self.rg = rg
        self.medic = []
        self.horarios = []


class Session:
    def __init__(self, duration, day, month):
        self.duration = duration
        self.day = day
        self.month = month
        self.patients = []
        self.fila = []
        self.is_active = False

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_patient_fila(self, patient):
        self.fila.append(patient)


class Clinica:
    def __init__(self):
        self.sessions = []
        self.patients = []

    def add_patient(self, name, age, rg):
        patient = Patient(name, age, rg)
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


sistema_clinica = Clinica()


def sistema_recepcao(system):
    reception = system
    while True:
        title()
        print(" " * 17, "1 - Cadastrar Paciente")
        print(" " * 17, "2 - Cadastrar Sessão")
        print(" " * 17, "3 - Listar Sessões")
        print(" " * 17, "4 - Buscar Sessão")
        print(" " * 17, "5 - Iniciar Sessão Clínica De Hoje")
        print(" " * 17, "6 - Marcar Horário Para Paciente")
        print(" " * 17, "7 - Listar Horários De Um Paciente")
        print(" " * 17, "8 - Verificar Horário De Um Paciente Na Sessão Atual")
        print(" " * 17, "9 - Adicionar Paciente Na Fila Da Sessão Atual")
        print(" " * 17, "10 - Listar Próximo Paciente Da Fila De Atendimento")
        print(" " * 17, "11 - Sair")
        print("")
        print(" " * 18, end="")
        escolha_opcao = int(input("Escolha uma opção: "))

        if escolha_opcao == 1:
            title()
            can_add = True
            name = input("Digite o nome completo do paciente: ")
            age = int(input("Digite a idade do paciente: "))
            rg = int(input("Digite o RG do paciente: "))

            for patient in reception.patients:
                if patient.rg == rg:
                    print("Esse RG já está cadastrado!")
                    can_add = False
                    break

            if can_add:
                reception.add_patient(name, age, rg)
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
                print(f"Duração: {session_data.duration}min, "
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
            data_atual = datetime.today()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            ano_atual = data_atual.year
            print()
            for session_data in reception.sessions:
                if (session_data.day == dia_atual
                        and session_data.month == mes_atual
                        and session_data.is_active is False):
                    session_data.is_active = True
                    print(
                        f"-> Sessão {dia_atual}/"
                        f"{mes_atual}/{ano_atual}")
                    print()
                    print("[!] Sessão iniciada com sucesso!")
                    cont = 1
                if cont != 1:
                    print("[!] Sessão Já Iniciada Ou Não Existe!")
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
                    horario = input("Digite o horário marcado pro paciente: ")

                paciente_selecionado = next((patient for patient in
                                             reception.patients if patient.rg
                                             == rg_paciente), None)

                if paciente_selecionado:
                    reception.add_patient_to_session(selected_session,
                                                     paciente_selecionado)
                    paciente_selecionado.horarios.append(
                        [selected_session.day, selected_session.month, horario]
                    )
                    print()
                    print("[!] Horário marcado com sucesso!")
                else:
                    print()
                    print("[!] Paciente não encontrado.")
            else:
                print()
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
            data_atual = datetime.today()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            rg_paciente = int(
                input("Digite o RG do paciente a ser pesquisado: "))
            for session in reception.sessions:
                if dia_atual == session.day:
                    if mes_atual == session.month:
                        if session.is_active is True:
                            sessao_atual = session
            for patient in reception.patients:
                for horario in patient.horarios:
                    if horario[0] == sessao_atual.day:
                        if horario[1] == sessao_atual.month:
                            print()
                            print("-+-"*10)
                            print(f"[!] O Paciente está marcado "
                                  f"para hoje ás {horario[2]}")
                            print("-+-"*10)
            input("Pressione [ENTER] para continuar")
        elif escolha_opcao == 9:
            title()
            data_atual = datetime.today()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            ano_atual = data_atual.year
            patient_found = None
            print(f"-> Sessão {dia_atual}/{mes_atual}/{ano_atual}")
            print()
            print("Lista de Pacientes:")
            for patient in reception.patients:
                print(f"Nome: {patient.name}, RG: {patient.rg}")
                print("")
            rg = int(input("Digite o RG do paciente: "))
            for patient in reception.patients:
                if patient.rg == rg:
                    patient_found = patient
            for session in reception.sessions:
                if dia_atual == session.day:
                    if mes_atual == session.month:
                        if session.is_active is True:
                            session.add_patient_fila(patient_found)
                            print()
                            print("[!] Paciente Adicionado Na"
                                  " Fila Com Sucesso!")
                            print()
            input("Pressione [ENTER] para continuar")
        elif escolha_opcao == 10:
            title()
            data_atual = datetime.today()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            for session in reception.sessions:
                if dia_atual == session.day:
                    if mes_atual == session.month:
                        if session.fila:
                            print("-+-"*10)
                            print("Próximo Paciente A Ser Atendido:")
                            print()
                            print(f"Nome: {session.fila[0].name}")
                            print(f"Idade: {session.fila[0].age}")
                            print(f"RG: {session.fila[0].rg}")
                            print("-+-"*10)
                            print()
                        else:
                            print("[!] Não há pacientes na fila desta sessão!")
            input("Pressione [ENTER] para continuar")
        elif escolha_opcao == 11:
            break
        else:
            title()
            print("[!] Selecione Uma Opção Válida!")

    global sistema_clinica
    sistema_clinica = reception


def sistema_dentista(system):
    dentista = system
    while True:
        title()
        print(" " * 17, "1 - Localizar Sessão Clínica")
        print(" " * 17, "2 - Iniciar Sessão Clínica")
        print(" " * 17, "3 - Atender Próximo Paciente")
        print(" " * 17, "4 - Sair")
        print("")
        print(" " * 18, end="")
        escolha_opcao = int(input("Escolha uma opção: "))

        if escolha_opcao == 1:
            title()
            dia_busca_sessao = int(input("Digite o dia da sessão: "))
            mes_busca_sessao = int(input("Digite o mês da sessão: "))
            print()
            if dentista.sessions != []:
                contador = 0
                for session_data in dentista.sessions:
                    contador += 1
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
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 2:
            title()
            dia_inicio_sessao = int(input("Digite o dia da sessão: "))
            mes_inicio_sessao = int(input("Digite o mês da sessão: "))
            print()
            for session_data in dentista.sessions:
                if (session_data.day == dia_inicio_sessao
                        and session_data.month == mes_inicio_sessao
                        and session_data.is_active is False):
                    session_data.is_active = True
                    print("[!] Sessão iniciada com sucesso!")
                else:
                    print("[!] Sessão já iniciada ou não existe!")
            print()
            input("Pressione [ENTER] para continuar")

        elif escolha_opcao == 3:
            data_atual = datetime.today()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            ano_atual = data_atual.year
            for session in dentista.sessions:
                if dia_atual == session.day and mes_atual == session.month:
                    if session.fila:
                        while True:
                            print("-+-"*10)
                            print("Próximo Paciente A Ser Atendido:")
                            print()
                            print(f"Nome: {session.fila[0].name}")
                            print(f"Idade: {session.fila[0].age}")
                            print(f"RG: {session.fila[0].rg}")
                            print("-+-"*10)
                            print()
                            print(" " * 17, "1 - Ler Prontuário Completo")

                            print(" " * 17, "2 - Ler Primeira "
                                  "Anotação Do Prontuário")

                            print(" " * 17, "3 - Ler A Última "
                                  "Anotação Do Prontuário")

                            print(" " * 17, "4 - Adicionar "
                                  "Nova Anotação No Prontuário")
                            print(" " * 17, "5 - Voltar")
                            escolha_opcao = int(input("Escolha uma opção: "))
                            if escolha_opcao == 1:
                                title()
                                for session in dentista.sessions:
                                    if dia_atual == session.day:
                                        if mes_atual == session.month:
                                            if session.fila:
                                                if session.fila[0].medic:
                                                    print("-+-"*10)
                                                    print(
                                                        "Anotações do"
                                                        "Prontuário")
                                                    print()
                                                    for p in (session.fila[0].
                                                              medic):
                                                        print(p)
                                                        print()
                                                    print("-+-"*10)

                            elif escolha_opcao == 2:
                                title()
                                for session in dentista.sessions:
                                    if dia_atual == session.day:
                                        if mes_atual == session.month:
                                            if session.fila:
                                                if session.fila[0].medic:
                                                    print("-+-"*10)
                                                    print("Primeira "
                                                          "Anotação Do "
                                                          "Prontuário:")
                                                    print()
                                                    print(session.fila[0].
                                                          medic[0])
                                                    print("-+-"*10)

                            elif escolha_opcao == 3:
                                title()
                                for session in dentista.sessions:
                                    if dia_atual == session.day:
                                        if mes_atual == session.month:
                                            if session.fila:
                                                if session.fila[0].medic:
                                                    i = len(
                                                        session.fila[0].
                                                        medic)-1
                                                    print("-+-"*10)
                                                    print("Última "
                                                          "Anotação Do "
                                                          "Prontuário:")
                                                    print()
                                                    print(session.fila[0].
                                                          medic[i])
                                                    print("-+-"*10)
                                            else:
                                                print()
                                                print(
                                                    "[!] Não há pacientes na "
                                                    "fila desta sessão!")
                                print()
                                input("Pressione [ENTER] para continuar")
                            elif escolha_opcao == 4:
                                title()
                                for session in dentista.sessions:
                                    if dia_atual == session.day:
                                        if mes_atual == session.month:
                                            if session.fila:
                                                texto = input(
                                                    "Escreva A "
                                                    "Nova Anotação: ")
                                                txt_f = (
                                                    f"{dia_atual}/{mes_atual}/"
                                                    f"{ano_atual} -> ")
                                                txt_f += texto
                                                (session.fila[0].medic.
                                                 append(txt_f))
                            elif escolha_opcao == 5:
                                break
        elif escolha_opcao == 4:
            break
    global sistema_clinica
    sistema_clinica = dentista


def popular(system):
    popular_system = system
    popular_system.add_patient("Joao", 18, 4455)
    popular_system.add_patient("André", 20, 8593)
    popular_system.add_patient("Iran", 19, 2354)
    popular_system.add_patient("Maria", 25, 8235)
    popular_system.add_patient("Kamile", 17, 8345)
    popular_system.add_session(70, 20, 1)
    popular_system.add_session(90, 15, 1)
    popular_system.add_session(150, 18, 1)
    popular_system.add_session(30, 23, 1)
    popular_system.add_session(45, 9, 1)
    global sistema_clinica
    sistema_clinica = popular_system


while True:
    title()
    print(" " * 20, "1. Recepção")
    print(" " * 20, "2. Dentista")
    print(" " * 20, "3. Sair")
    print("")
    print(" " * 12, end="")
    escolha = int(input("Qual sistema deseja acessar? "))
    if escolha == 1:
        sistema_recepcao(sistema_clinica)
    elif escolha == 2:
        sistema_dentista(sistema_clinica)
    elif escolha == 3:
        break
    elif escolha == 5:
        popular(sistema_clinica)
