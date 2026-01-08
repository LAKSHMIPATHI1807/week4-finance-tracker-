from collections import defaultdict
from datetime import datetime

def monthly_summary(expenses):
    summary=defaultdict(float)
    for e in expenses:
        month=e.date.strftime("%Y-%m")
        summary[month]+=e.amount
    return summary

def category_breakdown(expenses):
    result=defaultdict(float)
    for e in expenses:
        result[e.category]+=e.amount
    return result

def text_visualization(data):
    for key,value in data.items():
        print(f"{key:15} | {'*'*int(value/50)} ${value}")

def current_month_expense(expenses):
    current_month=datetime.now().strftime("%Y-%m")
    return sum(e.amount for e in expenses if e.date.strftime("%Y-%m") == current_month)

def expense_statistics(expenses):
    if not expenses:
        return None
    amounts=[e.amount for e in expenses]
    stats={
        'total':sum(amounts),
        'average':sum(amounts)/len(amounts),
        'maximum':max(amounts),
        'minimum':min(amounts),
        'count':len(amounts)
    }
    return stats
