
#8-2
'''def favorite_book(book_name):
    print(book_name.title())    #函数定义
favorite_books=input('What\'s your favourite book?')
favorite_book(favorite_books)'''

#8-3
def make_shirt(size,word):
    print(f'you want to make a shirt with {size} and have {word} in it.')
make_shirt(123,'hhh')

#8-4
'''a=input('asd')
def make_shirt(size,word='I love python'):
    print(f'you want to make a shirt with {size} and have {word} in it.')
make_shirt('big')
make_shirt('middle')
make_shirt('small',a)

#8-6
ab=input()
ba=input()
def city_country(aa,bb):
    print("'",aa,',',bb,"'")
city_country(ab,ba)'''

#8-7
'''name=input('..')
music=input('...')
def make_album(names,mmu):
    musi={'name':names,'music':mmu}
    print(musi['name'],musi['music'])
make_album(name,music)'''


#8-8
'''def make_album(names,mmu):
    mus={'names':names,'music':mmu}
    return mus
nam=input('123')
musi=input('123543')
musics=make_album(nam,musi)
jiance=True
while jiance:
    nam = input('..')
    musi = input('...')
    if nam=='stop':
        jiance=False
    elif musi=='stop':
        jiance=False
    musics[nam]=musi
print(musics)'''

#8-9
message=['a','b','c','d','e']
def shou_message(a):
    for ab in a:
        print(ab)
shou_message(message)

#单*及双*号
def aaa(*a):
    print(a)
aaa(123,12344)  #元组
def bbb(**b):
    print(b)
bbb(acv=12)

#拆包
s='123'
def ooo(a,b,c):
    print(a)
    print(b)
    print(c)
ooo(*s)

l=[1,2,3]
def ooo(a,b,c):
    print(a)
    print(b)
    print(c)
ooo(*l)

t={'名':1,'b':2,'c':3}         #双星号键、位置参数、函数内部参数须一致
def ooo(名,b,c):
    print(名)
    print(b)
    print(c)
ooo(**t)

t={'a':1,'b':2,'c':3}
def ooo(a,b,c):
    print(a)
    print(b)
    print(c)
ooo(*t)


#8-10
message=['a','b','c','d','e']
send_message=[]
def change():
    print(message)
    while message:
        aba=message.pop()
        print(aba)
        send_message.append(aba)
    print(send_message)
    print(message)
change()

#8-12
'''def sand(biyao,*food):
    print('You want to use ',biyao,'、 ',food,'to make a sandwish.')
foo = input('嗨害嗨')
fo=[]
abc=True
while abc:
    foo = input('还有吗')
    if foo!='none':
        fo.append(foo)
    else:
        abc=False
sand('bread',fo)'''

#8-14
car=input('asdasd')
x=input('asda')
def cars(**car):
    print(car)
cars(car=x)


#模块

import 整除检测















