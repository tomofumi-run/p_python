# 関数

def  greeting(name="ボビーオロゴン",age=20):
  print("{0}さん、こんにちは!!え！！{1}歳なんですか？".format(name,age))
  if age < 20:
    print("エネルギッシュですね！")
  elif age > 29:
    print("年齢よりお若く見えますね！")
  else:
    print("もう一度ご年齢をお伺いしてもよろしいですか？")



greeting()