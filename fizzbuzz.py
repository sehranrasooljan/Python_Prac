# Fizzbuzz challenge

#if num is divisble by 3 print 'fizz'
#if num is divisble by 5 print 'buzz'
#if num is divisble by 3 & 5 both print 'fizzbuzz'

for i in range (0,30):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3  == 0:
        print("Fizz")   
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
