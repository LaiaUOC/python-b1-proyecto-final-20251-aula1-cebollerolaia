from abc import ABC, abstractmethod
#Write your code here
from .food_package import *

class Product(ABC):
    """
    Clase abstracta que representa un producto generico
    Atributos:
        Identificador del producto (id)
        Nombre del producto (name)
        Precio del producto (price)
    """
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        """Devuelve una cadena con toda la información del producto."""
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        """Describe el tipo de producto."""
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        """Devuelve el tipo de envoltorio asociado al producto."""
        pass  

class Hamburger(Product):
    # Producto de tipo "Hamburguesa" que se entrega en Wrapping
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    # Producto tipo "Soda" que se entrega en botella
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Soda"
    def foodPackage(self) -> FoodPackage:
        return Bottle()    

class Drink(Product):
    # Producto tipo "Drink" que se entrega en vaso
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Drink"
    def foodPackage(self) -> FoodPackage:
        return Glass()

class HappyMeal(Product):
    # Producto tipo HappyMeal que se entrega en caja
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "HappyMeal"
    def foodPackage(self) -> FoodPackage:
        return Box()