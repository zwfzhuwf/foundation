#if语句
#5-1
foods=['meat','vegetables','rise']
for food in foods:
  if food=='meat':
    print('eat more vegetables')
  elif food=='vegetables':
    print('you can eat meat')
  else:
    print('ohhhhhhhh no')

#5-2

a='bab'
if a!='ccc':
    print('yes')
else:
    print('no')


b='ABc'
if b.lower()=='abc':
    print('yes')
else:
    print('no')


n1=23
n2=21
if n1 or n2>22:
    print('so old')
else:
    print('so young')

n1=23
n2=21
if n1 and n2>22:
    print('so old')
else:
    print('so young')


#5-3
'''you can choose one of (green),(yello) and (red)'''
colour='red'
if colour=='green':
    print('you get 5 scores!')
#5-4
elif colour=='yello':
    print('you get 10 scores!')
#5-5
elif colour=='red':
    print('you get 15 scores!')

#5-6
age=70
if age<2:
    print('婴儿')
elif 2<=age<4:
    print('幼儿')
elif 4<=age<13:
    print('儿童')
elif 13<=age<20:
    print('青少年')
elif 20<=age<65:
    print('成年人')
else:
    print('老年人')

#5-7
fruits=['苹果','香蕉','梨']
if '甘蔗' in fruits:
    print('you really like bananas')
else:
    print('you don\'t like bananas')


#5-8
yhs=['admin','bdmin','cdmin','ddmin','edmin']
for yh in yhs:
    if yh=='admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello Jaden, thank you for looking in again.')

yhs=['admin','bdmin','cdmin','ddmin','edmin']
for yh in yhs:
    if yh=='admin':
        print(f'Hello {yh}, would you like to see a status report?')
    elif yh=='bdmin':
        print(f'Hello {yh}, would you like to see a status report?')
    else:
        print('Hello Jaden, thank you for looking in again.')

#5-9  空列表检测
yhs=[]
if yhs:
  for yh in yhs:
    if yh=='admin':
      print('Hello admin, would you like to see a status report?')
    else:
      print('Hello Jaden, thank you for looking in again.')
else:
  print('We need to find some users!')

#5-10
current_users=['a1','b1','c1','d1','e1']
new_users=['a1','b1','f1','g1','h1']
for new in new_users:
    if new in current_users:
        print(f'{new}'.title(),' you should change a name.')
    else:
        print(f'{new}'.title(), 'you can use this name.')



current_users=['a1','B1','c1','d1','e1']
new_users=['A1','b1','c1','g1','h1']
current=[]
for user in current_users:
    current.append(user.upper())
for new in new_users:
    if new.upper() in current:
        print(f'{new}, you should change a name.')
    else:
        print(f'{new}, you can use this name.')

#5-11
number=[]
for num in range(1,10):
    number.append(num)
for numb in number:
    if numb==1:
        print('1st')
    elif numb==2:
        print('2nd')
    elif numb==3:
        print('3rd')
    else:
        print(f'{numb}th')


while True:
    if 1==1:
        print('asdas')
    if 2==2:
        print('asdasdasd')
