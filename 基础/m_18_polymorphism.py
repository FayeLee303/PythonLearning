class Dog(object):
    def __init__(self,name):
        self.name = name

    def play(self):
        print("%s普通玩耍" % self.name)


class XiaoTianQuan(Dog):
    def __init__(self,name):
        self.name = name

    def play(self):
        print("%s飞上天玩耍" % self.name)


class Person(object):
    def __init__(self,name):
        self.name = name

    def play_with_dog(self,dog):
        print("%s和%s一起玩耍"%(self.name,dog.name))
        dog.play()


xtt = Dog("旺财")
#xtt = XiaoTianQuan("啸天犬")
ren = Person("小明")
ren.play_with_dog(xtt)
