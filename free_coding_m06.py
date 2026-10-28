temp = 68
change = 5
if temp + change >= 75:
    status = 'Hot'
elif temp - change < 60:
    status = 'Cold'
else:
    status = 'Mild'
print(status)
