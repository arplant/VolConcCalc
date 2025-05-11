
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Volume-Concentration Calculator")
        self.geometry("400x150")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.check_var = customtkinter.StringVar(value="on")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame,
                                                    text="checkbox 1",
                                                    command=self.checkbox_event,
                                                    variable=self.check_var,
                                                    onvalue="on",
                                                    offvalue="off")
        self.checkbox_1.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
        print("button pressed")

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())


app = App()
app.mainloop()

