class Women:
    def __init__(self,name):
        self.name = name
        # 私有属性
        self.__age = 18

    def secret(self):
        print("%s的年龄是%d"%(self.name,self.__age))

xiaofang = Women("小芳")

# print(xiaofang.__age)
# 访问私有方法
print(xiaofang._Women__age)
xiaofang.secret()