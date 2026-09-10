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
        if self.transactions:
            for transactions in self.transactions:
                if type(transactions)==Income:
                    print(f"Type:Income | Amount:{transactions.amount} | Date:{transactions.date} | Description:{transactions.description} | Income_Type:{transactions.income_type}")
                else:
                    print(f"Type:Expense | Amount:{transactions.amount} | Date:{transactions.date} | Description:{transactions.description} | Expense_Category:{transactions.category}")
        else:
            print("There are no Transactions at the moment")
    def view_balance(self):
        balance=0
        if self.transactions:
            Total_expense=0
            Total_income=0
            for transactions in self.transactions:
                if type(transactions)==Income:
                    Total_income+=transactions.amount
                elif type(transactions)==Expense:
                    Total_expense+=transactions.amount

            balance=Total_income-Total_expense
            print(f"Your Balance is: {balance}")
        else:
            print("There are no available transactions")
    
    def spending_by_category(self):
        if self.transactions:
            Total_spendings={}
            for transactions in self.transactions:
                if type(transactions)==Expense:
                    if transactions.category in Total_spendings:
                        Total_spendings[transactions.category]+=transactions.amount
                    else:
                        Total_spendings[transactions.category]=transactions.amount

            print(f"Your Total spendings are{Total_spendings}")
        else:
            print("There are no Transactions")
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
#user_menu
user = PersonalFinanceManager()
while True:
    print(f"===== PERSONAL FINANCE MANAGER =====\n\nPlease Select a choice\n1. Add Income\n2. Add Expense\n3. Add Category\n4. View Transactions\n5. View Balance\n6. Add Budget\n7. View Spending by Category\n8. Financial Summary\n9. Exit")
    try:
        choice=int(input("Enter your Choice: "))
        if choice < 1 or choice > 9:
            print("Please Select a number between 1-9") 
            continue   
    except ValueError:
        print("Please Select a number between 1-9")
        continue


    #User Adding income
    if choice==1:
        while True:
            try:
                income_user=int(input("Enter the Your Income: "))
                break
            except ValueError:
                print("Please Enter a Integer number")
        
        while True:
            income_description = input("Enter the description of your income: ")
            has_digits=any(char.isdigit() for char in income_description)
            if income_description and not has_digits:
                break
            
            print("Enter a valid description.")
        while True:
            income_type = input("Enter the Type of your income: ")
            has_digits=any(char.isdigit() for char in income_type)
            if income_type and not has_digits:
                break

            print("Enter a valid income type.")
    
        user.add_income(income_user, income_description.capitalize(), income_type.capitalize())

    #User adding expenses
    elif choice==2:
        while True:
            try:
                expense_user=int(input("Enter amount of expense: "))
                break
            except ValueError:
                print("Expense must be a number")
        while True:
            expense_description = input("Enter the description of your Expense: ")
            has_digits=any(char.isdigit() for char in expense_description)
            if expense_description and not has_digits:
                break
            
            print("Enter a valid description.")
        while True:
            expense_category = input("Enter Expese category: ")
            has_digits=any(char.isdigit() for char in expense_category)
            if expense_category and not has_digits:
                break

            print("Enter a valid expense_category.")
        
        user.add_expense(expense_user, expense_description.capitalize(), expense_category.capitalize())

    #User Adding Category
    elif choice==3:
        while True:
            user_category = input("Enter a category Name: ")
            has_digits=any(char.isdigit() for char in user_category)
            if user_category and not has_digits:
                break

            print("Enter a valid category Name.")
        while True:
            user_cat_desc = input("Enter a category Description: ")
            has_digits=any(char.isdigit() for char in user_cat_desc)
            if user_cat_desc and not has_digits:
                break

            print("Enter a valid category Description.")
        
        user.add_category(user_category.capitalize(), user_cat_desc.capitalize()) 

    #User Adding Budget
    elif choice==6:
        while True:
            try:
                budget_amount=int(input("Enter Budget Amount: "))
                break
            except ValueError:
                print("Budget must be a number")
        while True:
            budget_description = input("Enter the description of your Budget: ")
            has_digits=any(char.isdigit() for char in budget_description)
            if budget_description and not has_digits:
                break
            
            print("Enter a budget description.")
        while True:
            budget_category = input("Enter budget category: ")
            has_digits=any(char.isdigit() for char in budget_category)
            if budget_category and not has_digits:
                break

            print("Enter a valid budget_category.")
    
        user.add_budget(budget_amount, budget_category.capitalize(), budget_description.capitalize())
    # User View Transacions
    elif choice==4:
        user.view_transactions()
    elif choice==5:
        user.view_balance()
    elif choice==7:
        user.spending_by_category()
    elif choice==8:
        user.financial_summary()
    elif choice==9:
        break

 


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
        
 