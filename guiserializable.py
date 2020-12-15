import tkinter
import pickle
from tkinter import ttk, messagebox


class Contact:

    def __init__(self, telephone, name, surname):
        self.telephone = telephone
        self.name = name
        self.surname = surname


class Contacts:

    def __init__(self):
        self.clist = []

    def addcontact(self, contact: Contact):
        self.clist.append(contact)

    def removecontact(self, contact: Contact):
        self.clist.remove(contact)

    def dumpcontacts(self, filename: str):
        outfile = open(filename, 'wb')
        pickle.dump(self.clist, outfile)
        outfile.close()

    def readcontacts(self, filename: str):
        infile = open(filename, 'rb')
        self.clist = pickle.load(infile)
        infile.close()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Agenda de contactos")

    contacts = Contacts()

    table = ttk.Treeview()
    table.grid(row=0, column=0, columnspan=6)

    table["columns"] = ("1", "2", "3")

    table.column("#0", width=0)
    table.column("1", width=100, minwidth=100)
    table.column("2", width=100, minwidth=100)
    table.column("3", width=100, minwidth=100)
    table.heading("#0", text="Nº")
    table.heading("1", text="Telefono")
    table.heading("2", text="Apellidos")
    table.heading("3", text="Nombre")

    telephonelabel = tkinter.Label(window, text="Telefono")
    telephonelabel.grid(row=1, column=0)

    telephonefield = tkinter.Entry(window)
    telephonefield.grid(row=1, column=1)

    namelabel = tkinter.Label(window, text="Nombre")
    namelabel.grid(row=1, column=2)

    namefield = tkinter.Entry(window)
    namefield.grid(row=1, column=3)

    surnamelabel = tkinter.Label(window, text="Apellidos")
    surnamelabel.grid(row=1, column=4)

    surnamefield = tkinter.Entry(window)
    surnamefield.grid(row=1, column=5)

    addButton = tkinter.Button(window, text="Añadir", command=contacts.addcontact())





    window.mainloop()

