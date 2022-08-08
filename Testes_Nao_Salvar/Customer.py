from datetime import datetime

class Customer:
    
    """
      My test with new instructions in OO with Python
      CamelCaseNames for class names
      name_second_name_third_name for attributes and methods
    """

    def __init__(self, name, salary, balance=0):
      self.name = name
      self.salary = salary
      self.balance = balance
      self.hire_date = datetime.today()
      print("Seu usuário foi instanciado com sucesso!")


    def set_name(self,new_name):
      self.name = new_name

    def set_salary(self,new_salary):
      self.salary = new_salary

    def set_balance(self,new_balance):
      self.balance = new_balance


    def identify(self):
      print('This is the customer: ' + self.name)
      print('The salary is: ' + str(self.salary))
      print('The balance is: ' + str(self.balance))
      print('Hired in: ' + str(self.hire_date.date()))
