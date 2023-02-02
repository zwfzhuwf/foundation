
#整除检测
#7-3 bug修复版
def is_number(s):
    try:
        float(s)
        return  True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False
ab=True
ba=True
abc=int(ab)*int(ba)
while abc==1:
    print("结束程序运行请在任意行输入'stop'")
    bcs = input('这个程序可以检测是否可以被某数整除，下面请输入被除数:')
    cs = input('请输入除数:')
    a = is_number(bcs)
    b = is_number(cs)
    if bcs == 'stop':
        ab = False
    elif cs == 'stop':
        ba = False
    abc = int(ab) * int(ba)
    if abc==1:
        if a and b ==True:
            if int(cs) != 0:
                if int(bcs)%int(cs)==0:
                    print(bcs,'可以被',cs,'整除，结果为:',int(bcs)/int(cs),'\n    ')
                elif int(bcs)/int(cs)<1:
                    print(bcs, '无法被', cs, '整除。\n小数结果为:', int(bcs) / int(cs),'\n结果小于1，无余数结果')
                else:
                    print(bcs,'无法被',cs,'整除。\n小数结果为:',int(bcs)/int(cs),'\n余数结果为:',\
                          int(int(bcs)/int(cs)),'余',int(bcs)%int(cs),'\n    ')
            else:
                print('你干嘛，哎哟！\n   ')
        else:
            print('你小子行，我先报个错。\n   ')
    else:
        print('程序停止运行')
        break
