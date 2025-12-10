from abc import ABC, abstractmethod

class User(ABC):
  """
  Clase abstracta que representa un usuario genérico (persona)
  Atributos:
    Documento de identidad del usuario (dni)
    Nombre del usuario (name)
    Edad del usuario (age)
  """
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      """Devuelve una descripción en texto del usuario"""
      pass

class Cashier(User): 
  """
  Representa a un cajero
  Atributos específicos de la subclase Cashier:
    Horario del cajero (timeTable)
    Salario del cajero (salary)
  """
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
    super().__init__(dni, name, age)
    self.timeTable = timeTable
    self.salary = salary  
 
  def describe(self):
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

class Customer(User):
  """
  Representa a un cliente del establecimiento
  Atributos específicos de la subclase Customer:
    Correo electrónico del cliente (email)
    Código postal del cliente (postal code)
  """
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
    super().__init__(dni, name, age)
    self.email = email
    self.postalCode = postalCode


  def describe(self):
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"