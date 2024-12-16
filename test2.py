to read data from file
import pickle
with open("demo6.dat","rb") as f1:
    while True:
        try:
            row=pickle.load(f1)
            print(row)
        except:
            break


        
writing to file
import pickle
#f1=open("demo5.dat","ab")
with open("demo6.dat","ab") as f1:    
    pickle.dump(["name",12,89.56],f1)
    pickle.dump([1,2,3,4],f1)
        
    

 

