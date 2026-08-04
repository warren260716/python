animal = ['dog','cat','monkey','fox','tiger']
print('*'*40)
print(f'原始串列：{animal}')
print('*'*40)
data = sorted(animal, reverse = False)
print(f'排序後的animal：{animal}')
# print(f'animal = {animal}') # animal=['dog','cat','monkey','fox','tiger']
print(f'data = {data}') # data = ['cat','dog','fox','monkey','tiger']
print('*'*40)