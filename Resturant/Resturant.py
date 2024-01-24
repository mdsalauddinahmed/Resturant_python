class Resturant:
    def __init__(self,name,rent,menu =[]) -> None:
        self.name=name
        self.chef=None
        self.orders=[]
        self.server=None
        self.rent=rent
        self.Manager=None
        self.menu =menu
        self.revenue = 0
        self.expense =0
        self.balance =0
        self.profit = 0

    def add_employee(self,employee_type,employee):
        if employee_type =='chef':
            self.chef=employee
        elif employee_type =='server':
            self.server=employee

        elif employee_type =='Manager':
            self.Manager=employee
    
    def add_oreders(self,order):
        self.orders.append(order)

    def received_payment(self,order,amount,customer):
        
        if amount>=order.bill:
            self.revenue +=order.bill
            self.balance +=order.bill
            customer.bill_due = 0
            return amount - order.bill
        else:
            print('not enough money')
    
    def pay_expanse(self,amount,description):
         if amount < self.balance:
             self.expense +=amount
             self.balance -=amount
             print(f'Expanse {amount} for {description}')
         else:
             print(f'Not enough money to pay {amount}')

    def pay_salary (self,employee):
        if employee.salary <self.balance:
            employee.receive_salary()

    def show_employee(self):
        print('------Showing All Employers----')
        print(" ")

        if self.chef is not None:
            print(f'Chef : {self.chef.name} with salary :{self.chef.salary}')
        if self.Manager is not None:
            print(f'Manager :{self.Manager.name} with salary:{self.Manager.salary}')
        if self.server is not None:
            print(f'Manager :{self.server.name} with salary:{self.server.salary}')