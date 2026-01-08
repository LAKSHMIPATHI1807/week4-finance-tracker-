from datetime import datetime

class Expense:
    def __init__(self,date,amount,category,description):
        self.date=self.validate_date(date)
        self.amount=self.validate_amount(amount)
        self.category=category
        self.description=description
        
    def validate_date(self,date):
        try:
            return datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD")
        
    def validate_amount(self,amount):
        amount=float(amount)
        if amount<=0:
            raise ValueError("Amount must be greater than zero")
        return amount
    
    def to_dict(self):
        return {
            "date":str(self.date),
            "amount":self.amount,
            "category":self.category,
            "description":self.description
        }

class ExpenseManager:
    def __init__(self):
        self.expenses=[]
        
    def add_expense(self,expense):
        self.expenses.append(expense)
        
    def remove_expense(self,index):
        self.expenses.pop(index)
        
    def search_by_category(self,category):
        return [e for e in self.expenses if e.category.lower()==category.lower()]
    
    def view_all_expenses(self):
        return self.expenses