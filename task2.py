import random
import string

def otp():
    x = random.choices(string.digits,k = 6)
    num = ''.join(x) 
    print(num)
def password():
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    punc = random.choice(string.punctuation)

    remain = string.ascii_letters+string.digits
    remain = ''.join(random.choices(remain,k = 3))
    
    finalpas = list(lower+upper+punc+remain )
    random.shuffle(finalpas)
    finalpas = ''.join(finalpas)
    
    print(finalpas)
otp()    
password()
