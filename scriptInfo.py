import pandas as pd

#df = pd.read_csv('info.txt', delimiter=r"\s+")

file = open('result.txt')

t = 0
columns = None
dfAux = []
for row in file:
    if t == 0:
        columns = row.split()
        columns = [c.replace('-03','time') for c in columns]
        t += 1
    else:
        dfRow = []
        rowSplit = row.split()
        for i in range(len(rowSplit) - 2):
            dfRow.append(rowSplit[i])
        time = rowSplit[len(rowSplit) - 1] + ' ' + rowSplit[len(rowSplit) - 2]
        dfRow.append(time)
        dfAux.append(dfRow)

df = pd.DataFrame(dfAux, columns = columns)

df.to_csv('result.csv', index = False)
