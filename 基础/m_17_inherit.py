class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# 继承
class Dog(Animal):
    def bark(self):
        print("叫")


# 继承传递
class XiangTianQuan(Dog):
    def fly(sel):
        print("飞")

    # 覆盖父类
    # def bark(self):
    #     print("汪汪叫")

    # 扩展父类
    def bark(self):
        # 子类的特有
        print("汪汪叫")
        # 调用父类里的方法
        super().bark()
        # Dog.bark()
        # 子类的特有
        print("&^%$#%*")


xtq = XiangTianQuan()
xtq.eat()
xtq.fly()
xtq.bark()

class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 =2

    def __test(self):
        print("私有方法%d %d" % (self.num1,self.__num2))

    def test(self):
        print("父类中的公有方法")
        print("访问父类的私有属性%d"%self.__num2)

class B(A):
    def demo(self):
    # 子类不能访问父类的私有属性和方法
    # 可以访问父类的公有属性和方法
        print("子类方法%d" % self.num1)
        self.test()

b = B()
print(b.num1)
b.demo()

# 多继承
class AA:
    def test(self):
        print("AA---test")

class BB:
    def test(self):
        print("BB---test")

class CC(AA,BB):
    pass

cc = CC()
cc.test()
# 确定CC类对象调用的顺序
print(CC.__mro__)
