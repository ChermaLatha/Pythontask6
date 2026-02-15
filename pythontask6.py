#problem1:
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount >0:
          self.__balance+=amount
          print(f"Deposited:{amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount <=0:
            print("Invalid withdrawal amount")
        elif amount >self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn:{amount}")
class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=self.get_balance()*self.interest_rate/100
        print(f"Interest amount:{interest}")
        return interest
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
       super().__init__(account_number, balance)
       self.minimum_balance=minimum_balance
    def withdraw(self,amount):
        if self.get_balance()-amount < self.minimum_balance:
            print("Minimum balance required.Cannot withdraw your amount")
        elif amount<=0:
            print("Invalid withdrawal amount")
        else:
            super().withdraw(amount)
print("SAVINGS ACCOUNT")
savings=SavingsAccount("SBI12345",10000,5)
savings.deposit(2000)
savings.withdraw(3000)
savings.calculate_interest()
print("Balance Amount:",savings.get_balance())
print("\nCURRENT ACCOUNT")
current=CurrentAccount("CRSBI1234",15000,5000)
current.withdraw(10000)
current.withdraw(3000)
print("Balance:",current.get_balance())

#problem2
#Base Class
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_salary(self):
        return self.salary
#Derived classes
class RegularEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self,):
        return self.salary
class ContractEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name,0)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        return self.hourly_rate *self.hours_worked
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name, salary)
    def calculate_salary(self):
        return self.salary
employees=[RegularEmployee("Latha",4000),
           ContractEmployee("Cherma",3000,60),
           Manager("Chermalatha",100000)]
for emp in employees:
    print(f"{emp.__class__.__name__}\n  Name:{emp.name}\n Salary:{emp.calculate_salary()}")

# Problem 3
class Vehicle:
    def __init__(self,model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate
    def calculate_rental(self,days):
        self.days=days
class Car(Vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, days):
        return self.rental_rate * days

class Bike(Vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, days):
        return self.rental_rate * days
class Truck(Vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)
    def calculate_rental(self, days):
        return self.rental_rate * days
rental_days=int(input("Enter rental duration in Days:"))
vehicles = [
    Car("TataMotors", 2000 ),
    Bike("Yamaha", 800 ),
    Truck("Tata Truck", 5000)
]
# Polymorphism in action
for vehicle in vehicles:
    print(f"{vehicle.__class__.__name__}  \n Model: {vehicle.model}, \n "
          f"Rental Cost for {rental_days} days: {vehicle.calculate_rental(rental_days)}")