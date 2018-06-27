import string, random

pool = string.ascii_lowercase + string.digits
number = 200
lenght = 8
code_pool = []
while len(code_pool) <number:
    code = ''
    for i in range(lenght + 1):
        code = code + random.choice(pool)
    if code not in code_pool:
        code_pool.append(code)
print(len(code_pool))
#print(code_pool)
print(random.choices(code_pool))