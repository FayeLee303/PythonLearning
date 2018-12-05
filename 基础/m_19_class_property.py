class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    # 类方法
    @classmethod
    def show_tool_count(cls):
        # 类似于self
        print("使用类方法访问类属性count%s" % cls.count)

    def __init__(self,name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1

tool1 = Tool("aa")
tool2 = Tool("bb")
print(Tool.count)
# 实例可以调用类方法和类属性
print(tool1.count)
# 如果使用对象.类属性 = 值赋值语句，只会给这个对象增加一个属性，不会影响到类属性
tool1.count = 100
# 调用类方法
Tool.show_tool_count()
tool1.show_tool_count()