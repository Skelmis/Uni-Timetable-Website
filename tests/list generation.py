base = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

newList = []

for i in range(4):
    x = i + 8
    for item in base:
        payload = f"{item}{x}am"
        newList.append(payload)

for i in range(5):
    if i == 0:
        x = 12
    else:
        x = i
    for item in base:
        payload = f"{item}{x}pm"
        newList.append(payload)

print(newList)
print(len(newList))
