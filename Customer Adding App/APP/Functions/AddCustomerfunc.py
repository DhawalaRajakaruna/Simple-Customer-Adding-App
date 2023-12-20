from db.db import cutomerList
from Classes.Customer import Customer
from tkinter import messagebox
from Functions.showCustomerFunc import*
def addCustomer(name,age,address,id):
        new_Customer=Customer(name,age,address,id)
        try:
                cutomerList.append(new_Customer)
                messagebox.showinfo("Added Customer","Customer Adde Successfully")
                
                print(cutomerList)
        except Exception as e:
                messagebox.showerror("Error in Adding Customer","Error Happends in Adding Customer ! ")
                print(e)