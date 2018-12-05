"""
程序执行入口
"""
#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# 导入工具模块
import card_tools

# 无限循环，由用户决定什么时候退出
while True:
    # 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    # 1,2,3是正确操作，0退出，其他输入提示输入错误
    # in表示在容器里！这里相当于if action_str ==1 or ==2 or ==3
    if action_str in ["1","2","3"]:
        # 暂时跳过，pass占位符不会执行任何操作
        # pass
        # 新增名片
        if action_str == "1":
            card_tools.new_card()
        # 显示全部
        elif action_str == "2":
            card_t  ools.show_all()
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()
    elif action_str == "0":
        # 跳出循环
        print("欢迎再次使用名片系统，再见！")
        break
    # 其他提示输入错误
    else:
        print("输入无效")