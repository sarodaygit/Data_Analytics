a = 18
if a >= 18:
    print("You are an adult")
else:
    print("You are a child")

b = 85
if b >= 80:
    print("You got an A")
elif b >= 70:
    print("You got a B")
else:
    print("You got a C")

c = 15
if c > 0:
    print("You are an positive number")
    if c % 2 == 0:
        print("You are even")
    else:
        print("You are odd")
else:
    print("c is less then  0")

x = 10
y = 20

max = x if x > y else y
print(max)