from configure import Label, Frame, LabelFrame, TopLevel, Scale, Button, Entry, Tk
from tkinter import messagebox, ttk
from panel_ambulance import PanelAmbulance
from AddInfo import AddInfo


class PanelManager(Tk):
    def __init__(self, callback_show_patient, callback_add_patient, callback_add_ambulance, callback_on,
                 callback_off, callback_clock, callback_choice, callback_show_am):
        super(PanelManager, self).__init__()
        self.callback_show_patient = callback_show_patient
        self.call_back_add_patient = callback_add_patient
        self.callback_add_ambulance = callback_add_ambulance
        self.callback_on = callback_on
        self.callback_choice = callback_choice
        self.callback_off = callback_off
        self.callback_clock = callback_clock
        self.callback_show_am = callback_show_am

        self.name = None
        self.speed_worse = None

        self.list_pat = []
        self.list_am = []

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        self.main_tab = Frame(self)
        self.main_tab.grid(row=0, column=0)
        self.not_tab.add(self.main_tab, text="Emergency")
        frm_lbl = LabelFrame(self.main_tab)
        frm_lbl.grid(row=0, column=1)

        frm1 = Frame(frm_lbl)
        frm1.grid(row=0, column=0)
        Button(frm1, text="Add Patient", command=self.add_patient).grid(row=0, column=0)
        Button(frm1, text="Add Ambulance", command=self.add_ambulance).grid(row=0, column=1)

        self.frm2 = Frame(frm_lbl)
        Label(self.frm2, text="Name:").grid(row=0, column=0)
        self.ent_name_am = Entry(self.frm2)
        self.ent_name_am.grid(row=0, column=1)
        Label(self.frm2, text="Speed:").grid(row=0, column=2)
        self.ent_speed = Scale(self.frm2, width=18, length=122, from_=10, to=200, orient="horizontal")
        self.ent_speed.grid(row=0, column=3)
        Button(self.frm2, text="Ok", command=self.forget_grid_frm2).grid(row=0, column=4)

        self.frm3 = Frame(frm_lbl)
        Label(self.frm3, text="Name:").grid(row=0, column=0)
        self.ent_name_pat = Entry(self.frm3)
        self.ent_name_pat.grid(row=0, column=1)
        Label(self.frm3, text="Worse:").grid(row=0, column=2)
        self.ent_worse = Scale(self.frm3, width=18, length=122, from_=0, to=200, orient="horizontal")
        self.ent_worse.grid(row=0, column=3)
        Button(self.frm3, text="Ok", command=self.forget_grid_frm3).grid(row=0, column=4)

        Label(frm_lbl, text="Patient").grid(row=0, column=2)
        frm4 = Frame(frm_lbl)
        frm4.grid(row=0, column=3)
        self.tree = ttk.Treeview(frm4, show="headings", selectmode="browse", height=10)
        self.tree["columns"] = ("name", "worse")
        self.tree.heading("name", text="Name")
        self.tree.heading("worse", text="Worse")
        self.tree.grid(row=0, column=0)

        Label(frm_lbl, text="Ambulance").grid(row=0, column=2)
        frm5 = Frame(frm_lbl)
        frm5.grid(row=0, column=4)
        self.tree1 = ttk.Treeview(frm5, show="headings", selectmode="browse", height=10)
        self.tree1["columns"] = ("name", "speed")
        self.tree1.heading("name", text="Name")
        self.tree1.heading("worse", text="Speed")
        self.tree1.grid(row=0, column=0)
        self.tree1.bind("<Double-1>", self.panel_am)

    def panel_am(self, even):
        res = self.tree1.selection()
        result = self.tree1.item(res)["text"]
        panel = PanelAmbulance(self.list_am[int(result)], self.callback_off)
        self.not_tab.add(panel, text="Ambulance")

    def on_mission(self):
        am_res, pat_res = self.callback_choice
        result = messagebox.askokcancel("Do you want?", f"Do you want {am_res.name} to follow {pat_res.name}")
        if result:
            self.callback_on(pat_res)
            address = AddInfo(self, "Address:", f"{pat_res.name}")
            phone = AddInfo(self, "Phone:", f"{pat_res.name}")
            pat_res.update_patient(address, phone)

    def forget_grid_frm3(self):
        self.frm3.grid_forget()
        self.call_back_add_patient(self.name, self.speed_worse)
        self.show_ambulance()

    def forget_grid_frm2(self):
        self.frm2.grid_forget()
        self.callback_add_ambulance(self.name, self.speed_worse)
        self.show_patient()

    def add_ambulance(self):
        self.frm2.grid(row=0, column=1)
        self.name, self.speed_worse = self.ent_name_am.get(), self.ent_speed.get()

    def add_patient(self):
        self.frm3.grid(row=0, column=1)
        self.name, self.speed_worse = self.ent_name_pat.get(), self.ent_worse.get()

    def show_patient(self):
        patients = self.callback_show_patient()
        self.tree.delete(*self.tree.get_children())
        count = 0
        self.list_pat = []
        for pat in patients:
            self.list_pat.append(pat)
            pa = (pat.name, pat.worse)
            self.tree.insert("", "end", values=pa, text=str(count))
            count += 1

    def show_ambulance(self):
        ambulance_off, ambulance_on = self.callback_show_am()
        self.tree1.delete(*self.tree.get_children())
        count = 0
        self.list_am = []
        for am in ambulance_off.traverse():
            a = (am.name, am.speed)
            self.list_am.append(am)
            self.tree1.insert("", "end", values=a, text=str(count))
            count += 1

        for am in ambulance_on.traverse():
            self.list_am.append(am)
            a = (am.name, am.speed)
            self.tree1.insert("", "end", values=a, text=str(count))
            count += 1

    def clock(self):
        self.callback_clock()
        self.after(1000, self.clock)





