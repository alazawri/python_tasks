emails = ['a@a.com', 'b@b.com', 'c@c.com']
for i in range(1,4):
  (lambda email: ((exit(f'Hello {email}') if email in emails else print(f'Ran out of tries') if i == 3 else print(f'Wrong email'))))(input('Enter Your Email: ').lower())