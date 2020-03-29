# 1
names = ['John', 'William', 'Smith']
first, second, last = None, None, None
for name in range(len(names)):
    first = names[0]
    second = names[1]
    last = names[2]
len_names = len(first)+len(second)+len(last)
print(f'{first[0]}. {second[0]}. {last[0]}. {len_names}')


# 2
def sum_num(the_list, number):
  for num in the_list:
    if num > number:
      print(num)
  print(sum(the_list))
sum_num([8,2,5,3,1,9], 4)


# 3
def count_num(the_list, number):
  total = 0
  for num in the_list:
    if num > number: total+=1
  print(total)
count_num([7,1,9,5], 6)