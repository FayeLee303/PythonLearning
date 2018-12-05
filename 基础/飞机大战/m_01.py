import pygame
from m_sprite import GameSprite

# 初始化
pygame.init()

print("start")

# hero_rect = pygame.Rect(100,500,100,100)
# print("原点 %d %d"%(hero_rect.x,hero_rect.y))
# print("尺寸 %d %d"%(hero_rect.width,hero_rect.height))
# print("尺寸 %d %d"%hero_rect.size)

# 创建游戏的窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

# 绘制飞机
player_image = pygame.image.load("./images/me1.png")
screen.blit(player_image,(189,500))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义Rect记录飞机的初始位置
player_rect = pygame.Rect(150,300,102,126)

# 创建敌机的精灵
enemy_1 = GameSprite("./images/enemy1.png")
enemy_2 = GameSprite("./images/enemy1.png",2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy_1,enemy_2)

# 让游戏不会立刻退出
while True:

    # 设置帧率60
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        for event in event_list:
            # 点击关闭按钮退出
            if event.type == pygame.QUIT:
                print("游戏退出...")
                # quit卸载所有模块
                pygame.quit()
                # 直接退出程序
                exit()

    # 修改飞机的位置
    player_rect.y -= 5
    # 如果移出屏幕，则将英雄的顶部移动到屏幕的底部
    # if player_rect.y + player_rect.height <= 0:
    if player_rect.bottom <=0:
        player_rect.y = 700
    # 调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(player_image,player_rect)

    # 精灵组
    enemy_group.update()
    enemy_group.draw(screen)

    # 调用update方法更新显示
    pygame.display.update()


# # 退出
# pygame.quit()