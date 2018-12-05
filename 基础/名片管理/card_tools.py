"""
给主程序提供执行方法和函数
"""

# 用列表储存所有名片字典
card_list = []


def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""

    print("-" * 50)
    # 提示用户输入信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")
    # 使用用户输入的信息建立一个名片字典
    card_dict = {
        "name":name_str,
        "phone":phone_str,
        "email":email_str
    }
    # 将该名片字典添加到名片列表里
    card_list.append(card_dict)
    # 提示用户添加成功
    print("新增 %s 的名片成功！" % name_str)
    print("-" * 50)


def show_all():
    """显示所有名片"""

    print("-" * 50)
    # 判断列表中是否有数据，如果什么都没有就不打印表头而是提醒用户
    if len(card_list) == 0:
        print("名片夹为空！请添加名片")
    else:
        # 打印表头
        for title in ["姓名","电话","邮箱"]:
            print(title,end="\t\t")
        print("")
        print("=" * 50)
        # 遍历名片列表依次输出
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s"%(card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["email"]))

    print("-" * 50)


def search_card():
    """搜索名片"""

    print("-" * 50)
    # 提示用户输入查找的姓名
    find_name = input("请输入查找的姓名：")
    # 遍历名片列表，根据姓名查询，并输出，如果没有则提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            # 打印表头
            for title in ["姓名", "电话", "邮箱"]:
                print(title, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s"%(card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["email"]))
            # TODO 针对找到的名片进行修改和删除
            deal_card(card_dict)
            break
    else:
        print("没有找到要查询的姓名！")
    print("-" * 50)


def deal_card(find_card):
    """处理名片"""
    action_str = input("请输入对名片的操作："
                       "1修改/2删除/0返回上一级")
    # 因为deal_card函数调用完之后跟着break,跳出search_card函数
    # 在main程序里往下走就是回到while循环
    # 有就是说，在这里无论输入什么键都会回到主界面，只是输入1，2之后有操作的时间，操作完还会回到主界面
    if action_str in ["0","1","2"]:

        if action_str == "1":
            # 修改
            # 思路1：一次只修改一项，直到0确认修改成功
            # update_card_1(find_card)
            # 思路2：按回车不修改当前项
            update_card_2(find_card)
        elif action_str == "2":
            # 删除
            card_list.remove(find_card)
            print("成功删除 %s" % find_card["name"])
        # elif action_str == "0":
        #     pass
    else:
        print("输入无效")


def update_card_1(find_card):
    """思路1：一次只修改一项，直到0确认修改成功"""
    while True:
        action_str_2 = input("请输入修改项："
                             "1姓名/2电话/3邮箱/0确认")
        if action_str_2 in ["0", "1", "2", "3"]:
            if action_str_2 == "1":
                find_card["name"] = input("输入修改的姓名：")
            elif action_str_2 == "2":
                find_card["phone"] = input("输入修改的电话：")
            elif action_str_2 == "3":
                find_card["email"] = input("输入修改的邮箱：")
            elif action_str_2 == "0":
                print("修改完成！")
                break


def update_card_2(find_card):
    """思路2：按下回车跳过当前项不修改"""
    find_card["name"] = input_card_info(find_card["name"],"输入修改的姓名：(回车不修改)")
    find_card["phone"] = input_card_info(find_card["phone"],"输入修改的电话：(回车不修改)")
    find_card["email"] = input_card_info(find_card["email"],"输入修改的邮箱：(回车不修改)")
    print("%s 的名片修改成功！" % find_card["name"])


def input_card_info(dict_value,tip_message):
    """

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入内容，则返回结果，如果用户没有输入内容，返回字典中原有的值
    """
    # 提示用户输入内容
    result_str = input(tip_message)
    # 如果用户输入内容，则返回结果
    if len(result_str) >0:
        return result_str
    else:
        # 如果用户没有输入内容，返回字典中原有的值
        return dict_value
