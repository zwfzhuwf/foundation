#7-1
'''car=input('What car you want?')
print('let me see if I can find you a ',car,'.')'''

#7-2
'''peop=input('Hou many people?')
if int(peop)>8:
    print('We have no table.')
else:
    print('We have enough tables.')'''

#7-3进阶版
'''bcs=input('这个程序可以检测是否可以被某数整除，下面请输入除数')
cs=input('请输入被除数')
if int(bcs)%int(cs)==0:
    print(bcs,'可以被',cs,'整除')
else:
    print(bcs,'无法被',cs,'整除。\n小数结果为:',int(bcs)/int(cs),'\n余数结果为:',\
              int(int(bcs)/int(cs)),'余',int(bcs)%int(cs))'''


#7-4
'''pl=input('输入你想要的配料:')
while pl != 'quit':
    print('为你添加了配料:',pl)
    pl = input('输入你想要的配料:')'''


#7-5
'''nl=input('请输入你的年龄:')
ac=True
while ac:
    if int(nl)<3:
        print('free')
        nl = input('请输入你的年龄:')
    elif 3<=int(nl)<=12:
        print('10 dollers')
        nl = input('请输入你的年龄:')
    elif 100>=int(nl)>12:
        print('15 dollers')
        nl = input('请输入你的年龄:')
    elif int(nl)>100:
        print('下播!')
        ac=False'''

#7-7
'''while True:
    print('456')'''

#7-8
sandwich=['a','b','c']
finish=[]
while sandwich:
    zj=sandwich.pop()
    print(f'I made {zj[0]}')
    finish.append(zj)
print(finish)
print('just these:')
for fin in finish:
    print(fin)

#7-9
foods=['d','e','f','f','f']
while 'f' in foods:
    foods.remove('f')
print(foods)
if 'f' in foods:
    print('没删干净')

#7-10
places=input('If you ...,where would you go?(If have no place please say:no places)')
place=[]
atta=True
while atta:
    place.append(places)
    places=input('Do you have other places?')
    if places=='no places':
        atta=False
pl=list(set(place))
print('so you like:')
for pla in pl:
    print(pla)









