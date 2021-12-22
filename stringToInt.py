def str_to_int(str1,num):
          if len(str1)==1:
                    return int(str1) + (num*10)

          num= int(str1[0:1]) + (num*10)

          return str_to_int(str1[1:], num)

str1= input('Enter number')
num=0
print(str_to_int(str1,num))
