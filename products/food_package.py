#Write your code here
from abc import ABC, abstractmethod

class FoodPackage (ABC):
    """Clase abstracta para envoltorios de comida.""" 
    @abstractmethod
    def pack(self)  -> str:
       """Nombre de el tipo de envoltorio."""
       pass
    @abstractmethod
    def material(self) -> str:
       """Material del envoltorio."""
       pass
    def describe(self):
       return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
    def pack(self):
       return "Food Warp Paper"
    def material(self):
       return "Aluminium"

class Bottle(FoodPackage):  
    def pack(self):
       return "Bottle"
    def material(self):
       return "Plastic"
      
class Glass(FoodPackage):  
    def pack(self):
       return "Glass"
    def material(self):
       return "Cardboard"

class Box(FoodPackage):
    def pack(self):
       return "Box"
    def material(self):
       return "Paper"
