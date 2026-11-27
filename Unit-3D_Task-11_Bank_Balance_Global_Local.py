balance = 1000  # e.g. 1000


def deposit(amount):
    global balance
    balance = balance + amount
    print("After deposit, balance =", balance)


def show_local_balance():
    balance = 0  # local only, e.g. 0
    print("Inside local function, balance =", balance)


print("Start:", balance)
deposit(500)  # e.g. 500
print("Account balance:", balance)
show_local_balance()
print("Account balance still:", balance)