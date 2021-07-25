# 集合型

# セット

num1 = {5, 3, 8, 5} # 重複は表示しない
print(3 in num1) # 指定はできない。期待する値が含まれているかどうかを確認
num1.add(1)
num1.remove(3) # {5, 1, 8}
print(len(num1))

num2 = {5, 2, 8}

print(num1 | num2) # 和集合
print(num1 & num2) # 積集合 5 8
print(num1 - num2) # 差集合 1