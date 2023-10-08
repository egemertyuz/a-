import random 

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("kaç uzunlukta şifre istersiniz?"))

şifre = ""

for i in range (uzunluk):
    şifre += random.choice(karakterler)

print (şifre)