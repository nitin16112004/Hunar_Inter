import random
characters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
captcha=''
for _ in range(5):
    captcha+=random.choice(characters)
print("Your CAPTCHA is:",captcha)
