level = 3
xp = 250
if xp >= 300:
    level = level + 2
elif xp >= 200:
    level = level + 1
    xp = xp - 200
else:
    xp = 0
print(level)
print(xp)
