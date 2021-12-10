from configure import Frame, Button, Label


class PanelAmbulance(Frame):
    def __init__(self, callback_ambulance, callback_off, callback_patient=None):
        super(PanelAmbulance, self).__init__()
        self.callback_off = callback_off

        Label(self, text="Name:").grid(row=0, column=0)
        Label(self, text=f"{callback_ambulance.name}").grid(row=0, column=1)

        Label(self, text="Speed:").grid(row=1, column=0)
        Label(self, text=f"{callback_ambulance.speed}").grid(row=1, column=1)

        if callback_patient:
            self.lbl_name = Label(self, text="Name:")
            self.lbl_name.grid(row=2, column=0)
            self.lbl_name1 = Label(self, text=f"{callback_patient.name}")
            self.lbl_name1.grid(row=2, column=1)
            self.btn = Button(self, text="Off", command=self.off)
            self.btn.grid(row=3, column=0)

    def off(self):
        self.lbl_name.grid_forget()
        self.lbl_name1.grid_forget()
        self.btn.grid_forget()
        self.callback_off()
