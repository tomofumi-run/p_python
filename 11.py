# リスト
scores = [40, 50] # 配列
print(scores)
scores[0] = 1
print(scores)
print(len(scores)) # 長さを取得 length
scores.append(100) # 要素を追加

for score in scores: # scoresをscoreに代入していって表示
  print(score)

for i, score in enumerate(scores): # enumerateは組み込み関数、番号を取得できる
  print("{0}: {1}".format(i,score))

# タプル(値の変更ができない)
items = (50, "りんご", 32.5)
print(items[0])
# items[1] = "apple" # これができない

list((1,3,5)) # listからtupleへ
tuple([1,3,5]) # tupleからlistへ
