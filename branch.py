
"""if 3 < 5:
    print("aaa")
print("bbb")
"""

"""

score = input("input numbere")
score = int(score)

if 0 < score < 60:
    print("C")
elif 60 <= score < 80:
    print("B")
elif 80 <= score <= 100:
    print("A")
else:
    print("please input nummber 1--100")
"""

"""
age = 16
print("age < 18") if age < 18 else print("age > 18")

isMale = True

if age > 18:
    print ("yes aa")
else:
    if isMale:
        print("nested if")
    else:
        print("ddddd")
"""

#while else结构 可以不使用标志位就判断循环是否正常执行完，只有循环正常执行完才会执行else
#需要连续7天yes
'''
day = 1
while day <= 7:
    answer = input("today work hard?")
    if answer != "yes":
        break
    day += 1
else:
    print("great!")
'''

'''
for each in "hello":
    print(each)


for i in range(11):
    print(i)
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n,"是质数")
