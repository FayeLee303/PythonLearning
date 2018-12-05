for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内使用break退出循环
    # else下方的代码就不会执行
    print("else")

students = [
    {
        "name":"xiao",
        "age":12
    },
    {
        "name":"sou",
        "age":21
    },
    {
        "name":"stt",
        "age":18
    }

]
for student_dict in students:
    if student_dict["age"] <=10:
        print(student_dict)
        break
else:
    print("没有年龄小于10的")