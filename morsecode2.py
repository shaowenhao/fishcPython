c_table = {".-":"A","-...":"B"}

code = input("input morese code:")

split_code = code.split(" ")

result = [ c_table[each] for each in split_code]
print(result)
