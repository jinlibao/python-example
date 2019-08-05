#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
