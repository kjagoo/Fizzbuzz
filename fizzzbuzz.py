
def fizzBuzz(arg1):
  if (arg1%3==0) and (arg1%5==0):
    return 'FizzBuzz'
  elif (arg1%3==0) and (arg1%5!=0):
    return 'Fizz'
  elif (arg1%5==0) and (arg1%3!=0):
    return 'Buzz'
  else :
    return arg1
  
fizzBuzz(10)
