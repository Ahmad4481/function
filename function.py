def count (string,a) -> int:
  string=str(string)
  if type(string)==list:
    def to_list(list):
      word = ''
      for item in list:
        word+= str(item)
      word= string
      return word
    string=(to_list(string))
  a=str(a)
  w=0
  for i in string:
    if i == a:
      w+=1
  return w
# print(count('elzero','e'))

def repeat(string:str,re:int,space=' ',end_space:bool=False):
  integar= string
  string=str(string)
  word = ''
  for i in range(re):
    if end_space== False:
      word+= string
      if re-1 > i:
        word += space
    else:
      word+= string+space
  return word
# print (repeat(8888,6,'#',True))

def zfill(st,width:int,fill:str='0') -> str:
  st=str(st)
  len(st)
  while True:
    if len(st)==width:
      return st
    else:
      st=fill+st
# print(zfill('999',4,'#'))

def reverse(st:str):
  word = ''
  for i in st:
    word= i+word
  return word
# print(reverse('orezle'))

def minmal(lst,minOrMax='minmal'):
  num = lst[0]
  for i in lst:
    if minOrMax=='minmal':
      if i<num:
        num=i
    elif minOrMax=='max' or 'maxmal':
      if i>num:
        num=i
  return num
# print(minmal([-220,392,933,444]))



