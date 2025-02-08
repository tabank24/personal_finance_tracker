import json

def load_transactions():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_transaction(amount, category):
    transactions = load_transactions()
    transactions.append({"amount": amount, "category": category})
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)

add_transaction(50, "Food")
