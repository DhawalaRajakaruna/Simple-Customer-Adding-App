from tkinter import*
from Windows.addCustomer import AddCustomer


class Dashboard(Tk):
    def __init__(self):
        super().__init__()

        self.title("Dash Board.")
        self.config(bg="#dfe8d3")

        self.custo_frame=LabelFrame(self,text="Dash Board...",padx=100,pady=20)
        self.custo_frame.grid(row=0,column=0,padx=20,pady=20)

        self.addCustomerBut=Button(self.custo_frame,text="Add Customer",command=lambda:self.makeAddCusWin())
        self.exitBut=Button(self.custo_frame,text="Exit",command=self.destroy)

        self.addCustomerBut.pack()
        self.exitBut.pack()

    def run(self):
        self.mainloop()

    def makeAddCusWin(self):
        addCustomerWindow=AddCustomer()
        addCustomerWindow.run()