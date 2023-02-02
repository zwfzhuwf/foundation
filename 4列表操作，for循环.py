#for循环
temp=['16','19','21']
for tem in temp:
    print(tem)
    print('温度'+tem)
for tem in temp:
    print('温度'+tem)
print('真不错！')


#for与range
aa=0
for nu in range(1,2):
    aa=aa+nu
    print(aa)

#4-3
x=0
for x in range(1,21):
    print(x)

#4-4
"""xx=[]
for xxx in range(1,1000001):
    xx.append(xxx)
for xxx in xx:
    print(xxx)

#4-5
print(min(xx))
print(max(xx))

print(sum(xx))"""

#4-6
abc=[]
for abcd in range(1,21,2):
    abc.append(abcd)
for cba in abc:
    print(cba)

#4-7
abce=[]
for abcde in range(3,31,3):
    abce.append(abcde)
for cbaa in abce:
    print(cbaa)

#4-8
lf=[]
for lfs in range(1,11):
    lf.append(lfs)
for blf in lf:
    print(blf**3)

#4-9：列表解析
squire=[sss**3 for sss in range(1,11)]
print(squire)


#4-10
mene=['The','first','three','itens','in','the','line','are',':']
print(mene[0:3])
print(mene[3:6])
print(mene[-3:])

#4-11
pizzas=['aaa']
pizzas.append('bbb')
set(pizzas)
print(pizzas)


