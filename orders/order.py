from users import *
from products import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    """Añade un producto a la lista de productos de la orden."""
    self.products.append(product)

  def calculateTotal(self) -> float:
    """Calcula el precio total de la orden."""
    return sum(product.price for product in self.products)
  
  def show(self):
    """Muestra por pantalla la inforamción de la orden."""    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal()}")
