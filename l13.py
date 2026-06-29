import numpy as p

dt = [('name', 'S15'),('class',int),('height',float)]
sd = [('James',5,48.5),('Nail',6,52.5),('Paul',5,42.1),('Pit',5,40.11)]
students = p.array(sd , dt )
print('original array:')
print(students)
print('sort by height')
print(p.sort(students, order='height'))