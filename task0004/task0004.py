def program(l=[]):
  totle, average, new_list,msg = 0, 0, [], ''
  for i in l:
    if not str(i).isdigit():
      msg = print('There are a character in the list not a digit!')
      return msg
    else:
      new_list.append(i)
  totle = sum(new_list)
  average = round(sum(new_list) / len(new_list), 2)
  msg = print(f'The Total is {totle}, and the average is {average}')
  return msg


program([1,2,3])
program([1,2,'a'])