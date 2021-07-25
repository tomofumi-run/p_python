# イテレーター 次のデータを返す集合体

scores = [40, 50, 70, 90, 60]

it = iter(scores) # イテレーターに変換
print(next(it)) # 40
print(next(it)) # 50
print("hello")
print(next(it)) # 70

for score in scores: # 児童的にイテレーターに変換して、繰り返し処理している
  print(scores) # 内部でnextを呼び出している

def get_infinite(): # ジェネレーター = イテレーターの土台
  i = 0
  while True:
    yield i * 2
    i += 1

g = get_infinite() # 変数に代入する必要がある
print(next(g)) # 1回目だよ
print(next(g)) # 2回目だよ
print(next(g)) # 3回目だよ
