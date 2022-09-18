
import random

counts = 3
answer = random.randint(1,10)

while counts > 0:        
    temp = input("猜一下我心里想的数字：")
    guess = int(temp)

    if guess == answer:
        print("correct")
        break
    else:
        if guess < answer:
            print("small")
        else:
            print("bigger")
    counts = counts - 1
print("game over")
print("correct answer was:" + str(answer))
