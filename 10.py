class MyException(Exception): # 独自の例外処理をExceptionを継承して作成
  pass

def div(a,b):
  try:
    if (b < 0): # bが0以下の場合
      raise MyException("0以下は困る") # と表示させる
    print(a / b)
  except ZeroDivisionError:
    print("0は困る")
  except MyException as e: # eという変数でerror内容受け取る
    print(e) # error内容を表示
  else:
    print("問題なし")
  finally:
    print("終了")

div(10,2)
div(10,0)
div(10,-5)