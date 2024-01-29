# Importação de bibliotecas
from datetime import datetime


# Classe para os pacientes da clínica.
class Patient:

    # Inicialização da classe "Patient"
    def __init__(self, name, age, rg):
        self.name = name
        self.age = age
        self.rg = rg
        self.medic = []
        self.horarios = []

# Classe para as sessões da clínica.
class Session:
    # Inicialização da classe "Session"
    def __init__(self, duration, day, month, year):
        self.duration = duration
        self.day = day
        self.month = month
        self.year = year
        self.patients = []
        self.fila = []
        self.is_active = False

    # Função para adicionar pacientes à sessão!
    def add_patient(self, patient):
        self.patients.append(patient)

    # Função para adicionar pacientes á fila de atendimento!
    def add_patient_fila(self, patient):
        self.fila.append(patient)

# Classe para o sistema da clínica.
class Clinic:
    # Abaixo, todas as funções da Recepção!

    # Inicialização da classe "Clinic".
    def __init__(self):
        self.sessions = []
        self.patients = []

    # Esta função cadastra o paciente no sistema!
    def add_patient(self):
        title()
        can_add = True
        name = input("Digite o nome completo do paciente: ")
        age = int(input("Digite a idade do paciente: "))
        rg = int(input("Digite o RG do paciente: "))

        for patient in self.patients:
            if patient.rg == rg:
                print("Esse RG já está cadastrado!")
                can_add = False
                break

        if can_add:
            patient = Patient(name, age, rg)
            self.patients.append(patient)
            print("Paciente cadastrado com sucesso!\n")
        input("[!] Pressione ENTER para continuar")

    # Esta função cadastra uma nova sessão no sistema!
    def add_session(self):
        title()
        can_add = True
        duration = int(input("Digite a duração da sessão (minutos): "))
        day = int(input("Digite o dia da sessão: "))
        month = int(input("Digite o mês da sessão: "))
        year = int(input("Digite o ano da sessão: "))

        for session in self.sessions:
            if (session.day == day and session.month == month 
                and session.year == year):
                print("Já existe uma sessão nessa data!")
                input("[!] Pressione ENTER para continuar")
                can_add = False
                break

        if can_add:
            session = Session(duration, day, month, year)
            self.sessions.append(session)
            print()
            print("[!] Sessão adicionada com sucesso!")
        input("Pressione [ENTER] para continuar")

    # Esta função adiciona o paciente á fila da sessão atual!
    def add_patient_to_session(self, session, patient):
        title()
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        patient_found = None
        print(f"-> Sessão {dia_atual}/{mes_atual}/{ano_atual}")
        print()
        print("Lista de Pacientes:")
        for patient in self.patients:
            print(f"Nome: {patient.name}, RG: {patient.rg}")
            print("")
        rg = int(input("Digite o RG do paciente: "))
        for patient in self.patients:
            if patient.rg == rg:
                patient_found = patient
        for session in self.sessions:
            if dia_atual == session.day:
                if mes_atual == session.month:
                    if session.is_active is True:
                        session.add_patient_fila(patient_found)
                        print()
                        print("[!] Paciente Adicionado Na"
                              " Fila Com Sucesso!")
                        print()
        input("Pressione [ENTER] para continuar")

    # Esta função lista as sessões cadastradas!
    def list_sessions(self):
        title()
        print("Sessões Cadastradas:")
        for session_data in self.sessions:
            print()
            print(f"Duração: {session_data.duration}min, "
                    f"Dia: {session_data.day}, Mês: {session_data.month}")
            for patient in session_data.patients:
                print(f"|-> Paciente: {patient.name}")
        print()
        input("Pressione [ENTER] para continuar")

    # Esta função procura uma sessão, passando dia, mês e ano!
    def search_session(self):
        title()
        dia_busca_sessao = int(input("Digite o dia da sessão: "))
        mes_busca_sessao = int(input("Digite o mês da sessão: "))
        ano_busca_sessao = int(input("Digite o ano da sessão: "))
        print()
        if self.sessions != []:
            for session_data in self.sessions:
                contador = 0
                contador = +1
                if (session_data.day == dia_busca_sessao
                        and session_data.month == mes_busca_sessao
                            and session_data.year == ano_busca_sessao):
                    print(" " * 13, f"Sessão {contador}")
                    print(f"Duração: {session_data.duration}min,"
                            f"Dia: {session_data.day},"
                            f" Mês: {session_data.month}, "
                            f" Ano: {session_data.year}")
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

    # Esta função inicia a sessão do dia atual!
    def start_session(self):
        title()
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        print()
        for session_data in self.sessions:
            if (session_data.day == dia_atual
                    and session_data.month == mes_atual
                    and session_data.year == ano_atual
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

    # Esta função encerra a sessão do dia atual!
    def finish_session(self):
        title()
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        print()
        for session_data in self.sessions:
            if (session_data.day == dia_atual
                    and session_data.month == mes_atual
                    and session_data.year == ano_atual
                    and session_data.is_active is True):
                session_data.is_active = False
                print(
                    f"-> Sessão {dia_atual}/"
                    f"{mes_atual}/{ano_atual}")
                print()
                print("[!] Sessão encerrada com sucesso!")
                cont = 1
            if cont != 1:
                print("[!] Sessão Já Encerrada Ou Não Existe!")
        print()
        input("Pressione [ENTER] para continuar")

    # Esta função agenda um horário pro paciente em uma sessão!
    def schedule(self):
        title()
        dia_busca_sessao = int(input("Digite o dia da sessão: "))
        mes_busca_sessao = int(input("Digite o mês da sessão: "))
        ano_busca_sessao = int(input("Digite o ano da sessão: "))

        session_disponivel = False
        selected_session = None

        for session in self.sessions:
            print()
            print(f"Sessão -> Dia: {session.day}, Mês: {session.month}")
            if (session.day == dia_busca_sessao and
                session.month == mes_busca_sessao
                and session.year == ano_busca_sessao):
                session_disponivel = True
                selected_session = session
                break

        if session_disponivel:
            if self.patients:
                print()
                print("Lista de Pacientes:")
                for patient in self.patients:
                    print(f"Nome: {patient.name}, RG: {patient.rg}")
                    print("")
                rg_paciente = int(input("Digite o RG do paciente para marcar o horário: "))
                horario = input("Digite o horário marcado pro paciente: ")

                paciente_selecionado = next((patient for patient in
                                             self.patients if patient.rg
                                             == rg_paciente), None)

                if paciente_selecionado:
                    self.add_patient_to_session(selected_session,
                                                     paciente_selecionado)
                    paciente_selecionado.horarios.append(
                        [selected_session.day, selected_session.month,
                          selected_session.year, horario]
                        )
                    print()
                    print("[!] Horário marcado com sucesso!")
                else:
                    print()
                    print("[!] Paciente não encontrado.")
            else:
                print()
                print("[!] Pacientes não cadastrados.")
        else:
            print()
            print("[!] Sessão não disponível.")
        print()
        input("Pressione [ENTER] para continuar")

    # Esta função lista quais horários estão marcados para um paciente!
    def list_hour_patient(self):
        title()
        contador = 0
        rg_paciente = int(
                input("Digite o RG do paciente a ser pesquisado: "))
        if self.patients:
            for patient in self.patients:
                if rg_paciente == patient.rg:
                    for i in patient.horarios:
                        if patient.horarios:
                            print()
                            print("-"*10)
                            print("Sessão")
                            print(f"Dia: {patient.horarios[contador][0]}")
                            print(f"Mês: {patient.horarios[contador][1]}")
                            print(f"Ano: {patient.horarios[contador][2]}")
                            print(
                                  f"Horário: {patient.horarios[contador][3]}"
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

    # Esta função verifica se o paciente está marcado para a sessão atual!
    def verify_hour_patient(self):
        title()
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        rg_paciente = int(
            input("Digite o RG do paciente a ser pesquisado: "))
        for session in self.sessions:
            if dia_atual == session.day and mes_atual == session.month and ano_atual == session.year:
                    if session.is_active is True:
                        sessao_atual = session

        for patient in self.patients:
            for horario in patient.horarios:
                if horario[0] == sessao_atual.day:
                    if horario[1] == sessao_atual.month and horario[2] == sessao_atual.year:
                        print()
                        print("-+-"*10)
                        print(f"[!] O Paciente está marcado "
                                f"para hoje ás {horario[3]}")
                        print("-+-"*10)
        input("Pressione [ENTER] para continuar")
    
    # Esta função lista qual o próximo paciente!
    def list_next_patient(self):
        title()
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        for session in self.sessions:
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


    # Abaixo, as funções exclusivas do Dentista!

    # Esta função chama o próximo paciente a ser atendido, exibindo novas funcionalidades!
    def attend_next_patient(self):
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        for session in self.sessions:
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
                        print(" " * 17, "2 - Ler Primeira Anotação Do Prontuário")
                        print(" " * 17, "3 - Ler A Última Anotação Do Prontuário")
                        print(" " * 17, "4 - Adicionar Nova Anotação No Prontuário")
                        print(" " * 17, "5 - Voltar")
                        escolha_opcao = int(input("Escolha uma opção: "))
                        if escolha_opcao == 1:
                            self.read_record()

                        elif escolha_opcao == 2:
                            self.read_first_note()

                        elif escolha_opcao == 3:
                            self.read_last_note()

                        elif escolha_opcao == 4:
                            self.add_new_note()
                                
                        elif escolha_opcao == 5:
                            break

    # Esta função lê o prontuário completo do paciente!
    def read_record(self):
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        title()
        for session in self.sessions:
            if dia_atual == session.day:
                if mes_atual == session.month:
                    if session.fila:
                        if session.fila[0].medic:
                            print("-+-"*10)
                            print("Anotações do Prontuário")
                            print()
                            for p in (session.fila[0].medic):
                                print(p)
                                print()
                            print("-+-"*10)

    # Esta função lê a primeira anotação no prontuário do paciente atendido
    def read_first_note(self):
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        title()
        for session in self.sessions:
            if dia_atual == session.day:
                if mes_atual == session.month:
                    if session.fila:
                        if session.fila[0].medic:
                            print("-+-"*10)
                            print("Primeira Anotação Do Prontuário:")
                            print()
                            print(session.fila[0].medic[0])
                            print("-+-"*10)

    # Esta função lê a última anotação no prontuário do paciente atendido
    def read_last_note(self):
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        title()
        for session in self.sessions:
            if dia_atual == session.day:
                if mes_atual == session.month:
                    if session.fila:
                        if session.fila[0].medic:
                            i = len(session.fila[0].medic)-1
                            print("-+-"*10)
                            print("Última Anotação Do Prontuário:")
                            print()
                            print(session.fila[0].medic[i])
                            print("-+-"*10)
                    else:
                        print()
                        print("[!] Não há pacientes na fila desta sessão!")
        print()
        input("Pressione [ENTER] para continuar")

    # Esta função dá a possibilidade do dentista escrever uma nova anotação no prontuário
    def add_new_note(self):
        data_atual = datetime.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        title()
        for session in self.sessions:
            if dia_atual == session.day:
                if mes_atual == session.month:
                    if session.fila:
                        texto = input("Escreva A Nova Anotação: ")
                        txt_f = (f"{dia_atual}/{mes_atual}/{ano_atual} -> ")
                        txt_f += texto
                        (session.fila[0].medic.append(txt_f))

# Esta linha instancia o sistema da clínica com a classe "Clinic"
clinic_system = Clinic()


# Esta função exibe o título do programa!
def title():
    print("-=-" * 20)
    print(" " * 18, "Clinica Dente Clean")
    print("-=-" * 20)
    print("")

# Esta função executa o sistema da recepção.
def sistema_recepcao(system):
    # instanciando o sistema
    reception = system

    # Loop principal do sistema
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
        print(" " * 17, "11 - Encerrar Sessão Clínica De Hoje")
        print(" " * 17, "12 - Sair")
        print("")
        print(" " * 18, end="")

        # Escolha de opções com base no menu acima.
        escolha_opcao = int(input("Escolha uma opção: "))

        if escolha_opcao == 1:
            reception.add_patient()

        elif escolha_opcao == 2:
            reception.add_session()

        elif escolha_opcao == 3:
            reception.list_sessions()

        elif escolha_opcao == 4:
            reception.search_session()

        elif escolha_opcao == 5:
            reception.start_session()

        elif escolha_opcao == 6:
            reception.schedule()

        elif escolha_opcao == 7:
            reception.list_hour_patient()

        elif escolha_opcao == 8:
            reception.verify_hour_patient()

        elif escolha_opcao == 9:
            reception.add_patient_to_session()

        elif escolha_opcao == 10:
            reception.list_next_patient()

        elif escolha_opcao == 11:
            reception.finish_session()

        elif escolha_opcao == 12:
            break
        else:
            # Condicional para exibir uma mensagem de erro 
            # caso não seja digitado um número fora das opções
            title()
            print("[!] Selecione Uma Opção Válida!")

    # Por fim, o sistema salva todas as alterações feitas
    # no sistema da recepção, no sistema principal da clinica
    global clinic_system
    clinic_system = reception

# Esta função executa o sistema do dentista
def sistema_dentista(system):

    # instanciando o sistema do dentista
    dentist = system

    # Loop principal do sistema
    while True:
        title()

        # Menu inicial do dentista
        print(" " * 17, "1 - Localizar Sessão Clínica")
        print(" " * 17, "2 - Iniciar Sessão Clínica")
        print(" " * 17, "3 - Atender Próximo Paciente")
        print(" " * 17, "4 - Sair")
        print("")
        print(" " * 18, end="")
        pick_option = int(input("Escolha uma opção: "))

        if pick_option == 1:
            dentist.search_session()

        elif pick_option == 2:
            dentist.start_session()

        elif pick_option == 3:
            dentist.attend_next_patient()

        elif pick_option == 4:
            break

    # Por fim, o sistema salva todas as alterações feitas
    # no sistema do dentista, no sistema principal da clinica
    global clinic_system
    clinic_system = dentist

# Esta função tem o objetivo de popular o sistema para poupar tempo ao testar as funcionalidades do programa!
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
    global clinic_system
    clinic_system = popular_system

# Esta é a função principal do programa
def main():
    # Loop principal do programa
    while True:
        title()
        print(" " * 20, "1. Recepção")
        print(" " * 20, "2. Dentista")
        print(" " * 20, "3. Sair")
        print("")
        print(" " * 12, end="")
        pick_option = int(input("Qual sistema deseja acessar? "))
        if pick_option == 1:
            sistema_recepcao(clinic_system)
        elif pick_option == 2:
            sistema_dentista(clinic_system)
        elif pick_option == 3:
            break

# Execução do programa.
main()
