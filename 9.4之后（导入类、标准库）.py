#9-13
'''from random import randint
tiao=input("是否需要输入骰子面数，是输入'yes':")
zheng=6
if tiao=='yes':
    zheng=input('输入想要的骰子数:')
class Die:
    def __init__(self,side):
        self.sides=side
    def roll_die(self):
        print(randint(1,int(self.sides)))
dies=Die(zheng)
dies.roll_die()'''

#9-14（计入顺序）
from random import choice
cai=['0','1','2','3','4','5','6','7','8','9','a','b','c','d']
caip=[]
caipiao=[]
num=int(input('想要抽取几个字符？(<=14)'))
class piao:
    def __init__(self):
        self.piao='彩票抽取'
    def chou(self):
        jishu=0
        while jishu<num:
            jishu=jishu+1
            caip.append(choice(cai))
    def huoqu(self):
        jish=0
        while jish<num:
            jish=jish+1
            caipiao.append(choice(cai))
Piao=piao()
Piao.huoqu()
Piao.chou()
times=0
que=True
while que:
    if caip!=caipiao:
        caip.clear()
        times=times+1
        Piao.chou()
        print(f'抽取到:',caip)
        print(times)
        if times>=10000000:
            print('循环次数超过10亿次，强制停止')
            break
    else:
        que=False
        print(f'累计抽取:',{times})
        print(f'中奖号码:',caipiao)

























