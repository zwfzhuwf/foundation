#9-14(不计顺序)
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
    if set(caip)!=set(caipiao):
        caip.clear()
        times=times+1
        Piao.chou()
        print(f'抽取到:',caip)
    else:
        que=False
        print(f'累计抽取:',{times})
        print(f'中奖号码:',caipiao)