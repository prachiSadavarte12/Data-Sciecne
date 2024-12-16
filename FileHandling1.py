import pickle
#f1=open("demo5.dat","ab")
with open("demo6.dat","ab") as f1:    
    pickle.dump(["name",12,89.56],f1)
    pickle.dump([1,2,3,4],f1)

