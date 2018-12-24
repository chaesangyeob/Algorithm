import copy
from functools  import reduce

def func(a):
  li = list(str(a))
  print(li)
  do = reduce(lambda x,y: int(x)+int(y), li)
  print(do)



if __name__ =="__main__":
  func(123)
