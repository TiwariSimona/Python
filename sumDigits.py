def sumDigits(n):
          if n==0:
                    return 0
          else:
                    return n%10 + sumDigits(n//10)


n= int(input("Enter number"))
print(' Sum of ', n , 'is' ,sumDigits(n))
