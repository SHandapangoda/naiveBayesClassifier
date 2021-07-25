from itertools import count
from numpy.lib.function_base import append
from sklearn import datasets


datasets =[
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,0],
    ]

mp = dict()

#data seperation
for i in range(len(datasets)):
    row = datasets[i]
    y = row[-1]

    if (y not in mp):
        mp[y] = list()
    
    mp[y].append(row)

for label in mp:
    print(label)
    for row in mp[label]:
        print(row)

test = [2,2,1,0]

# naive bayes algo
chance = 1 

count = 0
total = 0

for row in datasets:
    if (row[-1] == 1):
        count += 1
    total += 1
    print("feature" +str(count)+ "/" +str(total))
    chance *= count / total

noChance = 1

count = 0 
total = 0

for row in datasets:
    if(row[-1] == 0):
        count += 1
    total += 1
    print("feature" +str(count)+ "/" +str(total))
    noChance *= count / total

for i in range(len(test)):
    count = 0
    total = 0

    for row in mp[0]:
        if(test[i] == row[i]):
            count += 1
        total +=  1
    
    print('feature' +str(i+1))
    print(str(count)+" / "+str(total))
    noChance *= count/total