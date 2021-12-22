def harmonic(n):
          if(n==1):
                    return 1
          if(n!=1):
                    return(1/n + harmonic(n-1))

n=int(input("Enter n "))
print(harmonic(n))
