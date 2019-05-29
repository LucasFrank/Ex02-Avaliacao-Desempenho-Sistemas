import pandas as pd
import numpy as np

def busyTime(us):
    count  = 0
    busyTimeList = []
    for i in us:
        if i > 10:
            count += 1
        elif count != 0:
            busyTimeList.append(count)
            count = 0

    return busyTimeList


df = pd.read_csv('result.csv')
df['time'] = pd.to_datetime(df['time'])

T = df['time'][387] - df['time'][0]
T = T.total_seconds() # tempo de execução da compressão

btlist = busyTime(df['us'])
busyTimeCPU = np.mean(btlist)

print('CPU Average Util: {} '.format(np.mean(df['us'][:387])))
