def sum_numbers(num):
    print(num)
    # 1先写出口
    if num == 1:
        return 1
    # 2数字累加，先假设递归可以完成
    # 假设temp = an到a2 的和
    # 只需要让temp + a1
    temp = sum_numbers(num-1)
    return num + temp

result = sum_numbers(5)
print(result)