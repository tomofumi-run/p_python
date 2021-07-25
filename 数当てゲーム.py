import random

ans = random.randint(1,10)
count = 0

while True:
  print("数字当てゲーム開始！", end = "")
  num = int(input())
  count += 1
  if ans == num:
    print("正解です！！おめでとうございます")
    print("正解までのカウントは %i です" %count)
    break
  elif ans > num:
    print("小さすぎ！")
  elif ans < num:
    print("大きすぎ！")