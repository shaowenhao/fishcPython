Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,3,4,5]
[1, 2, 3, 4, 5]
>>> 
>>> [1,2,3,4,5,"上山打老虎"]
[1, 2, 3, 4, 5, '上山打老虎']
>>> 
>>> lb = [1,2,3,4,5,"上山打老虎"]
>>> print(lb)
[1, 2, 3, 4, 5, '上山打老虎']
>>> 
>>> 
>>> for each in lb:
	print(each)

	
1
2
3
4
5
上山打老虎
>>> 
>>> 
>>> 
>>> lb[0]
1
>>> lb[1]
2
>>> 
>>> 
>>> lb[5]
'上山打老虎'
>>> 
>>> 
>>> lb[len(lb) - 1]
'上山打老虎'
>>> lb[-1]
'上山打老虎'
>>> 
>>> 
>>> lb[0:3]
[1, 2, 3]
>>> 
>>> lb[3:6]
[4, 5, '上山打老虎']
>>> 
>>> 
>>> lb[:3]
[1, 2, 3]
>>> 
>>> 
>>> lb[3:]
[4, 5, '上山打老虎']
>>> 
>>> 
>>> lb[:]
[1, 2, 3, 4, 5, '上山打老虎']
>>> 
>>> 
>>> lb[0:6:2]
[1, 3, 5]
>>> 
>>> 
>>> 
>>> lb[::2]
[1, 3, 5]
>>> 
>>> 
>>> lb[::-2]
['上山打老虎', 4, 2]
>>> 
>>> 
>>> lb[::-1]
['上山打老虎', 5, 4, 3, 2, 1]
>>> 
>>> 
>>> 
>>> 
>>> heros = ["钢铁侠","绿巨人"]
>>> 
>>> heros.append("黑寡妇")
>>> 
>>> heros
['钢铁侠', '绿巨人', '黑寡妇']
>>> 
>>> 
>>> heros.extend(["灭霸","雷神"])
>>> heros
['钢铁侠', '绿巨人', '黑寡妇', '灭霸', '雷神']
>>> 
>>> 
>>> s = [1,2,3,4,5]
>>> s[len(s):] = [6]
>>> s
[1, 2, 3, 4, 5, 6]
>>> s[len(s):] = [7,8,9]
>>> s
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> s = [1,3,4,5]
>>> s.insert(1,2)
>>> s
[1, 2, 3, 4, 5]
>>> 
>>> s.insert(len(s),6)
>>> s
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> heros.remove("灭霸")
>>> heros
['钢铁侠', '绿巨人', '黑寡妇', '雷神']
>>> 
>>> heros.remove("悟空")
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    heros.remove("悟空")
ValueError: list.remove(x): x not in list
>>> 
>>> heros.pop("黑寡妇")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    heros.pop("黑寡妇")
TypeError: 'str' object cannot be interpreted as an integer
>>> heros.pop(2)
'黑寡妇'
>>> heros
['钢铁侠', '绿巨人', '雷神']
>>> 
>>> heros.clear()
>>> heros
[]
>>> 
>>> 
>>> 
>>> heros = ["蜘蛛侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
>>> 
>>> heros[4] = "钢铁侠"
>>> 
>>> heros
['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '钢铁侠', '雷神']
>>> 
>>> heros[3:] = ["武松","林冲","李逵"]
>>> 
>>> heros
['蜘蛛侠', '绿巨人', '黑寡妇', '武松', '林冲', '李逵']
>>> 
>>> nums = [3,1,9,6,8,3,5,3]
>>> nums.sort()
>>> nums
[1, 3, 3, 3, 5, 6, 8, 9]
>>> 
>>> nums.reverse()
>>> nums
[9, 8, 6, 5, 3, 3, 3, 1]
>>> 
>>> nums = [3,1,9,6,8,3,5,3]
>>> nums.sort(reverse=True)
>>> nums
[9, 8, 6, 5, 3, 3, 3, 1]
>>> 
>>> 
>>> nums.count(3)
3
>>> heros.index("武松")
3
>>> 
>>> heros
['蜘蛛侠', '绿巨人', '黑寡妇', '武松', '林冲', '李逵']
>>> 
>>> heros[heros.index("李逵")] = "宋江"
>>> 
>>> heros
['蜘蛛侠', '绿巨人', '黑寡妇', '武松', '林冲', '宋江']
>>> 
>>> 
>>> 
>>> nums = [3,1,9,6,8,3,5,3]
>>> 
>>> nums.index(3,1,7)
5
>>> 
>>> nums.copy()
[3, 1, 9, 6, 8, 3, 5, 3]
>>> nums_copy1 =  nums.copy()
>>> nums_copy1
[3, 1, 9, 6, 8, 3, 5, 3]
>>> 
>>> nums_copy2 = nums[:]
>>> nums_copy2
[3, 1, 9, 6, 8, 3, 5, 3]
>>> 
>>> """列表的加法和乘法"""
'列表的加法和乘法'
>>> 
>>> s = [1,2,3]
>>> t = [4,5,6]
>>> s + t
[1, 2, 3, 4, 5, 6]
>>> #加法即为拼接
>>> 
>>> 
>>> 
>>> s * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> #列表中的元素重复 3 次
>>> 
>>> 
>>> #嵌套列表
>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
>>> #访问嵌套列表
>>> for i in matrix:
	for each in i:
		print(each)

		
1
2
3
4
5
6
7
8
9
>>> 
>>> 
>>> 
>>> for i in matrix:
	for each in i:
		print(each, end=' ')
	print()

	
1 2 3 
4 5 6 
7 8 9 
>>> 
>>> matrix[0]
[1, 2, 3]
>>> matrix[0][0]
1
>>> matrix[1][1]
5
>>> matrix[2][2]
9
>>> 
>>> 
>>> A = [0] * 3
>>> A
[0, 0, 0]
>>> 
>>> for i in range(3):
	A[i] = [0] * 3

	
>>> A
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 
>>> x='test'
>>> y='test'
>>> x is y
True
>>> 
>>> x = [1,2,3]
>>> y = [1,2,3]
>>> x is y
False
>>> 
>>> 
>>> 
>>> x = [1,2,3]
>>> y = x
>>> x[1] = 1
>>> x
[1, 1, 3]
>>> y
[1, 1, 3]
>>> 
>>> 
>>> x = [[1,2,3],[4,5,6],[7,8,9]]
>>> y = x.copy()
>>> x[1][1] = 0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> 
>>> import copy
>>> 
>>> x = [[1,2,3],[4,5,6],[7,8,9]]
>>> y =  copy.copy(x)
>>> x[1][1] = 0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> 
>>> x = [[1,2,3],[4,5,6],[7,8,9]]
>>> y = copy.deepdopy(x)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    y = copy.deepdopy(x)
AttributeError: module 'copy' has no attribute 'deepdopy'
>>> y = copy.deepcopy(x)
>>> x[1][1] = 0
>>> x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
>>> y
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> # 1维列表的copy 想，x,y不会互相影响（修改X的某个值）
>>> # 2维 需要深拷贝和浅拷贝区分
>>> 
>>> #列表推导式
>>> 
>>> oho = [1,2,3,4,5]
>>> for i in range(len(oho)):
	oho[i] = oho[i] * 2

	
>>> oho
[2, 4, 6, 8, 10]
>>> 
>>> [expression for target in interable]
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    [expression for target in interable]
NameError: name 'interable' is not defined
>>> x = [i for i in range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = [i + 1 for i in range(10)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> y = [c * 2 for c in "FishC"]
>>> y
['FF', 'ii', 'ss', 'hh', 'CC']
>>> 
>>> matrix = [[1,2,3],
	      [4,5,6],
	      [7,8,9]]
>>> col2 = [row[1] for row in matrix]
>>> col2
[2, 5, 8]
>>> 
>>> diag = [matrix[i][i] for i in range(len(matrix))]
>>> diag
[1, 5, 9]
>>> 
>>> diag = [matrix[2-i][i] for i in range(len(matrix)-1,0,-1)]
>>> diag
[3, 5]
>>> diag = [matrix[3-i][i-1] for i in range(len(matrix),0,-1)]
>>> diag
[3, 5, 7]
>>> 
>>> 
>>> S = [[0] * 3 for i in range(3)]
>>> S
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 
>>> 
>>> S[1][1] = 1
>>> s
[1, 2, 3]
>>> S
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
>>> 
>>> #列表推导式还可以加if
>>> even = [i for i in range(10) if i % 2 == 0]
>>> even
[0, 2, 4, 6, 8]
>>> 
>>> words = ["Greate","FishC","Brilliant","Excellent","Fantistic"]
>>> 
>>> count = [i for i in words if i[0] == 'F']
>>> count
['FishC', 'Fantistic']
>>> 
>>> 
>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> flatten = [col for row in matrix for col in row]
>>> flatten
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> flatten = []
>>> for row in matrix:
	for col in row:
		flatten.append(col)

		
>>> fatten
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    fatten
NameError: name 'fatten' is not defined
>>> flatten
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 