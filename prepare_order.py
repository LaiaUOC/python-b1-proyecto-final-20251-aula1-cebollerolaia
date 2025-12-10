"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
import pandas as pd
from datetime import datetime

from users import *
from util import *
from products import *
from orders import *

    
class PrepareOrder:
    """
    Clase principal que integra la lectura de datos, la búsqueda de usuarios y 
    productos y la creación de órdenes

    Atributos:
        Lista de todos los cajeros disponibles (cashiers)
        Lista de todos los compradores disponibles (consumers)
        Lista de todos los productos disponibles (products)
    """
    def __init__(self):
        self.cashiers = self.load_cashier_list()
        self.customers = self.load_customer_list()
        self.products = self.load_product_list()

    def load_cashier_list(self) -> list[Cashier]:
        """
        Lee el CSV de cajeros y lo convierte en una lista de objetos tipo Cashier
        Imprime la descripción de todos los cajeros disponibles.
        """
        df_cashiers = CSVFileManager("data/cashiers.csv").read()
        cashier_converter = CashierConverter()
        cashier_list = cashier_converter.convert(df_cashiers)
        cashier_converter.print(cashier_list)
        return cashier_list
    
    def load_customer_list(self) -> list[Customer]:
        """
        Lee el CSV de compradores y lo convierte en una lista de objetos tipo Customer
        Imprime la descripción de todos los compradores diponibles.
        """
        df_customers = CSVFileManager("data/customers.csv").read()
        customer_converter = CustomerConverter()
        customer_list = customer_converter.convert(df_customers)
        customer_converter.print(customer_list)
        return customer_list
  
    def load_product_list(self) -> list[Product]:
        """
        Lee los distintos CSV de productos (drinks, hamburgers, happyMeal y sodas)
        y los integra en una sola lista de objetos tipo Product.
        Imprime la descripción de todos los productos disponibles
        """
        df_drinks = CSVFileManager("data/drinks.csv").read()
        df_hamburgers = CSVFileManager("data/hamburgers.csv").read()
        df_happyMeal = CSVFileManager("data/happyMeal.csv").read()
        df_sodas = CSVFileManager("data/sodas.csv").read()

        product_converter = ProductConverter()
        product_list = (product_converter.convert(df_drinks, "Drink") +
                        product_converter.convert(df_hamburgers, "Hamburguesa") +
                        product_converter.convert(df_happyMeal, "HappyMeal") +
                        product_converter.convert(df_sodas, "Soda"))
        product_converter.print(product_list)
        return product_list
    
    def ask_for_cashier(self) -> Cashier:
        """Pide por teclado el DNI del cajero hasta que coincida con un cajero existente"""
        while True:
            dni = input("Introduce DNI cashier: ")
            cashier = self.find_cashier(dni)
            if cashier is not None:
                print(cashier.describe())
                return cashier
            print("Cashier not found. Try again.")


    def find_cashier(self, dni: str ) -> Cashier:
        """Devuelve el cajero con el DNI indicado (dni), o None si no existe"""
        for cashier in self.cashiers:
             if str(cashier.dni) == dni:
                return cashier

    def ask_for_customer(self) -> Customer:
        """Pide por teclado el DNI del cliente hasta que encuentre uno que este en la lista existente"""  
        while True:
            dni = input("Introduce DNI customer: ")
            customer = self.find_customer(dni)
            if customer is not None:
                print(customer.describe())
                return customer 
            print("Customer not found. Try again.")   
        
    def find_customer(self, dni: str) -> Customer:
        """Devuelve el Customer con el DNI indicado, o None si no existe"""
        for customer in self.customers:
            if str(customer.dni) == dni:
                return customer

    def find_product(self, product_id: str) -> Product:
        """Devuelve el Product con el ID indicado, o None si no existe"""
        for product in self.products:
            if str(product.id) == product_id:
                return product  

    def show_products(self):
        """Musestra por pantalla todos los productos disponibles"""
        print("Product list:")
        for product in self.products:
            print(product.describe())

    def select_products(self) -> list[Product]:
        """
        Permite al usuario seleccionar productos por ID
        
        Pregunta por un ID de producto, lo busca y, si existe, lo añade a 
        la selección existente. Se detiene cuando el usuario responde que 
        no quiere añadir más productos
        """
        selected_products = []
        while True:
            product_id = input("Introduce product ID: ")
            product = self.find_product(product_id)
            if product is not None:
                print(product.describe())
                selected_products.append(product)
            else:
                print("Product not found.")
            if input("Do you want to add another product (yes/no)? ").lower() != "yes":
                break
        return selected_products
            
    def prepare_order(self):
        """
        Flujo principal para preparar una orden:

        - Muestra los productos
        - Pide cajero y cliente
        - Permite seleccionar productos
        - Crea la orden, la muestra por pantalla y la guarda en un CSV
        """
        self.show_products() #Muestra todos los productos disponibles por pantalla
        cashier = self.ask_for_cashier() #Busca cajero pedido por pantalla (si no existe vuelve a pedirlo)
        customer = self.ask_for_customer() #Busca cliente pedido por pantalla (si no existe vuelve a pedirlo)

        order = Order(cashier, customer) #Crea la orden con el cajero y el cliente seleccionados

        product_list = self.select_products() #Selecciona los productos que van a formar parte de la orden
        for product in product_list:
            order.add(product) #Añade los productos a la orden

        order.show() #Muestra la información de la orden por pantalla

        #Guarda la información de la orden al final de orders.csv
        CSVFileManager("orders.csv").write(pd.DataFrame([{"DNI cajero": cashier.dni,
                                                        "DNI comprador": customer.dni,
                                                        "Fecha y hora": datetime.now(),
                                                        "Total": order.calculateTotal()}]))

PrepareOrder().prepare_order()
