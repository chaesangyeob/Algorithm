
def find_max(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

def main():
  print(find_max([1,7,5,3,3,3,1112]))

if __name__ == '__main__':
  main()
