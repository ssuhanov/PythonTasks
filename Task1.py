a = "First Red Second Green"
print(a.split())
print([a[0], a[6], a[10], a[17]])
print(a[-1])

print(a[6:9])
print(a[:5])
print(a[17:])

print(a.find("Second"))
print(a[a.find("Second"):])

b = a[::2]
print("b = ", b)

c = a[1::2]
print("c = ", c)

print(a[::-1])
