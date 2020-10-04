import re
import matplotlib.pyplot as plt
import numpy as np

def getNumbers(data):
    i=0
    k=0
    times=[]
    for word in data:
        timee = re.findall('\d*', word)
        for time in timee:
            if time!='':
                times.append(time)
            
    return times
    
def toFile(t, f):
    count=0
    for time in t:
        f.write(time+'\n')
        count+=1
    return count

with open("ping.txt", 'r') as f:
    data=f.read()
    data = re.findall('ўаҐ¬п=\d*', data )
    
file_result = open('result.txt', 'w')

times = getNumbers(data)
count = toFile(times, file_result)

times = [int(time) for time in times]
    
x = [i for i in range (99, 141)]

fig = plt.figure()
plt.hist(times, x)
plt.title('Simple histogramm')
plt.grid(True)

f.close
