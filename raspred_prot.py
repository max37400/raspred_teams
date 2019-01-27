import pandas as pd 
import numpy as np 
data=pd.read_excel('input.xlsx',encoding='utf-8') 
teams={} 
keys=[]
tr=[]
numb=int(input("Введите число команд на мероприятие:")) 
for i in range(1,numb+1): 
    teams['team{}'.format(str(i))]=[] 
    keys.append('team{}'.format(str(i)))
    print(keys)
a=np.array(data[data.columns[0]])
b=np.array(data[data.columns[1]])
c=np.array(data[data.columns[2]])
d=np.array(data[data.columns[3]])
e=np.array(data[data.columns[4]])
f=np.array(data[data.columns[5]])
 
l=list(np.concatenate((a,b,c,d,e,f),axis=0))
members=len(l)%numb
while members!=0:
    print(members)
    l.append('-')
    members=len(l)%numb
members=len(l)//numb
print("keys=",keys)
for key in keys:
    for i in range(members):
        try:
            k=len(l)
            teams[key].append(l.pop(np.random.randint(k,size=1)[0]))
        except:
            pass
data = pd.DataFrame(teams)
data.to_csv("output.csv")
