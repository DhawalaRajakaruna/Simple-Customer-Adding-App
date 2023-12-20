class Customer:
    def __init__(self,name,age,address,id):
        self.name=name
        self.age=age
        self.address=address
        self.id=id
        
    def __str__(self):
        return f"Customer(name={self.name},age={self.age},address={self.address},id={self.id})"

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddress(self):
        return self.address

    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age

    def setAddress(self,address):
        self.address=address

    def setId(self,id):
        self.id=id
