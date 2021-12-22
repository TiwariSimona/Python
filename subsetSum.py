def subsetSums(arr, l, r,sum=0):

          #print current subset
          if l>r:
                    print(sum, end=" ")
                    return

          #subset including arr[l]
          subsetSums(arr, l+1, r, sum+arr[l])

          #subset excluding arr[l]
          subsetSums(arr, l+1, r, sum)

#driver code
arr= [1,2]
n=len(arr)
subsetSums(arr, 0, n-1)
