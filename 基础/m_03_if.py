"""
age = float(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了")
else:
    print("滚回家去")

holiday_name = input("请输入节日")
if holiday_name == "情人节":
    print("啪啪啪")
elif holiday_name == "平安夜":
    print("吃苹果")
elif holiday_name == "生日":
    print("买礼物")
else:
    print("每天都是节日")


has_ticket = True
knife_length = 10
if not has_ticket:
    print("不允许上车")
else:
    if knife_length>=10:
        print("不允许上车")
    else:
        print("允许上车")
"""

# 导入随机工具包
# 应该放在最前面
import random

"""
输入数字，得到出拳结果
"""
def chuquan(input):
    if input == 1:
        output = "石头"
    elif input == 2:
        output = "剪刀"
    elif input == 3:
        output = "布"
    return output

"""
比较出拳胜负，如果相等返回0，如果前者赢返回1，如果后者赢返回2
思路1：就是不是布进行讨论，按123大小比较
思路2：分析玩家胜利的三种情况
"""
def vs(a,b):
    """
    思路1
     # 相等返回0
    if a==b:
        return 0
    else:
        # 都不是布
        if a<3 and b<3:
            if b>a:
                return 2
            elif a>b:
                return 1
        # a是布
        elif a==3 and b<a:
            if b==1:
                return 2
            else:
                return 1
        #b是布
        elif b==3 and a<b:
            if a==1:
                return 1
            else:
                return 2
    """
    """
    思路2
    """
    # 平局
    if a == b:
        return 0
    # 前者胜利的三种情况
    # 注意书写格式
    elif((a == 1 and b == 2)
         or(a == 2 and b == 3)
         or(a == 3 and b == 1)):
        return 1
    # 剩下的就是后者胜利
    else:
        return 2

# 控制台输入出拳，石头1，剪刀2，布3
player_input = int(input("请输入要出的拳：石头1，剪刀2，布3"))
# 电脑随机出拳
ai_input = random.randint(1,3)
# ai_input = int(input("请输入要出的拳：石头1，剪刀2，布3"))
print("玩家出：%s,电脑出：%s" % (chuquan(player_input),chuquan(ai_input)))
# 比较胜负
result = vs(player_input,ai_input)
if result == 0:
    print("双方平局")
elif result == 1:
    print("玩家赢")
elif result == 2:
    print("电脑赢")
