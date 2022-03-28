from random import *

set_W = ['Ірина', 'Анна', 'Зоя', 'Олена', 'Марія', 'Юлія', 'Дарина', 'Інна', 'Катерина',]
set_M = ['Богдан', 'Ілля', 'Данило', 'Даніїл', 'Олександр', 'Віталій', 'Андрій', 'Артем', 'Владислав']

female = {'Ірина', 'Анна', 'Зоя', 'Олена'}
male = {'Ілля', 'Данило', 'Даніїл', 'Віталій', 'Андрій'}

#if set_M != set() and set_W != set():
#    relationS = set()
#    chrescheniy_father = set_M
#    chrescheniy_fathers_child = set_W
#    while chrescheniy_father != list():
#        father = choice(chrescheniy_father)
#        chrescheniy_father.remove(father)
#        if father in male:
#            chance = 90
#            if father in chrescheniy_fathers_child:
#                chrescheniy_fathers_child.remove(father)
#            local_child = list(chrescheniy_fathers_child)
#            while randrange(0, 101) in range(chance + 1) and local_child != list():
#                child = choice(local_child)
#                if child != father and (child, father) not in relationS:
#                    relationS.add((father, child))
#                    chrescheniy_fathers_child.remove(child)
#                    local_child.remove(child)
#                    chance -= 30
#                    if child in chrescheniy_father:
#                        chrescheniy_father.remove(child)
#                else:
#                    local_child.remove(child)


relations = set()
print(len(relations))