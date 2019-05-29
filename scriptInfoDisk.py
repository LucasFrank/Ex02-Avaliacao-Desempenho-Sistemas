import pandas as pd

columns = ['Device','r/s','w/s','rkB/s','wkB/s','rrqm/s','wrqm/s','%rrqm','%wrqm','r_await','w_await','aqu-sz','rareq-sz','wareq-sz','svctm','%util']

df = pd.read_csv('result.txt', delimiter=r"\s+", names = columns)

df = df[:386]

for i  in df:
    df[i] = df[i].str.replace(',', '.')

print(df)
df.to_csv('resultDisk.csv', index = False)

exit(0)

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
