from tkinter import*
from Functions.AddCustomerfunc import addCustomer
from Functions.showCustomerFunc import showCustomer

class AddCustomer(Tk):
    def __init__(self):
        super().__init__()

        self.title("Add Customer Window.")
        self.config(bg="#dfe8d3")

        self.custo_frame=LabelFrame(self,text="Add Customer Details...",padx=100,pady=20)
        self.custo_frame.grid(row=0,column=0,padx=20,pady=20)

        self.namelabel=Label(self.custo_frame,text="Name",pady=20)
        self.namelabel.grid(row=0,column=0)
        self.nameEntry=Entry(self.custo_frame,width=50)
        self.nameEntry.grid(row=0,column=1)

        self.agelabel=Label(self.custo_frame,text="Age",pady=20)
        self.agelabel.grid(row=1,column=0)
        self.ageEntry=Entry(self.custo_frame,width=50)
        self.ageEntry.grid(row=1,column=1)

        self.addresslabel=Label(self.custo_frame,text="Address",pady=20)
        self.addresslabel.grid(row=2,column=0)
        self.addressEntry=Entry(self.custo_frame,width=50)
        self.addressEntry.grid(row=2,column=1)

        self.idlabel=Label(self.custo_frame,text="ID",pady=20)
        self.idlabel.grid(row=3,column=0)
        self.idEntry=Entry(self.custo_frame,width=50)
        self.idEntry.grid(row=3,column=1)

        self.saveBut=Button(self,text="Save",
                            command=lambda:self.sendToSave(self.nameEntry.get(),
                                                                 self.ageEntry.get(),
                                                                 self.addressEntry.get(),
                                                                 self.idEntry.get()))
        self.showBut=Button(self,text="Show Customers ",command=lambda:self.showCustomers())
        self.showBut.grid(row=1,column=0,sticky="W",padx=20)
        self.saveBut.grid(row=1,column=0,sticky='E',padx=20)
        self.exitBut=Button(self,text="Exit",command=self.destroy)
        self.exitBut.grid(row=1,column=0)

    def showCustomers(self):
        showCustomer()

    def sendToSave(self,name,age,address,id):
        addCustomer(name,age,address,id)
        self.nameEntry.delete(0,END)
        self.ageEntry.delete(0,END)
        self.addressEntry.delete(0,END)
        self.idEntry.delete(0,END)
            
    def run(self):
        self.mainloop()