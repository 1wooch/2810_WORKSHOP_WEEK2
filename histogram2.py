from os import O_SEQUENTIAL
import sys
import math

input=sys.stdin.readlines()
#print(input) #['TEST 3\n', 'THIS 2\n', 'IS 2\n', 'A 2\n', 'TO 1\n', 'THAT 1\n']
#print(type(input)) #list

#print(input[0]) #TEST 3
#print(type(input[0]))#str


#print(input[0].split()) #['TEST', '3']
#print(type(input[0].split())) #list
count=0

for i in range( len(input)):
    value=input[i].split()
    count+=int(value[1])

#print(count) #11

for i in range( len(input)):
    value2=input[i].split()
    print(value2[0]," ",str(math.trunc(int(value2[1])/count*100))+'%')#," ",value2[1]/count)
    #print(int(value2[1])/count)

#alignment python
