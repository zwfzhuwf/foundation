class aihei:
    def __init__(self,n1,n2,n3):
        self.name=n1
        self.asd=n2
        self.zzz=n3
laoba=aihei('aaa','niganma','bbb')
print(laoba.name,laoba.asd,laoba.zzz)

#9-1
class restaurant1:
    def __init__(self,restaurant1_name,cuisine1_type):
        self.resrestaurant1_name=restaurant1_name
        self.cuisine1_type=cuisine1_type
    def describe_restauran(self):
        print(f'餐厅名:',{self.resrestaurant1_name})
        print(f'菜系:',{self.cuisine1_type})
    def open_restaurant(self):
        print('餐厅开始营业')
abc=restaurant1('laba','xx')
print(abc.resrestaurant1_name)
print(abc.cuisine1_type)
abc.describe_restauran()
abc.open_restaurant()

#9-2
class restaurant2:
    def __init__(self,retaurant2_name,cuisine2_type):
        self.restaurant2_name=retaurant2_name
        self.cuisine2_type=cuisine2_type
    def describe2_restauran(self):
        print(f'餐厅名:',{self.restaurant2_name})
        print(f'菜系:',{self.cuisine2_type})
    def open_restaurant2(selfs):
        print('餐厅今日不营业')
abc2=restaurant2('nianma','xiachi')
abc2.describe2_restauran()
abc.open_restaurant()
abc2.open_restaurant2()

#9-4
class restaurant1:
    def __init__(self,restaurant1_name,cuisine1_type):
        self.resrestaurant1_name=restaurant1_name
        self.cuisine1_type=cuisine1_type
        self.number=0
    def describe_restauran(self):
        print(f'餐厅名:',{self.resrestaurant1_name})
        print(f'菜系:',{self.cuisine1_type})
    def open_restaurant(self):
        print('餐厅开始营业')
    def set_number(self,number):
        self.number=number
    def increment_number(self,increment):
        self.number+=increment
abc=restaurant1('laba','xx')
abc.describe_restauran()
abc.open_restaurant()
abc.set_number(123)
abc.increment_number(456)
print(abc.number)

#9-5
class user:
    def __init__(self,names,age):
        self.names=names
        self.age=age
        self.login_attempts=0
    def increment_attempts(self,increment):
        self.login_attempts+=increment
    def reset_attempts(self):
        self.login_attempts=0
users=user('zwf','20')
print(users.names,users.age)
ssss=input('enter')
sss=True
while sss:
    if ssss=='no':
        print(users.login_attempts)
        users.reset_attempts()
        sss=False
    else:
        users.increment_attempts(1)
        ssss = input('enter')
print(users.login_attempts)

#9-6
class restaurant1:
    def __init__(self,restaurant1_name,cuisine1_type):
        self.resrestaurant1_name=restaurant1_name
        self.cuisine1_type=cuisine1_type
    def describe_restauran(self):
        print(f'餐厅名:',{self.resrestaurant1_name})
        print(f'菜系:',{self.cuisine1_type})
    def open_restaurant(self):
        print('餐厅开始营业')
class icecream(restaurant1):
    def __init__(self,restaurant1_name,flavors):
        super().__init__(restaurant1_name,'甜品')
        self.flavors=flavors
    def show_flavors(self):
        print(self.flavors)
ice=icecream('aaaaaa',['b','c','d','e'])
ice.describe_restauran()
ice.show_flavors()

#9-7
class user:
    def __init__(self,names,age):
        self.names=names
        self.age=age
class admin(user):
    def __init__(self,names,age):
        super().__init__(names,age)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for priv in self.privileges:
            print(priv)
Admin=admin('zwf','20')
Admin.show_privileges()

#9-9
class car:
    def __init__(self,lic=270):
        self.licheng=lic
    def lichengs(self):
        if int(Bettery.rongliang)==100:
            Car.licheng=360
class battery:
    def __init__(self,rongl):
        self.rongliang=rongl
    def change(self):
        if int(Bettery.rongliang)<=100:
            Bettery.rongliang=100
aass=input('...')
Bettery=battery(aass)
Car=car()
Bettery.change()
Car.lichengs()
print(f'升级后里程为:',{Car.licheng})
print(f'电池容量为:',{Bettery.rongliang})

