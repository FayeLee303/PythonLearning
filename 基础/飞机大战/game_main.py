import pygame
from m_sprite import *

# 主程序
class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self._creat_sprites()

    def _creat_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 1设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2捕获事件
            self._event_handler()
            # 3碰撞检测
            self._check_collider()
            # 4更新/绘制精灵粗
            self._update_sprites()
            # 5更新显示
            pygame.display.update()

    def _event_handler(self):
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 点击关闭按钮退出
                if event.type == pygame.QUIT:
                    PlaneGame._game_over()

    def _check_collider(self):
        pass

    def _update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    # 游戏结束设为静态方法
    @staticmethod
    def _game_over():
        print("游戏退出...")
        # quit卸载所有模块
        pygame.quit()
        # 直接退出程序
        exit()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()