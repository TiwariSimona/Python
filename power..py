def power(a,b):
          if b==0:
                    return 0
          elif b==1:
                    return a
          else:
                    return(a*power(a,b-1))

a=int ( input('Enter first number'))
b=int( input('Enter second number'))
print(power(a,b))
