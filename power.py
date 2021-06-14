#Write a program to calculate a^b using recursion.

p=3
q=5
def power(a,b):
  if (b==0):
    return 1
  else:
    return a * power(a, b-1)
  
