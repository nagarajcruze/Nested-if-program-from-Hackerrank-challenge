mainlist = []
minimum = 0
mini = None
for i in range(int(input())):
    name = input()
    score = float(input())
    l =[float(score),name]
    mainlist.append(l)
    mainlist.sort()

for i in mainlist:
    minimum=i[0]
    if mini == None:
        mini = minimum
        continue
    if minimum>mini:
        mini = minimum
        break
for i in mainlist:
    if mini == i[0]:
        print(i[1])
