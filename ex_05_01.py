# Write a program which repeatedly reads numbers until the user enters 'done'. Once 'done' is entered, print out of the total, count and average of the numbers. If the user enters anythings other than a number, detect their mistake using `try` and `except` and print an error message and skip to the next number.

num = 0
tot = 0.0
while True:
  sval = input('Enter a number: ') # string value
  if sval == 'done':
    break
  try:
    fval = float(sval)
  except:
    print('Invalid input')
    continue

  


  #print(fval)
  num = num + 1
  tot = tot + fval

#print('ALL DONE')
print(tot,num, tot/num)

