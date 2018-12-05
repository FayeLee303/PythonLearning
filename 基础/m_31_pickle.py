import pickle

dict = ["a",111,2,[23,4,5],"23",{1:2,"d":"er"}]
file = open("pickle_example.pickle","wb")
# 压缩并保存数据
pickle.dump(dict,file)
file.close()

with open("pickle_example.pickle","rb") as file:
# file = open("pickle_example.pickle","rb")
    # 读取数据并保存在变量里
    dict_1 = pickle.load(file)
# file.close()
