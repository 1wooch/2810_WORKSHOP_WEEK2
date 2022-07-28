
# what is phillip.txt?
from ast import operator
import math
def histogram():
    total=0
    result={}
    txt=open(input("Enter file name:"),'r')
    #txt=open('test.txt','r')
    texts=txt.readlines()
    for i in range(len(texts)):
        #print(texts[i].split())
        text=texts[i].split()
        #print(text)
        for i in range(len(text)):
            #print(text[i])
            if text[i] in result:
                result[text[i]]+=1  #result[text[i].upper()]+=1
                total+=1
            elif text[i] not in result:
                result[text[i]]=1 #result[text[i].upper()]+=1
                total+=1

    #print(result)
    result=sorted(result.items(),key=lambda x:x[1],reverse=True)
    #print(type(result))#list
    #print(result[0],type(result[0])) #tuple

    for i in range(len(result)):
        print(result[i][0].upper(),str(math.trunc(result[i][1]/total*100))+'%')

   
    #print(total)
    #for key,value in result.items():
    #print(key.upper(),str(math.trunc(value/total*100))+'%')
    txt.close()
#merged Error test git  why is it too slow for this?
histogram()