import random

count = 0
extra = "!@#$%^&*"
res = []

while count <= 3:
    res.append(chr(random.randint(65,90)))  # Upper
    res.append(chr(random.randint(97,122))) # Lower
    res.append(str(random.randint(0,9)))    # Number
    res.append(extra[random.randint(0,7)])  # Special
    count += 1

random.shuffle(res)  
print("".join(res))  
 
