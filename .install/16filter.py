# filter(関数,イテレータ) 条件に合致したモノを抽出

def is_even(n):
  return n % 2 == 0 # 偶数はtrue

# print(list(filter(is_even, range(10))))
# rangeで0~9を準備,rangeにメソッドを使用
print(list(filter(lambda n: n % 2 == 0, range(10))))
