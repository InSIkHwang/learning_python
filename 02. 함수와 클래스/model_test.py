class userCalculator:
  varsion = 1.0   # 클래스 변수

  def add(self, a, b):
    return a+b
  
  def sub(self, a, b):
    return a-b
  
def aaa():
  indata=[1,2,3,4,5]
  tot = 0
  for data in indata:
    tot += int(data)

  return indata, tot

userList=[1,2,3,4,5,6,7,8,9,10]

if __name__ == "__main__":
  
  print(__name__) #현재 실행되고 있는 위치(__main__ == 자기자신)

  a, b = aaa(1,2,3,4,5,6,7,8,9,10)
  print(a, b)