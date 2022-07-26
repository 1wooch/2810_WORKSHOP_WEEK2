
# what is phillip.txt?
def histogram():
    
    result={}
    txt=open(input("Enter file name:"),'r')
    #txt=open('test.txt','r')
    texts=txt.readlines()
    for i in range(len(texts)):
        #print(texts[i].split())
        text=texts[i].split()
        for i in range(len(text)):
            if text[i] in result:
                result[text[i]]+=1
            elif text[i] not in result:
                result[text[i]]=1
    #print(result)
    for key,value in result.items():
        print(key,value)
        
    txt.close()
    
    
    #print("Output: ",result)
#merged Error
histogram()
