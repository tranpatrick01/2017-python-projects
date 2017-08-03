import random
start = input('Do you want to roll?')
start = start.upper()
a = (random.randint(1,6))
if start != 'YES' and start != 'NO':
  print('Please answer yes or no.')
if start == 'YES':
    print(a)
while True:
  playagain=input('Do you want to play again?')
  playagain = playagain.upper()
  if playagain == 'YES' :
    print(a)
  else: 
    break