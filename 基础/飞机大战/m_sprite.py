import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新帧率常量
FRAME_PER_SEC = 60

# 继承pygame的Sprite类
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


# 实现游戏背景的滚动
class BackGround(GameSprite):
    def __init__(self,is_alt = False):
        # 调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是，需要指定初始位置
        if is_alt:
            # 指定第二张图放在屏幕上方
            self.rect.y = -self.rect.height


    def update(self):
        # 调用父类的方法实现垂直移动
        super().update()
        # 判断图像是否移出屏幕
        # 如果移出屏幕，就将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height