"""

# 创建类
class Cat:
    def eat(self):
        # 类里的方法想要调用外部设置的参数，在创建对象的时候必须给这个参数赋值
        # 就是先赋值再调用这个函数
        print("%s eat"%self.name)

    def drink(self):
        print("drink")

# 创建对象
tom = Cat()
# 给对象增加独有的新属性，不需要在类里定义
# 在类的外部给对象增加属性，当调用时没有给属性赋值就会报错

tom.name = "tom"
tom.eat()
tom.drink()

# print(tom)
# addr = id(tom)
# print("%d"%addr)

jerry = Cat()
"""

"""
class Cat:
    def __init__(self,name):
        print("这是一个初始化方法")
        # 定义属性，并赋初始值
        # init里的属性，类里所有的方法都可以调用
        # self.name = ""
        # 通过形参传递
        self.name = name
    def __del__(self):
        # self.name = name
        print("销毁对象%s"% self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "sss"

tom = Cat("tom")
print(tom.name)
print(tom)
"""

"""
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我叫%s，体重是%.2f公斤"%(self.name,self.weight)
    def run(self):
        print("%s今天去跑步"%self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s今天吃东西"%self.name)
        self.weight += 1

ming = Person("小明",50)
ming.run()
ming.eat()
print(ming)

"""

"""
class Furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s]占地面积%.2f平方米"%(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        # 需要外部传递的参数
        self.house_type = house_type
        self.area = area

        # 初始化时不需要外部传递
        self.free_area = area
        self.furniture_list = []

    def __str__(self):
        return "户型：%s\n总面积：%.2f剩余面积：%.2f家具列表:%s"\
               %(self.house_type,self.area,
                 self.free_area,self.furniture_list)

    def addItem(self,item):
        print("添加家具：%s"%item)
        if self.free_area > item.area:
            self.furniture_list.append(item)
            self.free_area -= item.area
        else:
            print("空间不够")


bed = Furniture("席梦思",4)
wardrode = Furniture("衣柜",2)
table = Furniture("桌子",1.5)

my_home = House("两室一厅",70)
my_home.addItem(bed)
my_home.addItem(wardrode)
my_home.addItem(table)

print(my_home)
"""


class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print("[%s]发射子弹,剩余[%d]颗子弹"%(self.model,self.bullet_count))
        else:
            print("[%s]没有子弹了"%self.model)

    def __str__(self):
        return self.model


class Solider:
    def __init__(self,name):
        # 定义属性时没有初始值可以设置为None
        # None表示空对象，没有方法和属性，是一个特殊的常量
        self.name = name
        self.gun = None

    def fire(self):
        # 判断有没有抢
        # 喊口号
        # 给枪砖添子弹
        # 发射子弹
        if self.gun is None:
            print("[%s]还没有枪……" % self.name)
            return
        print("[%s]冲啊！" % self.name)
        if self.gun.bullet_count <= 0:
            print("[%s]装添子弹" % self.gun)
            self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("ak47")
ming = Solider("许三多")
ming.gun = ak47
fire = input("按下f键开火")
while True:
    if fire == "f":
        ming.fire()
    quit = input("按下q键退出")
    if quit == "q":
        break
