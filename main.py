import random

ans = random.randint(1,10)
print("数字当てゲーム開始！", end = "")
num = int(input())

if ans == num:
  print("正解です！！おめでとうございます")
elif ans > num:
  print("小さすぎ！")
elif ans < num:
  print("大きすぎ！")

print("答えは %i" %ans)