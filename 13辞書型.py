# 辞書型

sales = { "tomofumi":100, "fukui":300 }
print(sales["tomofumi"])
sales["tomofumi"] = 10000

sales["satou"] = 500
del(sales["fukui"])

print(sales)

for key, value in sales.items(): # 繰り返し処理
  print("{0}:{1}".format(key,value))