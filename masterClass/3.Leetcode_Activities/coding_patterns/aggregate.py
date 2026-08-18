transactions = [
    {"user": "A", "amount": 100},
    {"user": "B", "amount": 50},
    {"user": "A", "amount": 75}
]

def totals(transactions):
    
    result = {}
    
    for tx in transactions:
        user = tx['user']
        amount = tx['amount']
        
        result[user] = result.get('user', 0 ) + amount
        
    return result