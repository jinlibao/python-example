#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
请你综合四天所学知识，将下面的对话，用代码表现出来。

小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？
你：需要
小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询
你：2
小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币
小精灵：请问您需要兑换多少金加隆呢？
（你说了一个数字N）
小精灵：好的，我知道了，您需要兑换（你说的数字N）金加隆。
小精灵：那么，您需要付给我（你说的数字N*51.3）人民币。

注1：如果选择不需要帮助，小精灵会礼貌地说'好的，再见。'
注2: 如果选择帮助【1 存取款】，小精灵会推荐你去存取款窗口；如果选择帮助【3 咨询】，小精灵会推荐你去咨询窗口。
'''

print('Hello, welcome to Myhome, do you need any help?')
answer1 = input('Need or No need\n')

if answer1 == 'No need':
    print('Okay, goodbye!')
else:
    print('how can I help you?')
    answer2 = int(input('1 存取款；2 货币兑换；3 咨询\n'))
    if answer2 == 1:
        print('I recommend you to go conselling windows')
    elif answer2 == 2:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        moneychange = input('请问您需要兑换多少金加隆呢？\n')
        print(' Okay, I get it, you need to exchange for ' + moneychange + ' 金加隆。')
        moneychange1 = float(moneychange)
        print('那么，您需要付给我' + str(moneychange1 * 51.3) + '人民币。')
    else:
        print('You can go to 存取款窗口')
