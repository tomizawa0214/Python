# coding:utf-8

sales = {"taguchi": 200, "fkoji": 400}
print(sales["taguchi"])
sales["taguchi"] = 300
sales["dotinstall"] = 500
del(sales["fkoji"])
print(sales)

for key, value in sales.items():
    print("{0}: {1}".format(key, value))
