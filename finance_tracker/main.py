from expense import Expense,ExpenseManager
from file_handler import save_expense,load_expenses,export_to_csv,backup_expenses,restore_expenses
from reports import monthly_summary,category_breakdown,text_visualization,current_month_expense,expense_statistics
from file_handler import save_budget,load_budget

manager=ExpenseManager()
manager.expenses=load_expenses()

def display_expenses(expenses):
            if not expenses:
                print("No expenses found!")
                return
            print("\nIndex   |  Date           | Amount  |  Category         | Description")
            print("-"*80)
            for i,e in enumerate(expenses):
                print(f"{i:<5}   | {e.date}      | {e.amount:<6}  | {e.category:<12}      | {e.description}")

def display_statistics(stats):
    if not stats:
        print("No expenses available for statistics!")
        return
    print("\n --- Expense Statistics ---")
    print(f"Total Expenses     :{stats['total']}")
    print(f"Average Expense    :{stats['average']}")
    print(f"Highest Expense    :{stats['maximum']}")
    print(f"Lowest Expense     :{stats['minimum']}")
    print(f"Number of Entries  :{stats['count']}")

def menu():
    print("-"*40)
    print("              MAIN MENU")
    print("-"*40)
    print("\n --- Expense Tracker ---")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Generate Monthly Report")
    print("5. View Category Breakdown")
    print("6. Set/Update Budget")
    print("7. Export Data to CSV")
    print("8. View Statistics")
    print("9. Backup/Restore Data")
    print("0. Exit")
while True:
    menu()
    choice = input("Enter your Choice(0-9): ")
    
    if choice=="1":
        date=input("Date (YYYY-MM-DD): ")
        amount=input("Amount: ")
        category=input("Category: ")
        desc=input("Description: ")
        try:
            expense=Expense(date,amount,category,desc)
            manager.add_expense(expense)
            save_expense(manager.expenses)
            budget=load_budget()
            spent=current_month_expense(manager.expenses)
            if budget>0:
                print(f"Budget: {budget} | Spent: {spent}")
                if spent>budget:
                    print("Monthly budget exceeded!")
            print("Expense added successfully!")
        except Exception as e:
            print("Error: ",e)
        
            
    elif choice=="2":
        expense=manager.view_all_expenses()
        display_expenses(expense)
        
    elif choice == "3":
        category=input("Enter category to Search: ")
        manager.search_by_category(category)
        
    elif choice=="4":
        report=monthly_summary(manager.expenses)
        text_visualization(report)
        
    elif choice == "6":
        try:
            budget=float(input("Enter monthly budget amount: "))
            if budget<=0:
                raise ValueError
            save_budget(budget)
            print(f"Monthly budget set to {budget}")
        except:
            print("Invalid budget amount!")
            
    elif choice=="5":
        report=category_breakdown(manager.expenses)
        text_visualization(report)
        
    elif choice=="7":
        export_to_csv(manager.expenses)
        print("Exported to CSV!")
        
    elif choice =="8":
        stats=expense_statistics(manager.expenses)
        display_statistics(stats)
        
    elif choice =="9":
        backup_expenses()
        backup_name=input("Enter backup file path: ")
        restore_expenses(backup_name)
        manager.expenses=load_expenses()
        
    elif choice =="0":
        break