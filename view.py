from configure import Label, Frame, LabelFrame, TopLevel, Scale, Button, Entry, Tk


class PanelManager(Tk):
    def __init__(self, callback_show_patient, callback_add_patient, callback_add_ambulance, callback_on,
                 callback_off):
        super(PanelManager, self).__init__()
        self.callback_show_patient = callback_show_patient
        self.call_back_add_patient = callback_add_patient
        self.callback_add_ambulance = callback_add_ambulance
        self.callback_on = callback_on
        self.callback_off = callback_off



