#摩斯密文表
c_table = [".-", "-..."]

#摩斯明文表
d_table = ["A", "B"]

code = input("input morse code:")
split_code = code.split(" ")

result = [d_table[c_table.index(each)] for each in split_code]
print(result)
