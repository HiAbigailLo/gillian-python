stock = 12
order = 5
if stock - order >= 10:
    stock = stock - order
    status = 'OK'
else:
    stock = stock - order
    stock = stock + 20
    status = 'Restocked'
print(stock)
print(status)
