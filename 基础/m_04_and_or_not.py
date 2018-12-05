age = int(input("输入年龄："))
if age>=0 and age <=100:
    print("正确")
else:
    print("错误")

python_score = 80
c_score = 40
if python_score >=60 or c_score>=60:
    print("通过")
else:
    print("失败")

is_girl = True
"""
if is_girl:
    print("通过")
else:
    print("失败")
"""
if not is_girl:
    print("失败")
else:
    print("通过")
