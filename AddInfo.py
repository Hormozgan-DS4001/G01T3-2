from configure import TopLevel, Label, Button, Entry


class AddInfo(TopLevel):
    def __init__(self, master, message: str = "", title: str = ""):
        super(AddInfo, self).__init__(master)
        self.title = title
        self.geometry("500x500+200+100")
        Label(self, text=f"{message}: ").grid(row=0, column=0)
        self.ent = Entry(self)
        self.ent.grid(row=0, column=1)
        Button(self, text="OK", command=self.okay).grid(row=1, column=0)
        self.result = None

    def okay(self):
        self.result = self.ent.get()
        if self.result == "":
            return
        self.destroy()

    def get_result(self):
        if self.result is None:
            self.wait_window()
        return self.result
