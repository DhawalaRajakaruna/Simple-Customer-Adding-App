from tkinter import*
from db.db import *
class ShowCustomer(Tk):
    def __init__(self):
        super().__init__()

        self.title("Show Customer Window.")
        self.config(bg="#dfe8d3")
        self.custo_frame=LabelFrame(self,text="Show Customer Details...",padx=100,pady=20)
        self.custo_frame.grid(row=0,column=0,padx=20,pady=20)

        self.idLabel=Label(self.custo_frame,text="ID",borderwidth=2,relief="solid",padx=50)
        self.nameLabel=Label(self.custo_frame,text="Name",borderwidth=2,relief="solid",padx=50)
        self.ageLabel=Label(self.custo_frame,text="Age",borderwidth=2,relief="solid",padx=50)
        self.addressLabel=Label(self.custo_frame,text="Address",borderwidth=2,relief="solid",padx=50)

        self.idLabel.grid(row=0,column=0)
        self.nameLabel.grid(row=0,column=1)
        self.ageLabel.grid(row=0,column=2)
        self.addressLabel.grid(row=0,column=3)

        self.loadWhenAdd()
        
        self.exitBut=Button(self,text="Exit",command=self.destroy)
        self.exitBut.grid(row=1,column=0)
    def loadWhenAdd(self):
        for index,customer in enumerate(cutomerList):
            self.idItemlabel=Label(self.custo_frame,text=customer.getId())
            self.nameItemlabel=Label(self.custo_frame,text=customer.getName())
            self.ageItemlabel=Label(self.custo_frame,text=customer.getAge())
            self.addressItemlabel=Label(self.custo_frame,text=customer.getAddress())

            self.idItemlabel.grid(row=index+1,column=0)
            self.nameItemlabel.grid(row=index+1,column=1)
            self.ageItemlabel.grid(row=index+1,column=2)
            self.addressItemlabel.grid(row=index+1,column=3)
        return
    def run(self):
        self.mainloop()