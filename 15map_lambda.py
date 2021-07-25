# map(関数,イテレータ)

def triple(n):
  return n * 3

# tripleという関数で配列を処理する。
print(list(map(triple, [1,2,3]))) # [3,6,9]
# map はジェネレータなのでlistに変換して見やすくする

# lambda 引数: 処理 nが引数 nに3を掛け算する
print(list(map(lambda n: n * 3, [1,2,3]))) # [3,6,9]
