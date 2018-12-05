# 1.定义一个变量记录QQ号码
qq_number = "12312323"
# 2.定义一个变量记录QQ密码
qq_password = "dfa23242"


"""
price = 8.5
weight = 3
money = price * weight
money = money - 5
print(money)
"""

"""
姓名：小明
年龄：15
性别：男
身高：1.75米
体重：55公斤
name = "小明"
age = 15
gender = True  # true是男生
statual = 1.75
weight = 55.0
"""

"""
print("输入姓名：")
name = input()
print("输入年龄：")
age = input()
print("是男孩吗？y/n")
temp = input()
if(temp == "y"):
    gender = "男孩"
else:gender = "女孩"
print(name+"是一个"+age+"岁的"+gender)
"""

"""
price_str = input("苹果的单价：")
weight_str = input("苹果的重量：")
print("苹果一共"+str(float(price_str)*float(weight_str))+"元")

price = float(input("苹果的单价："))
weight = float(input("苹果的重量："))
print("苹果一共"+str(price * weight)+"元")

number = 1234
print("QQ号是 %06d" % number)
"""

"""
# 变量的格式化输出
price = float(input("苹果的单价："))
weight = float(input("苹果的重量："))
# print("苹果一共 %s 元" % str(price * weight))
print("苹果单价 %.02f 元，买 %.02f 斤，一共 %.02f 元" %(price,weight,price*weight))

# 如果不加括号，就是字符串拼接100遍了
scale = 0.25
print("数据比利是 %.2f%%" % (scale*100))

"""


"""
参数传递
"""
def test(num):
    print("在函数内部%d对应的内存地址是%d"%(num,id(num)))
    result = "hello"
    print("函数要返回数据的内存地址是%d"%id(result))
    return result

a = 10
print("变量保存数据的内存地址是%d"%id(a))
# 调用test函数，本质上传递的是实际参数保存数据的引用（地址）
# 并不是传递的实际参数保存的数据
result_id = test(a)
print("%s的内存地址是%d"%(result_id,id(result_id)))

# 局部变量
def demo1():
    num = 1
    print("输出局部变量：%d"%num)
# print(num)

# 全局变量
num = 1
def demo2():
    print("输出全局变量：%d"%num)

# 无法在函数内部修改全局变量的值
def demo3():
    # 这里不能通过赋值语句修改全局变量num的值
    # 而是在函数内部重新定义了一个叫num的变量
    num = 2
    print("在函数内部不能直接修改全局变量：%d"%num)

# 使用global关键字修改全局变量
def demo4():
    global num
    num = 2
    print("在函数内部使用global修改全局变量：%d"%num)

demo1()
demo2()
demo3()
demo4()