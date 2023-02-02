#10-1
with open("E:\zzzzaaa.txt",'r',encoding='utf-8') as f:
    aaa=f.read()
print(aaa)
with open("E:\zzzzaaa.txt",'r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
with open("E:\zzzzaaa.txt",'r',encoding='utf-8') as f:
    bbb=f.readlines()
print(bbb)

#10-2
with open("E:\zzzzaaa.txt",'r',encoding='utf-8') as f:
    wen=f.read().replace('python','c')
with open("E:\zzzzaaa.txt",'w',encoding='utf-8') as f:
    f.write(wen)

#10-3
'''with open('E:\guest.txt','r+') as e:
    name=input('输入用户名:')
    names=e.write(name)'''

#10-4
with open("E:\guest_book.txt",'a') as m:
    abb=True
    while abb:
        nam=input('输入用户名:')
        if nam!='stop':
            m.write(nam+'\n')
            print(f'欢迎',{nam})
        else:
            abb=False
with open("E:\guest_book.txt", 'r') as m:
    print(m.read())

#10-5
with open("E:\causes.txt",'a') as n:
    cuses = input('Why you like python?')
    n.write(cuses + '\n')
    while cuses!='q':
        cuses = input('Why you like python?')
        if cuses=='q':
            break
        n.write(cuses+'\n')








