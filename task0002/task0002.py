# 1
travel_plans = open('./travel_plans.txt')
num_words = len(travel_plans.read().split())
print(num_words)


# 2
school_prompt = open('./school_prompt.txt')
count = 0
for line in school_prompt:
  count += 1
print('Line Count:', count)


# 3
school_prompt = open('./school_prompt.txt')
for line in school_prompt:
  print(line.upper().replace('\n', ''))