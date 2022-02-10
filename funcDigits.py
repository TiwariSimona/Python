# Write a function which two numbers and returns the number that has minimum one's digit.

def func(n1,n2):
  O1 = n1%10
  O2 = n2%10
  if (O1<O2):
    print('First Numbers\'s one\'s digit is small.')
  if (O2>O1):
    print ('Second Numbers\'s one\'s digit is small.')
  if ( O2 = O1):
    print('Both are equal')
func()

