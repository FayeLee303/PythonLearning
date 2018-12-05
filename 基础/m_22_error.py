try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
    result = 8/num
    print(result)
# except ZeroDivisionError:
#     # 出现错误的处理代码
#     print("除数不能为0")
except ValueError:
    print("请输入正确的整数")
except Exception as e:
    print("未知错误 %s" % e)
else:
    print("没有异常才会执行的代码")
finally:
    print("无论有没有异常都会执行的代码")


# 异常的传递
def demo1():
    return int(input("请输入一个整数："))

def demo2():
    return demo1()

# 在主程序中进行异常捕获
try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")

# 主动抛出异常
def input_password():
    password = str(input("请输入八位密码："))
    if len(password) >= 8:
        return password
    # 密码长度小于8主动抛出异常
    # 创建异常对象，可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 抛出异常
    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)
