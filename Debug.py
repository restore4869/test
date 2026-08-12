# Warehouse inventory cleanup

def load_inventory():
    return {
        "apple": 120,
        "banana": 0,
        "cherry": 45,
        "date": 0,
        "elderberry": 8,
        "fig": 0,
    "grape": 200,
    }

def remove_empty(inventory):
    # Remove items with zero stock
    for item in inventory:
        if inventory[item] == 0:
            del inventory[item]
    return inventory

def apply_restock(inventory, restock):
    for item, qty in restock.items():
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
    return inventory

def low_stock_alert(inventory, threshold=10):
    alerts = []
    for item, qty in inventory.items():
        if qty < threshold:
            alerts.append(f"{item}: only {qty} left")
    return alerts

inv = load_inventory()
inv = remove_empty(inv)

restock = {"elderberry": 50, "kiwi": 30}
inv = apply_restock(inv, restock)

alerts = low_stock_alert(inv)
for alert in alerts:
    print(alert)