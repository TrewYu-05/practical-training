import random
# 添加金额
money = 2000
# 不确定玩多少次（没有钱了，就结束点），使用while循环
while money > 0:
    print(f'玩家的资产是：{money}')
    # 要排除所有的其他因素，后续代码才能执行
    while True:
        # 下注操作
        debt_str = input('请下注:')
        if not debt_str.isdigit():
            print('请输入有效数字')
            continue
        debt = int(debt_str)
        if debt <= 0:
            print('下注必须大于0')
        elif debt > money:
            print(f'下注金额不能超过当前的资产: {money}')
        else:
            break

    first_point = random.randint(1, 6) + random.randint(1, 6)
    print(f'玩家第一次摇出了 {first_point}点.')

    if first_point in (7, 11):
        print('玩家胜')
        money += debt
    elif first_point in (2, 3, 12):
        print('庄家胜')
        money -= debt
    else:
        while True:
            current_point = random.randint(1, 6) + random.randint(1, 6)
            print(f'玩家摇出了 {current_point}点.')
            if current_point == 7:
                print('庄家胜')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜')
                money += debt
                break

    if money <= 0:
        print('你破产了，游戏结束。')
        break

    play_again = input('是否继续玩？(y/n):')
    if play_again.lower() != 'y':
        break
