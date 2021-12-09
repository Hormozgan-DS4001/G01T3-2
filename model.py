from data_structure import HeapPriority, DLL


class Ambulance:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.patient = None
        self.mission = False

    def on(self, patient):
        self.patient = patient
        self.mission = True

    def off(self):
        self.patient = None
        self.mission = False


class Patient:
    def __init__(self, name, worse, address, phone):
        self.name = name
        self.worse = worse
        self.address = address
        self.phone = phone

    def increase_worse(self):
        self.worse += 1

    def update_patient(self, address, phone):
        self.address = address
        self.phone = phone


class Core:
    def __init__(self):
        self.ambulances_off = DLL()
        self.ambulances_on = DLL()
        self.patients = HeapPriority()

    def add_patient(self, name: str, worse: int, address: str = "", phone: str = ""):
        new_patient = Patient(name, worse, address, phone)
        self.patients.enqueue(new_patient, worse)

    def add_ambulance(self, name: str, speed: int):
        new_ambulance = Ambulance(name, speed)
        self.ambulances_off.enqueue(new_ambulance, speed)

    def on_mission(self, ambulance: "Ambulance", patient: "Patient"):
        ambulance.on(patient)
        self.patients.dequeue()
        self.ambulances_on.append(ambulance, ambulance.speed)

    def off_mission(self, ambulance: "Ambulance"):
        ambulance.off()
        self.ambulances_off.enqueue(ambulance, ambulance.speed)

    def show_patient(self):
        return self.patients

    def show_ambulance(self):
        return self.ambulances_off.get_node_handler(0), self.ambulances_on.get_node_handler(0)

