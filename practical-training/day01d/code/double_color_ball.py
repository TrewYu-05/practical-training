import random

n = int(input('请输入要打印的注数:'))
# 定义函数来做这个事情，因为函数可以传递参数，也可以进行代码复用
# n 表示的是打印几注
def create_balls(n):
    for _ in range(n):
        # 红色球
        red_balls = [x for x in range(1, 34)]
        # random.sample(red_balls, 6) 可以从列表中选出指定数量的元素
        select_balls = random.sample(red_balls, 6)
        # 进行排序操作
        # reverse=False 表示升序（不写是一样的效果）
        # reverse=True 表示降序
        select_balls.sort()
        # 蓝色球
        blue_balls = random.randint(1, 16)
        # ', '.join()
        # 表示格式化红色球
        fm_red = ', '.join([f'{val:02d}' for val in select_balls])
        # 表示格式化蓝色球
        fm_blue = f'{blue_balls:02d}'
        # 输出最终结果
        print(f'{fm_red} | {fm_blue}')

create_balls(n)
