
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


class Core:
    def __init__(self):
        pass

    def add_patient(self, name: str, worse: int, address: str = "", phone: str = ""):
        pass

    def add_ambulance(self, name: str, speed: int):
        pass

    def on_mission(self, data):
        pass

    def off_mission(self, data, key):
        pass

    def show_patient(self):
        pass

    def show_ambulance(self):
        pass

