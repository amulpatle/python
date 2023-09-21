import pickle

l = [10,20,30,44,2,67,1,98]

file = open("sample.txt","wb")

pickle.dump(l,file)
file.close()