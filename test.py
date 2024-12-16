'''a=open("python.txt","r")
a.seek(5)
print(a.readline(20))'''

'''b=open("auto.txt",'w')
b.write("heelo")
b.close()'''

#name="hello"
#rollno=input("enter your rollno")
#marks=78
#l=[name,rollno,marks]
#with open("binary.dat",'w') as c:
    #c.write(name)
    #print(c.read())
    #c.write(rollno)
    #c.write(marks)
'''import pickle
f1=open("demo5.dat","wb")
l=[1,2,3,4]
pickle.dump(l,f1)

f1.close()'''


import pickle
f1=open("demo5.dat","rb")
while True:
    try:
        row=pickle.load(f1)
        print(row)
    except:EOFError
    break
 
f1.close()

