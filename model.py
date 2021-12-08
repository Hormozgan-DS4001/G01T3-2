
class Ambulance:
    def __init__(self, name: str, speed: int):
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
    def __init__(self, name, worse: int, address="", phone=""):
        self.name = name
        self.worse = worse
        self.address = address
        self.phone = phone

    def increase_worse(self):
        self.worse += 1
