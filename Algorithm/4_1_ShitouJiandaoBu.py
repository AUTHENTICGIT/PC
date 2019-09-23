import random

gesture = {0:'剪刀',1:'石头',2:'布'}

wintimes = 0

for i in range(5):
    user = int(input('''石头剪刀布 Ver1.00 By A.U.
输入玩家手势：
0: 剪刀、1: 石头、2: 布
'''))
    computer = random.randint(0,2)

    text = '玩家：' + gesture[user] + '、计算机：' + gesture[computer]

    if user == computer:
        print(text + '...平局！\n')
    elif (user - computer) == -1 or 2:
    # elif computer == (user + 1) // 3:
        print(text + '...玩家获胜！\n')
        wintimes = wintimes + 1
    else:
        print(text + '...计算机获胜！\n')

print('玩家获胜次数：{}次\n'.format(wintimes))