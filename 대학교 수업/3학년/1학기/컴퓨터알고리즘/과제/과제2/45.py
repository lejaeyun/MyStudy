#45
import sys
#Subarray의 합을 구함
def sum_subarray(arr, start_index, end_index) :
  func_type = 1
  if start_index > end_index : # for의 type을 구한다.(왼쪽이냐 오른쪽이냐)
    func_type = -1
    
  result = -sys.maxsize
  s = 0
  for i in range(start_index, end_index,func_type):
    s = s+arr[i]
    if (s>result):
      result = s
  return result

#중간에서 왼쪽 오른쪽의 Subarray의 최대 합을 구하고 더해서 return
def max_mid_subarray(arr, low, high):
  mid = (high+low)//2
  
  left_sum = sum_subarray(arr, mid, low-1)
  right_sum = sum_subarray(arr, mid+1, high+1)
  
  return left_sum+right_sum

#중간을 기준으로 왼쪽 절반, 오른쪽 절반을 재귀 호출, 중간의 최대값을 구함
#이 셋의 max값을 return
def max_subarray(arr, low, high):
  if (high == low): 
    return arr[high]

  mid = (high+low)//2

  max_left_subarray = max_subarray(arr, low, mid)
  max_right_subarray = max_subarray(arr, mid+1, high)
  max_middle_subarray = max_mid_subarray(arr, low, high)

  return max(max_left_subarray, max_right_subarray , max_middle_subarray)

a = [33, -13, -10, 10, -3, -2, 4,7,8,9,11,-2,4,-5]
print(max_subarray(a, 0, len(a)-1))
