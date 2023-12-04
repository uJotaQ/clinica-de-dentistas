class Patient:
    def __init__(self, name):
        self.name = name


class Session:
    def __init__(self, duration, day, month):
        self.duration = duration
        self.day = day
        self.month = month
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)


class Receptions:
    def __init__(self):
        self.sessions = []

    def add_session(self, duration, day, month):
        session = Session(duration, day, month)
        self.sessions.append(session)
        return session

    def add_patient_to_session(self, session, patient):
        session.add_patient(patient)


# Criando instâncias de pacientes
patient1 = Patient("João")
patient2 = Patient("Maria")

# Criando instância da recepção
reception = Receptions()

# Adicionando sessões à recepção
session1 = reception.add_session(5, 2, 3)
session2 = reception.add_session(7, 2, 3)

# Adicionando pacientes às sessões
reception.add_patient_to_session(session1, patient1)
reception.add_patient_to_session(session2, patient2)

# Acessando informações
for session in reception.sessions:
    print(f"Sessão no dia {session.day}/{session.month} com duração de"
          f"{session.duration} horas:")
    for patient in session.patients:
        print(f"  - Paciente: {patient.name}")
