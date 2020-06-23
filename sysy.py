#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("hello")


# In[ ]:


nums=[]
for i in :
    nums=i
    print(nums)


# In[ ]:


str=input("Number? ")
nums=[]
for num in str.split():
    nums.append(int(num))
print("Max = ",max(nums))


# In[ ]:


d={}
arr=list()
for i in range(0,10,1):
    arr=input("Input: ").split()
    d[arr[0]]=arr[1]
print(d.get(input("Name? ")))
str=input("Phone? ")
for name,phone in d.items():
    if phone==str:
        print(name)


# In[11]:


str1=""
a=input("암호화: ")
a.replace("\t"," ")
arr1=a.split()
arr1.reverse()
for i in arr1:
    for j in i[::1]:
        j2=ord(j)
        j2+=1
        j=chr(j2)
        str1+=j
    str1+=" "
print(str1)
str2=""
b=input("복호화: ")
b.replace("\t"," ")
for l in b[::1]:
    if l == " ":
        str2+=" "
    else:
        l2=ord(l)
        l2-=1
        l=chr(l2)
        str2+=l
arr2=str2.split()
arr2.reverse()
print(' '.join(arr2))


# In[44]:


class STACK:
    def __init__(self):
        self.s=[]
    def push(self,a):
        self.s.append(a)
    def pop(self):
        if len(self.s)<1:
            print("stack empty")
        return self.s.pop()
    def peek(self):
        return self.s[-1]
    def istwo(self):
        if len(self.s)>=2:
            return True
n=STACK()
e=STACK()

string=input("식 입력:")
slist=string.split()
for index,i in enumerate (slist[::]):
    if i=='+' or i=='-' or i=='*' or i=='/':
        e.push(i)
    else:
        n.push(i)
        while n.istwo():
            e1=e.peek()
            if e1=='+':
                if len(slist)==index+1:
                    e.pop()
                    n1=int(n.pop())
                    n2=int(n.pop())
                    #print(n1+n2)
                    n.push(n1+n2)
                    #print(n.peek())
                else:
                    if slist[index+1]=='*' or slist[index+1]=='/':
                        break
                    else:
                        e.pop()
                        n1=int(n.pop())
                        n2=int(n.pop())
                        n.push(n1+n2)
            elif e1=='-':
                if len(slist)==index+1:
                    e.pop()
                    n1=int(n.pop())
                    n2=int(n.pop())
                    n.push(n1-n2)
                else:
                    if slist[index+1]=='*' or slist[index+1]=='/':
                        break
                    else:
                        e.pop()
                        n1=int(n.pop())
                        n2=int(n.pop())
                        n.push(n2-n1)
            elif e1=='*':
                e.pop()
                n1=int(n.pop())
                n2=int(n.pop())
                print(n1*n2)
                n.push(n1*n2)
            else :
                e.pop()
                n1=int(n.pop())
                n2=int(n.pop())
                n.push(n2/n1)
print("답:",n.pop())
    


# In[53]:


import numpy as np
file_path='SMSSpamCollection.txt'

r=open(file_path,"r",encoding="utf8")
lines=r.readlines()

lines=lines[:100]
x_data,y_data=[],[]
for line in lines:#한줄씩 읽어옴
    str(line)
    print(line)
    piece=line.split("\t")
    y,x=piece[0],piece[1]
    x_data.append(x)
    y_data.append(y)
    
print(len(x_data))
print(len(y_data))


# In[54]:


from keras.preprocessing.text import Tokenizer
tokenizer=Tokenizer()

labeling={'spam':0,'ham':1}
index_x,index_y=[],[]
for y in y_data:
    index_y.append(labeling[y])#라벨
tokenizer.fit_on_texts(x_data)
max_length=60
for index in range(len(index_x)):
    length=len(index_x[index])
    if length >= max_length:
        index_x=index_x[:60]
    else:
        llen=max_length-length
        index_x+([0]*llen)


# In[58]:


llist=[1,2,3,4,4]
if len(llist)>=6:
    llist[:6]
else:
    
print(llist)


# In[ ]:




