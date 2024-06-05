# Number Guessing Game
import random

x = random.randrange(1,100)
# print(x)
guess = int(input("0 ile 100 arasında olan sayıyı tahmin ediniz: "))

while guess != x:
    if guess < x:
        print("Yukarı")
        guess = int(input("0 ile 100 arasında olan sayıyı tekrar tahmin ediniz: "))
    elif guess > x:
        print("Aşağı")
        guess = int(input("0 ile 100 arasında olan sayıyı tekrar tahmin ediniz: "))
    else:
        break
print("Sayıyı Doğru Tahmin Ettiniz. Tebrikler.") 