# A persnal finance manager project
# class for transactions
from datetime import datetime
class Transaction:
    def __init__(self,amount,description):
        self.amount=amount
        self.date=datetime.now()
        self.description=description
#income class
class Income(Transaction):
    def __init__(self, amount,description,income_type):
        super().__init__(amount, description)
        self.income_type=income_type
#expense class
class Expense(Transaction):
    def __init__(self, amount,description,category):
        super().__init__(amount,description)
        self.category=category
#category class
class Category:
    def __init__(self,name,description):
        self.name=name
        self.description=description
#budget class
class Budget:
    def __init__(self,amount,category,description):
        self.amount=amount
        self.category=category
        self.description=description
#PersonalFinanceManagerClass
class PersonalFinanceManager:
    def __init__(self):
        self.transactions=[]
        self.categories=[]
        self.budgets=[]

    def add_income(self, amount,description, income_type):
        income = Income(amount,description, income_type)
        self.transactions.append(income)

    def add_expense(self,amount,description,category):
        expense=Expense(amount,description,category)
        self.transactions.append(expense)

    def add_category(self,name,description):
        category=Category(name,description)
        self.categories.append(category)

    def add_budget(self,amount,category,description):
        budget=Budget(amount,category,description)
        self.budgets.append(budget)

    def view_transactions(self):
        for transactions in self.transactions:
            if type(transactions)==Income:
                print(f"Type:Income | Amount:{transactions.amount} | Date:{transactions.date} | Description:{transactions.description} | Income_Type:{transactions.income_type}")
            else:
                print(f"Type:Expense | Amount:{transactions.amount} | Date:{transactions.date} | Description:{transactions.description} | Expense_Category:{transactions.category}")

    def view_balance(self):
        balance=0
        Total_expense=0
        Total_income=0
        for transactions in self.transactions:
            if type(transactions)==Income:
                Total_income+=transactions.amount
            elif type(transactions)==Expense:
                Total_expense+=transactions.amount

        balance=Total_income-Total_expense
        return f"Your Balance is: {balance}"
    
    def spending_by_category(self):
        Total_spendings={}
        for transactions in self.transactions:
            if type(transactions)==Expense:
               if transactions.category in Total_spendings:
                   Total_spendings[transactions.category]+=transactions.amount
               else:
                   Total_spendings[transactions.category]=transactions.amount

        return Total_spendings
    
    def financial_summary(self):
        Total_expense=0
        Total_income=0
        for transactions in self.transactions:
            if type(transactions)==Income:
                Total_income+=transactions.amount
            elif type(transactions)==Expense:
                Total_expense+=transactions.amount

        return (f"====FINANCIAL SUMARRY====\n\nTotal Income: {Total_income}\nTotal Expense:{Total_expense}\nTotal Balance: {self.view_balance()}\nTotal Spendings:{self.spending_by_category()}")

    def view_categories(self):
        for category in self.categories:
            print(f"The categories include\n\nCategory Name:{category.name} - {category.description}\n")
            
    def view_budgets(self):
            for budget in self.budgets:
                print(f"The Budgets include\n\nBudget Amount:{budget.amount} - {budget.category} - {budget.description} \n")
while True:
    try:
        income_user=int(input("Enter the Your Income: "))
        break
    except ValueError:
        print("Please Enter a Integer number")

user = PersonalFinanceManager()
user.add_income(income_user, "Monthly salary", "Employment")
user.add_expense(8000, "House rent", "Rent")
user.view_transactions()



'''
manager = PersonalFinanceManager()

manager.add_income(50000, "2026-09-01", "Monthly salary", "Employment")
manager.add_income(10000, "2026-09-03", "Freelance website", "Freelance")

manager.add_expense(8000, "2026-09-02", "House rent", "Rent")
manager.add_expense(5000, "2026-09-04", "Groceries", "Food")
manager.add_expense(2000, "2026-09-05", "Transport", "Transport")

manager.add_category("Food", "Food and groceries")
manager.add_category("Transport", "Daily transportation")

manager.add_budget(10000, "Food", "Monthly food budget")


manager.view_categories()
manager.view_budgets()
'''
        
 