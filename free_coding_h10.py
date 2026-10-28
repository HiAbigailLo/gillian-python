x = 4
y = 7
if x * 2 > y:
    x = x + y
else:
    y = y - x
if x + y > 20:
    print('High')
elif x + y > 12:
    print('Mid')
else:
    print('Low')
print(x)
print(y)
