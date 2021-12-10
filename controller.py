from model import Core
from view import PanelManager

database = Core()

win = PanelManager(database.show_patient, database.add_patient, database.add_ambulance, database.on_mission,
                   database.off_mission, database.clock, database.choice_ambulance, database.show_ambulance)

win.mainloop()



