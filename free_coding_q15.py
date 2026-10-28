balance = 100
fee = 30
if balance - fee >= 80:
    balance = balance - fee
else:
    fee = 10
    balance = balance - fee
print(balance)
print(fee)
