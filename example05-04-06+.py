blow = 0
for i in range(4):
    if int(b[0] == a[i]):
        blow = blow + 1
        break
if (int(b[0] == a[i]) and (a[i] != int(b[i])) and (a[0] != int(b[0])):

blow = 0
for i in range(4):
    if(int(b[0]) == a[i]) and (a[i] != int(b[i])) and (a[0] != int(b[0])):
        blow = blow + 1
        break
for i in range(4):
    if(int(b[1]) == a[i]) and (a[i] != int(b[i])) and (a[1] != int(b[1])):
        blow = blow + 1
        break
for i in range(4):
    if(int(b[2]) == a[i]) and (a[i] != int(b[i])) and (a[2] != int(b[2])):
        blow = blow + 1
        break
for i in range(4):
    if(int(b[3]) == a[i]) and (a[i] != int(b[i])) and (a[3] != int(b[3])):
        blow = blow + 1
        break

blow = 0
for j in range(4):
    for i in range(4):
        if(int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
            blow = blow + 1
            break

