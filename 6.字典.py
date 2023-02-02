alien={'a':'b','c':3,('e','f'):123}
alien['a']='d'
print(alien['a'])
print(alien[('e','f')])
err=alien.get('g','no point')
print(err)

#6-1
person={'fn':'wenfei','ln':'zhu','age':20,'city':'wuxi'}
print(person['fn'])
print(person['ln'])
print(person['age'])
print(person['city'])

#6-3
py_sy={'#':'注释','for':'循环','upper':'大写','if':'条件'}
py_sy['lower']='小写'
#6-4
for k,n in py_sy.items():
    print(k,n)

#6-5
rivers={'qwe':'rty','asd':'fgh','zxc':'vbn'}
for country,river in rivers.items():
    print('The '+river.title()+' runs through '+country.title())
for country,river in rivers.items():
    print("river's name:"+river.title())
for country, river in rivers.items():
    print("country's name:"+country.title())

#书   6.4嵌套
waixings=[]
waixing_1={'colour':'green','points':5}
waixing_2={'colour':'yellow','points':10}
waixing_3={'colour':'red','points':15}
for waixings_number in range(3):
    waixings.append(waixing_1)
for waixings_number in range(3):
    waixings.append(waixing_2)
for waixings_number in range(3):
    waixings.append(waixing_3)
for waixing in waixings:
    print(waixing)
print(f'Total number of waixings:{len(waixings)}')




#6-7
person_1={'fn':'wenfei','ln':'zhu','age':20,'city':'wuxi'}
person_2={'fn':'laoba','ln':'cai','age':22,'city':'heilongjiang'}
person_3={'fn':'naidi','ln':'nai','age':24,'city':'suzhou'}
people=[person_1,person_2,person_3]
for pe in people:
    print(pe)

#6-8
pets={'dubing':person_1,'heibei':person_2,'demu':person_3}
for k_p,v_p in pets.items():
    print(k_p+'\'s zhuren is',v_p)

#6-11
citys={'wuxi':{'c':'ab','p':'ac','f':'ad'},'xini':{'c':'bb','p':'bc','f':'bd'}\
    ,'huashemdun':{'c':'cb','p':'cc','f':'cd'}}
for k_c,v_c in citys.items():
    print(k_c,'is in ',v_c['c'],' have ',v_c['p'],' population and ',v_c['f'],' facts.' )


#6-12
citys={'wuxi':{'c':'ab','p':'ac','f':'ad'},'xini':{'c':'bb','p':'bc','f':'bd'}\
    ,'huashemdun':{'c':'cb','p':'cc','f':'cd'}}
for k_c,v_c in citys.items():
    for kkc,vvc in v_c.items():
        print(k_c,':(',kkc,':',vvc,')')
