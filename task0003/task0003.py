# python 3
import random
the_generator = [random.sample(range(1, 51), 1) for i in range(1000000)]
the_list = []
for i in the_generator:
    the_list.extend(i)
with open('./out.dat', 'w') as file_name:
    for i in range(1, 51):
        file_name.write((f'Number{i}, {the_list.count(i)}\n'))


# python 2
import random
the_generator = [random.sample(range(1, 51), 1) for i in range(1000000)]
the_list = []
for i in the_generator:
    the_list.extend(i)
with open('./out.dat', 'w') as file_name:
    for i in range(1, 51):
        file_name.write(('Number' + str(i) +',' + str(the_list.count(i)) + '\n'))