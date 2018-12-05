class Dog(object):
    # 静态方法，不访问类属性类方法，不访问实例属性实例方法
    @staticmethod
    def run():
        print("汪汪汪")

# 只能通过类名.调用静态方法
# 不能用对象调用静态方法
Dog.run()


class Game(object):
    # 游戏最高分
    top_score = 0
    # 静态方法显示游戏信息
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")
    # 类方法显示历史最高分
    @classmethod
    def show_top_socre(cls):
        print("游戏历史最高分%d" % cls.top_score)
    # 初始化
    def __init__(self,name):
        self.player_name = name
    # 开始游戏
    def start_game(self):
        print("%s开始游戏" % self.player_name)


game = Game("小明")
Game.show_help()
Game.show_top_socre()
game.start_game()

