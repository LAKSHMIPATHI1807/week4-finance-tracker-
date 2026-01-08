import json
import csv
import os
from expense import Expense
import shutil
from datetime import datetime

FILE_PATH="data/expenses.json"
BUDGET_FILE="data/budget.json"
BACKUP_FOLDER='data/backups'

def save_expense(expenses):
    os.makedirs("data",exist_ok=True)
    with open(FILE_PATH,"w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)
        
def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r") as f:
        data=json.load(f)
        return [Expense(**item) for item in data]
    
def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date","Amount","Category","Description"])
        for e in expenses:
            writer.writerow([e.date,e.amount,e.category,e.description])

def save_budget(amount):
    os.makedirs("data",exist_ok=True)
    with open(BUDGET_FILE, "w") as f:
        json.dump({"monthly_budget": amount}, f)
        
def load_budget():
    if not os.path.exists(BUDGET_FILE):
        return 0
    with open(BUDGET_FILE, "r") as f:
        return json.load(f).get("monthly_budget", 0)
    
def backup_expenses():
    if not os.path.exists(FILE_PATH):
        print("No expense data found to backup!")
        return
    os.makedirs(BACKUP_FOLDER,exist_ok=True)
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file=f"{BACKUP_FOLDER}/expenses_backup_{timestamp}.json"
    shutil.copy(FILE_PATH, backup_file)
    print(f"Backup created: {backup_file}")
    
def restore_expenses(backup_file):
    if not os.path.exists(backup_file):
        print("Backup file does not exist!")
        return
    shutil.copy(backup_file, FILE_PATH)
    print("Data restored successfully from backup!")
