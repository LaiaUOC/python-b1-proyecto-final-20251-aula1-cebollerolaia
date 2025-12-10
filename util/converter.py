from abc import ABC, abstractmethod
#Write your code here
from users import *
from products import *

class Converter(ABC):
  """Clase abstracta para convertir DataFrames en listas de objetos."""
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      """
      Convierte un DataFrame en una lista de objetos corresponsiente.
      Los parámetros adicionales (*args) premiten pasar inforamción adicional (ej. tipo de producto)"""
      pass  
  def print(self, objects):
    """Imprime la descripción de cada objeto convertido."""
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  """Convierte un DataFrame en una lista de objetos de tipo Cashier."""
  def convert(self,dataFrame): 
    cashiers = []
    for row in dataFrame.itertuples(): #Recorremos el DataFrame fila a fila, creando un Cashier para cada fila
      cashiers.append(Cashier(row.dni, row.name, row.age, row.timetable, row.salary))
    return cashiers  

class CustomerConverter(Converter):
  """Convierte un dataFrame en una lista de objetos tipo Customer"""
  def convert(self, dataFrame):
    customers = []
    for row in dataFrame.itertuples(): #Recorremos el DataFrame fila a fila, creando un Customer para cada fila
      customers.append(Customer(row.dni, row.name, row.age, row.email, row.postalcode))
    return customers

class ProductConverter(Converter):
  """Convierte un DataFrame en una lista de objetos Product"""
  def convert(self, dataFrame, type):
    #El argumento type indica que tipo de producto debemos crear (Hamburger, Soda, Drink o HappyMeal)
    products = []
    if type == "Hamburguesa":
      for row in dataFrame.itertuples():
        products.append(Hamburger(row.id, row.name, row.price))
    elif type == "Soda":
      for row in dataFrame.itertuples():
        products.append(Soda(row.id, row.name, row.price))
    elif type == "Drink":
      for row in dataFrame.itertuples():
        products.append(Drink(row.id, row.name, row.price))
    elif type == "HappyMeal":
      for row in dataFrame.itertuples():
        products.append(HappyMeal(row.id, row.name, row.price))
    return products