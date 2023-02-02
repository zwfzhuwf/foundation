#10-6,10-7
while True:
    n1 = input('输入一个数:')
    n2 = input('输入一个数:')
    if n1!='stop':
        if n2 != 'stop':
            try:
                jiegguo=int(n1)+int(n2)
            except ValueError:
                print('奶奶滴，和我玩阴滴是吧。')
                pass
            else:
                print(jiegguo)
        else:
            print('程序结束。')
            break
    else:
        print('程序结束。')
        break

#10-8
try:
    with open("E:\cat.txt",'r') as y:
        print(y.read())
    with open("E:\c.txt",'r') as t:
        print(t.read())
except FileNotFoundError:
    pass

#10-11
import json
def names():
    try:
        with open('name') as p:
            username=json.load(p)
    except FileNotFoundError:
        return None
    else:
        aba = input('Do you want change your favourite number?')
        if aba=='yes':
            return None
        else:
            return  username
def greet():
    user=names()
    if user:
        print(f'You like ',{user})
    else:
        num=input('What\'s your favourite number:')
        with open('name','w') as p:
            json.dump(num,p)
            print(f'Now we know your favourite number,it is ',{num})
greet()

#10-13
def ces():
    try:
        with open('usna') as i:
            us=json.load(i)
    except FileNotFoundError:
        return None
    else:
        print({us})
        mam=input('Is this your names?')
        if mam=='yes':
            return us
        else:
            return None
def gree():
    if ces():
        with open('usna') as i:
            us=json.load(i)
        print(f'welcome,',{us})
    else:
        na=input('What\'s your name?')
        with open('usna','w') as i:
            json.dump(na,i)
        print(f'welcome',{na})

gree()









































