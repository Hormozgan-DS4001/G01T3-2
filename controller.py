from model import Core
from view import PanelManager
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()

win = PanelManager(database.show_patient, database.add_patient, database.add_ambulance, database.on_mission,
                   database.off_mission, database.clock, database.choice_ambulance, database.show_ambulance)

win.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
