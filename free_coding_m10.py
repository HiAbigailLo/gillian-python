distance = 100
time = 8
if distance / time > 15:
    label = 'Fast'
elif distance / time > 10:
    label = 'Moderate'
else:
    label = 'Slow'
print(label)
