# Generator functions must include yield instead of return OR can be made with a loop as seen in the xor_d function 

def gen_demo():
    
    n = 100
    yield n 
    
    n += 20
    yield n
    
    n += 10
    yield n

print("\n \n")

demo = gen_demo()

print(demo)

print(next(demo))
print(next(demo))
print(next(demo))


print("\n \n")


xor_d = (chr(ord(i) ^ 0x5) for i in "hello")

print(next(xor_d))

for word in xor_d:
    print(word)