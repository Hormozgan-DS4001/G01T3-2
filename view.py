from configure import Label, Frame, LabelFrame, TopLevel, Scale, Button, Entry, Tk


class PanelManager(Tk):
    def __init__(self, callback_show_patient, callback_add_patient, callback_add_ambulance):
        super(PanelManager, self).__init__()
