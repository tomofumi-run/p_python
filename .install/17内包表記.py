# 内包表記(リストやジェネレータを生成、加工する)

# 0 - 9

print([i for i in range(10)])
# rangeで生成した0~9をiに入れて(in)iとして取り出す(i)

# 要素を加工(3倍)
print([i * 3 for i in range(10)])

# 数が偶数であれば要素を3倍して返す
print([i * 3 for i in range(10) if i % 2 == 0])
