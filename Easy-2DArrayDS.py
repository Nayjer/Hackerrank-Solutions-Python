def hourglassSum(arr):
   first_line = max([arr[0+k][0+i]+arr[0+k][1+i]+arr[0+k][2+i]+arr[1+k][1+i]+arr[2+k][0+i]+arr[2+k][1+i]+arr[2+k][2+i] for i in range(4) for k in range(4)])
   return first_line
