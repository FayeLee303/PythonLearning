def print_info(name,title = "      ",gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s:%s是%s"%(title,name,gender_text))

print_info("小明",gender=True)

def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

demo(1,2,3,a=1,b=2)

# 计算任意多个数字的和
def sum_numbers(*args):
    num = 0
    for n in args:
        num += n
    return  num
print(sum_numbers(9,32,2,1,2,9))

# 拆包
def demo2(*args,**kwargs):
    print(args)
    print(kwargs)

# 元祖变量和字典变量
gl_nums = (1,2,3)
gl_dict = {"a":1,"b":2}
# 这样两个变量都被传给args了
# ((1, 2, 3), {'a': 1, 'b': 2})
# {}
# demo2(gl_nums,gl_dict)
demo2(*gl_nums,**gl_dict)
# 相当于
demo2(1,2,3,a=1,b=2)
