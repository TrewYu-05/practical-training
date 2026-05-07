import random

first_point = random.randint(1, 6) + random.randint(1, 6)
print(f'玩家第一次摇出了 {first_point}点.')
if first_point in (7, 11):
    print('玩家胜')
elif first_point in (2, 3, 12):
    print('庄家胜')
else:
    # 其他情况游戏继续
    while True:
        current_point = random.randint(1, 6) + random.randint(1, 6)
        print(f'玩家重新摇出了 {current_point}点.')
        if current_point == 7:
            print('庄家胜')
            break
        elif current_point == first_point:
            print('玩家胜')
            break
