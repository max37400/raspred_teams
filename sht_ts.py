import pandas as pd
import random as rnd
data=pd.read_csv("t_santa_loc.csv")
data=data[data.columns[1:]]
ind=list(range(0,len(data[data.columns[0]])))
ind_1=[]
while len(ind)!=0:
    i=rnd.randint(0,len(ind)-1)
    ind_1.append(ind.pop(i))
s=''
for i in range(len(ind_1)-1):
    s+=str(i+1)+' '+str(data[data.columns[0]][ind_1[i]])+'-->'+str(data[data.columns[0]][ind_1[i+1]])+'\n'
s+=str(len(ind_1))+' '+str(data[data.columns[0]][ind_1[-1]])+'-->'+str(data[data.columns[0]][ind_1[0]])
handle = open("spisok.txt", "w")
handle.write(s)
handle.close()
for i in range(len(ind_1)):
    f=open(str(i)+'.txt','w',encoding='utf8')
    s=''
    s+="Send to: "+str(data[data.columns[-1]][ind_1[i]])+'\n\n\n'
    s+='Привет, штшник!'+'\n\n'
    s+="На этой неделе ты сможешь почувствовать себя в роли заботливого Дедушки Мороза,\nкоторый выбирает и упаковывает подарок на Новый Год своему подопечному.\nОтнесись к своей миссии с полной серьезностью, ведь именно от тебя зависит новогоднее настроение подопечного штшника."
    s+='\n'+"Ниже ты увидишь имя того, кому ты даришь подарок, а также некоторую информацию о нем.\n\n"
    try:
        s+='Имя: '+str(data[data.columns[0]][ind_1[i+1]])+'\n'
        s+="Ссылка вк: " + str(data[data.columns[1]][ind_1[i+1]])+'\n'
        s+="Три факта: " + str(data[data.columns[2]][ind_1[i+1]])+'\n'
        s+="Что главное в подарке: "+str(data[data.columns[3]][ind_1[i+1]])
        s+="\nКонкретный подарок: "+str(data[data.columns[4]][ind_1[i+1]])
        s+='\nЧто нельзя дарить: '+str(data[data.columns[5]][ind_1[i+1]])
        s+='\n\nJingle Bells!'
        
    except IndexError:
        i=-1
        s+='Имя: '+str(data[data.columns[0]][ind_1[i+1]])+'\n'
        s+="Ссылка вк: " + str(data[data.columns[1]][ind_1[i+1]])+'\n'
        s+="Три факта: " + str(data[data.columns[2]][ind_1[i+1]])+'\n'
        s+="Что главное в подарке: "+str(data[data.columns[3]][ind_1[i+1]])
        s+="\nКонкретный подарок: "+str(data[data.columns[4]][ind_1[i+1]])
        s+='\nЧто нельзя дарить: '+str(data[data.columns[5]][ind_1[i+1]])
        s+='\n\nJingle Bells!'
    f.write(s)
    print(i)    
    f.close()
        
