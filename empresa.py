class Empleado:
    def __init__(self, name, surname, dni, direction, telephone, salary, supervisor):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.direction = direction
        self.telephone = str(telephone)
        self.salary = salary
        self.supervisor = supervisor

    def setsupervisor(self, supervisor):
        self.supervisor = supervisor

    def addtosalary(self, number):
        self.salary += number

    def getnamesurnamedni(self):
        return self.name + " " + self.surname + " " + self.dni

    def print(self):
        print("Empleado:\n" +
              "Nombre: " + self.name + "\n" +
              "Apellidos: " + self.surname + "\n" +
              "DNI: " + self.dni + "\n" +
              "Dirección: " + self.direction + "\n" +
              "Número de teléfono: " + self.telephone + "\n" +
              "Salario: " + self.salary + "\n" +
              "Supervisor: " + self.supervisor.getnamesurnamedni()
              )


class Secretario(Empleado):
    def __init__(self, name, surname, dni, direction, telephone, salary, supervisor: Empleado, office, fax):
        super().__init__(name, surname, dni, direction, telephone, salary * 1.05, supervisor)
        self.office = str(office)
        self.fax = str(fax)

    def print(self):
        print("Secretario:\n" +
              "Nombre: " + self.name + "\n" +
              "Apellidos: " + self.surname + "\n" +
              "DNI: " + self.dni + "\n" +
              "Dirección: " + self.direction + "\n" +
              "Número de teléfono: " + self.telephone + "\n" +
              "Salario: " + self.salary + "\n" +
              "Supervisor: " + self.supervisor.getnamesurnamedni() + "\n"
              )


class Car:
    def __init__(self, plate, brand, model):
        self.plate = plate
        self.brand = brand
        self.model = model

    def data(self):
        return self.plate + " " + self.brand + " " + self.model


class Client:
    def __init__(self, dni, name):
        self.dni = dni
        self.name = name


class Vendedor(Empleado):
    def __init__(self, name, surname, dni, direction, telephone, salary, supervisor: Empleado, car: Car, mobile, area,
                 clients: list,
                 comission):
        super().__init__(name, surname, dni, direction, telephone, salary * 1.1, supervisor)
        self.car = car
        self.mobile = str(mobile)
        self.area = str(area)
        self.clients = clients
        self.comission = comission

    def newclient(self, client):
        self.clients.append(client)

    def removeclient(self, client):
        self.clients.remove(client)

    def changecar(self, car):
        self.car = car

    def print(self):
        print("Empleado:\n" +
              "Nombre: " + self.name + "\n" +
              "Apellidos: " + self.surname + "\n" +
              "DNI: " + self.dni + "\n" +
              "Dirección: " + self.direction + "\n" +
              "Número de teléfono: " + self.telephone + "\n" +
              "Salario: " + self.salary + "\n" +
              "Supervisor: " + self.supervisor.getnamesurnamedni() + "\n"
              )


class JefeDeZona(Empleado):
    def __init__(self, name, surname, dni, direction, telephone, salary, supervisor, secretary: Secretario, car: Car,
                 vendorlist: list):
        super().__init__(name, surname, dni, direction, telephone, salary, supervisor)
        self.secretary = secretary
        self.car = car
        self.vendorlist = vendorlist

    def changesecretary(self, secretary: Secretario):
        self.secretary = secretary

    def changecar(self, car: Car):
        self.car = car

    def newvendor(self, vendor: Vendedor):
        self.vendorlist.append(vendor)

    def removevendor(self, vendor: Vendedor):
        self.vendorlist.remove(vendor)

